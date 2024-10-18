# Flask Application with Docker

This project demonstrates the setup and optimization of a simple Flask web application running inside a Docker container. The Flask application exposes a POST `/predict` endpoint that interacts with a mock model for prediction purposes. Docker is used to containerize the application for deployment and testing.

## Approach

### Objective

1. **Flask Application**:
   - Build a Flask app that provides a `/predict` POST endpoint to accept user input and return model predictions (mocked for this example).
   
2. **Docker Optimization**:
   - Create an optimized Docker image to package the Flask app using best practices such as multi-stage builds to reduce the image size and improve security.

### Steps Taken

1. **Flask Application**:
   - Built a basic Flask app with a synchronous POST `/predict` endpoint.
   - Utilized threading to handle asynchronous POST `/predict` endpoint.

2. **Docker Setup**:
   - Built a multi-stage Dockerfile to ensure the final image is optimized in size and security.
   - Used a **slim base image** (`python:3.11-slim`) for reduced size.
   - Created the image to run the app on port `8080`.

3. **Testing the App**:
   - Tested the app using the Invoke-WebRequest command in windows powershell.
   - Synchronous mode request can be made by accessing the localhost with port 8080 directly.
   - Asynchronous Mode POST:
    `Invoke-WebRequest -Uri http://localhost:8080/predict -Method POST -Headers @{"Async-Mode" = "true"} | ConvertFrom-Json | ConvertTo-Json -Depth 5`
   - Asynchronous Mode GET:
    `Invoke-WebRequest -Uri http://localhost:8080/predict/<prediction id returned by the post request command> -Method GET | ConvertFrom-Json | ConvertTo-Json -Depth 5`
   - Used Docker to containerize the application, ensuring the app can be run in different environments.

---

## Project Files

- **app.py**: Contains the Flask app with the `/predict` POST endpoint.
- **model.py**: Contains the mock model's prediction logic.
- **Dockerfile**: Contains the instructions to build the Docker image for the Flask app.
- **requirements.txt**: Lists the Python dependencies needed for the app.

---

## Setup Instructions

### Prerequisites

- **Docker** must be installed and running on your local machine.
- **Python 3.x** must be installed on your local machine if you wish to run the app outside Docker.
- Basic knowledge of Flask and Docker is recommended.

### 1. Build the Docker Image

To build the Docker image, open a terminal or command prompt and navigate to the project directory (where the `Dockerfile` is located). Run the following command:

```bash
docker build -t flask-app .


## Running the app

```
docker run -p 8080:8080 flask-app