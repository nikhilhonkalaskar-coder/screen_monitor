#  Real-Time Employee Activity Monitoring System (Demo)

This project is a **real-time screen monitoring tool** built for learning and experimentation. It demonstrates how monitoring systems work by capturing screenshots from client machines and displaying them on a centralized dashboard.

##  Overview
The system consists of a Python-based client (agent) that captures screenshots at regular intervals and sends them to a Flask backend server via REST APIs. The server processes and stores the images, which are then displayed on a live web dashboard.

>  Note: This project is currently designed for **local testing and educational purposes only**.

##  Tech Stack
- Python (Screenshot Agent)
- Flask (Backend API)
- HTML/CSS (Dashboard UI)
- REST APIs

## ⚙️ Features
-  Periodic screenshot capture
-  Client-to-server communication using APIs
-  Live dashboard to view latest screenshots
-  Multi-client support using unique system IDs
-  Local environment setup for testing

##  Project Structure


##  Current Limitations
- Runs only on local network
- Basic UI (no advanced real-time streaming)
- Minimal security implementation

##  Learnings
- Understanding client-server architecture
- Working with Flask APIs
- Handling file uploads and errors
- Building a simple monitoring dashboard

##  Future Improvements
- Deployment to cloud (AWS/Render)
- Authentication & security enhancements
- Real-time streaming (WebSockets)
- Database integration
- Performance optimization

##  Disclaimer
This project is intended for **educational purposes only**. Monitoring systems should always be used ethically and with proper user consent.

---

 Feel free to contribute, suggest improvements, or fork the project!
