# MusicXML Web Viewer & Analyzer

## Name

Uday Jajala

---

## Project Overview

This project is a simple and interactive web application where I can upload and view MusicXML files directly in the browser. The main goal of this project is to show how a frontend application can handle user input, call backend APIs, and display complex data in a clean and understandable way.

I built this project focusing more on user interaction, smooth UI flow, and proper connection between frontend and backend. The application takes a MusicXML file, processes it in the backend, and shows the output in a structured and visual format on the frontend.

---

## What This Project Demonstrates

| Area                 | What I Implemented                               |
| -------------------- | ------------------------------------------------ |
| Frontend Interaction | Upload, dropdown selection, buttons, inputs      |
| API Integration      | Sending files to backend and receiving responses |
| Dynamic UI           | Updating content without refreshing the page     |
| Data Visualization   | Rendering sheet music using a library            |
| User Experience      | Smooth navigation and interaction                |
| State Handling       | Managing selected file and results in UI         |

---

## Technologies Used

| Category         | Technology              |
| ---------------- | ----------------------- |
| Frontend         | HTML5, CSS3, JavaScript |
| Backend          | Python (Flask)          |
| Music Processing | music21                 |
| Visualization    | OpenSheetMusicDisplay   |
| Communication    | REST APIs               |

---

## Features

* Upload MusicXML file from local system
* Load demo files from project dataset
* Extract and display metadata like title, composer, parts, and measures
* Render sheet music directly in the browser
* Transpose music by changing pitch values
* Navigate to a specific measure using input
* Search notes or rhythm and find matching measures
* Automatically scroll to selected measure
* UI updates dynamically without page reload

---

## Application Flow

1. User uploads a file or selects a demo file
2. Frontend sends the file to backend using API
3. Backend processes file using music21
4. Metadata is returned and shown on UI
5. Same file is rendered as sheet music in browser
6. User can interact using transpose, navigation, and search features

---

## Frontend Understanding

In this project, I focused on how frontend handles data and user interaction.

* I used JavaScript to manage the application state like selected file and metadata
* UI updates are handled dynamically without refreshing the page
* Each section of the UI works independently, similar to component-based design
* API responses are directly reflected in the UI
* Rendering is handled using a client-side library

This approach is similar to how modern frontend frameworks work.

---

## How to Run

1. Install required packages
   py -m pip install flask music21

2. Run the application
   py app.py

3. Open browser
   [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## Dataset

The MusicXML files used in this project are taken from public sources like MuseScore. These files are used for testing upload, rendering, and search functionality.

---


## Summary

This project shows how a frontend application can interact with backend services and present complex data in a user-friendly way. It covers file handling, API communication, UI updates, and user interaction, which are important for frontend development.
