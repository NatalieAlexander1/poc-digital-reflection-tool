 # Self-Care Journal: A Digital Reflection Tool

## Project Overview

Self-Care Journal is a web application designed to help users reflect on their daily experiences, practice gratitude, and identify their strengths and areas for improvement. This digital journaling tool aims to promote mental well-being and personal growth through consistent self-reflection.

## Key Features

1. User Authentication
2. Daily Reflection Journal
3. Gratitude Log
4. Goal Setting and Progress Monitoring

## Technology Stack

- Backend: Flask (Python)
- Frontend: HTML, CSS, JavaScript, Bootstrap
- Database: MySQL
- Cloud Platform: Azure
- Additional Tools: Socket.IO for real-time communication, Flask-SQLAlchemy for ORM

## Directory Structure

/accountify
├── run.py               # Main file to start the Flask app
├── app.py               # Backend logic and routes
├── requirements.txt     # Dependencies for the project
├── templates/           # HTML files for the frontend
│   ├── login.html       # Login page
│   ├── dashboard.html   # Main dashboard (includes journal, gratitude, and goals)
│   ├── register.html    # Registration page
├── static/              # Static assets (CSS, JS)
│   ├── styles.css       # Custom styles
│   ├── index.js         # Main JavaScript file for frontend logic
├── models.py            # Database models
