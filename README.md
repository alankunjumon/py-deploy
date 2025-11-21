# Py-Deploy: Automated CI/CD Pipeline for Python

## 🚀 Project Overview
Py-Deploy is a full-stack To-Do application built with **Python Flask** and **PostgreSQL**. It demonstrates a complete **DevOps lifecycle**, moving from local development to containerization and automated cloud deployment.

## 🛠️ Tech Stack
* **Application:** Python 3.10, Flask
* **Database:** PostgreSQL 14
* **Containerization:** Docker & Docker Compose
* **CI/CD:** GitHub Actions (Automated Build & Push)
* **Cloud Infrastructure:** AWS EC2 (Ubuntu Linux)
* **Server:** Gunicorn WSGI

## ⚙️ Key Features
* **Containerized Architecture:** Fully isolated application and database services using Docker.
* **Persistent Storage:** Data persistence managed via Docker Volumes.
* **Automated CI Pipeline:** GitHub Actions workflow triggers on every push to build and push images to Docker Hub.
* **Cloud Hosted:** Deployed on a live AWS EC2 instance.

## 🔧 How to Run Locally
1.  Clone the repository.
2.  Run with Docker Compose:
    ```bash
    docker-compose up -d
    ```
3.  Access the app at `http://localhost:5000`.
