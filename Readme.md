# Flask App Docker Setup

This project demonstrates a Flask web application optimized for Docker, running on port 8080.

## Approach

### Dockerfile Optimization

1. **Multi-Stage Build**:
   - We used multi-stage builds to separate the build and runtime environments. This allows us to reduce the final image size by copying only the required dependencies from the build stage.
   
2. **Slim Base Image**:
   - Used `python:3.11-slim` as the base image to minimize the image size, which is ideal for production.
   
3. **Non-root User**:
   - The app runs as a non-root user (`myappuser`), enhancing security by following Docker best practices.
   
4. **Efficient Caching**:
   - By copying the `requirements.txt` file first and running `pip install` separately from copying the application code, we can leverage Docker's cache to avoid reinstalling dependencies unless they change.

## Assumptions

- Docker is installed and running on your machine.
- You have basic knowledge of Flask and Docker.
- The application files `app.py`, `model.py`, and `requirements.txt` are in the same directory.

## Instructions to Run

1. **Build the Docker Image**:
   Run the following command to build the Docker image:

   ```bash
   docker build -t flask-app .
