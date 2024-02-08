Dash Web Application README

Quick Start
===========

Build and Run with Docker
-------------------------

1. Build Docker Image:
   docker build -t mydashapp .

2. Run Container:
   docker run -p 2718:2718 mydashapp

Access the application at http://localhost:2718.

Development
-----------

- Python 3.8+
- Docker

Files
-----

- app.py: Main Dash application script with app layout and callbacks.
- Dockerfile: Contains instructions for Docker to build the application image.
- requirements.txt: Lists Python package dependencies for the application.
- /assets: Directory for CSS, JavaScript, and images used by the Dash app.
- /pages: Contains separate Python modules for each page of the multi-page app.

Structure
---------

The application is structured as follows:
- The main entry point is `app.py`, which sets up the Dash app, defines the layout, and includes callbacks for interactivity.
- The `Dockerfile` facilitates the creation of a Docker container for the app.
- Dependencies required by the application are listed in `requirements.txt`.
- Static files such as custom CSS are stored in the `/assets` directory.
- The `/pages` directory holds individual Python scripts for different pages in the multi-page app setup.

Docker Commands
---------------

- Build Image: docker build -t mydashapp .
- Run Container: docker run -p 2718:2718 mydashapp

Access Application
------------------

Open a web browser and navigate to http://localhost:2718 to interact with the Dash application.

