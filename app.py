from flask import Flask, request, jsonify, send_from_directory
from music21 import converter
import os

app = Flask(__name__)

@app.route("/")
def home():
    return send_from_directory("frontend", "index.html")

@app.route("/frontend/<path:path>")
def send_frontend(path):
    return send_from_directory("frontend", path)

@app.route("/data/scores/<path:path>")
def send_scores(path):
    return send_from_directory("data/scores", path)

@app.route("/api/parse", methods=["POST"])
def parse_musicxml():
    file = request.files["file"]
    file_path = "temp_file.mxl"
    file.save(file_path)
    score = converter.parse(file_path)
    metadata = {
        "title": str(score.metadata.title) if score.metadata else "Unknown",
        "composer": str(score.metadata.composer) if score.metadata else "Unknown",
        "parts": [p.partName for p in score.parts],
        "measure_count": len(score.parts[0].getElementsByClass('Measure'))
    }
    return jsonify(metadata)

@app.route("/api/scores", methods=["GET"])
def list_scores():
    files = os.listdir("data/scores")
    return jsonify(files)

@app.route("/api/transpose", methods=["POST"])
def transpose_music():
    file = request.files["file"]
    semitones = int(request.form["semitones"])
    file_path = "temp_transpose.mxl"
    file.save(file_path)
    score = converter.parse(file_path)
    score = score.transpose(semitones)
    output_path = "transposed.xml"
    score.write("musicxml", output_path)
    return send_from_directory(".", output_path, as_attachment=False)

@app.route("/api/search", methods=["POST"])
def search_music():
    file = request.files["file"]
    query = request.form["query"]
    file_path = "temp_search.mxl"
    file.save(file_path)
    score = converter.parse(file_path)
    results = []
    for part in score.parts:
        for measure in part.getElementsByClass('Measure'):
            for note in measure.notes:
                if note.isNote:
                    pitch = str(note.pitch)
                    duration = note.duration.type
                    if query.lower() in pitch.lower() or query.lower() in duration.lower():
                        results.append(measure.number)
    return jsonify({"matches": list(set(results))})

if __name__ == "__main__":
    app.run(debug=True)