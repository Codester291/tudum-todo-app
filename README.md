FastAPI Todo Application
========================

A simple Todo API built with **FastAPI**, containerized with **Docker**, and deployed to **AWS EC2** using a **CI/CD pipeline**with **GitHub Actions**.

Table of Contents
-----------------

-   [Project Overview](#project-overview)
-   [Features](#features)
-   [Technologies Used](#technologies-used)
-   [Prerequisites](#prerequisites)
-   [Setup Instructions](#setup-instructions)
-   [Clone the Repository](#1-clone-the-repository)
-   [Create and Activate a Virtual Environment](#2-create-and-activate-a-virtual-environment)
-   [Install Dependencies](#3-install-dependencies)
-   [Running the Application](#running-the-application)
-   [Run with Uvicorn](#1-run-with-uvicorn)
-   [Run with Docker](#2-run-with-docker)
-   [CI/CD Pipeline](#cicd-pipeline)
-   [Github Actions Workflow](#github-actions-workflow)
-   [Environment Variables for Github Secrets](#environment-variables-for-github-secrets)
-   [API Endpoints](#api-endpoints)
-   [License](#license)

Project Overview
----------------

This project is a simple RESTful API that allows users to manage todo items. It demonstrates the use of FastAPI for building APIs, Docker for containerization, and GitHub Actions for CI/CD automation. The application is deployed on an AWS EC2 instance.

Features
--------

-   Create, read, update, and delete todo items.
-   RESTful API endpoints.
-   In-memory data storage (can be extended to use a database).
-   Dockerized application for consistent deployment.
-   Automated CI/CD pipeline for deployment.

Technologies Used
-----------------

-   **Python 3.8**: Programming language.
-   **FastAPI**: Modern web framework for building APIs.
-   **Uvicorn**: ASGI server implementation for FastAPI.
-   **Docker**: Containerization platform.
-   **GitHub Actions**: CI/CD automation for testing and deployment.
-   **AWS EC2**: Cloud computing service for hosting the application.

Prerequisites
-------------

Before you begin, ensure you have the following installed:

-   **Python 3.8+**
-   **Docker**
-   **Git**
-   **AWS Account**
-   **GitHub Account**
-   **Docker Hub Account**

Setup Instructions
------------------

### 1\. Clone the Repository

```
git clone https://github.com/Codester291/tudum-todo-app.git
cd tudum-todo-app
```

### 2\. Create and Activate a Virtual Environment

```
python3 -m venv venv
```

-   MacOS/Linux

```
source venv/bin/activate
```

-   Windows

```
venv\Scripts\activate
```

### 3\. Install Dependencies

```
pip install -r requirements.txt
```

Running the Application
-----------------------

### 1\. Run with Uvicorn

```
uvicorn main:app --reload
```

### 2\. Run with Docker

1.  Build Docker Image:

```
docker build -t <container-name> .
```

1.  Run Docker Container:

```
docker run -d --name <container-name> -p 80:80 <image-name>
```

Access the API at <http://localhost/docs>

CI/CD Pipeline
--------------

This project uses GitHub Actions for continuous integration and deployment. The workflow:

### GitHub Actions Workflow

1.  Runs tests on every push
2.  Builds Docker image
3.  Pushes to Docker Hub
4.  Deploys to AWS EC2

### Environment Variables for GitHub Secrets

Set up the following secrets in your GitHub repository:

-   `AWS_ACCESS_KEY_ID`
-   `AWS_SECRET_ACCESS_KEY`
-   `AWS_REGION`
-   `EC2_HOST`
-   `EC2_PRIVATE_KEY`
-   `DOCKER_USERNAME`
-   `DOCKER_PASSWORD`

API Endpoints
-------------

| Method | Endpoint | Description |

|--------|----------|-------------|

| GET | `/todos/` | List all todos |

| POST | `/todos/` | Create a new todo |

| GET | `/todos/{id}` | Get a specific todo |

| PUT | `/todos/{id}` | Update a todo |

| DELETE | `/todos/{id}` | Delete a todo |

| PATCH | `/todos/{id}/complete` | Mark a todo as complete |

License
-------

This project is licensed under the MIT License - see the <LICENSE> file for details.