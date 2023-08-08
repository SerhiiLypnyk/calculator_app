# Django Calculator App

This repository contains the source code for a simple calculator app built with Django and Docker.

## Prerequisites

- **Docker**: Ensure you have Docker installed on your machine. If not, download and install it from [Docker's official website](https://www.docker.com/products/docker-desktop).
- **Docker Compose**: It typically comes installed with Docker Desktop, but if you need to install it separately, you can find the instructions on the [Docker Compose GitHub page](https://github.com/docker/compose).

## Setup & Run

### 1. Clone the repository
```
git clone https://github.com/SerhiiLypnyk/calculator_app.git
cd calculator_app
cd calculator
```

### 2. Build the Docker images
```
docker-compose build
```

### 3. Start the services
```
docker-compose up -d
```
This command starts the services in the background. If you prefer to view the logs in the foreground, simply omit the `-d` flag.

### 4. Access the app
Open your web browser and navigate to [http://localhost:8000/web/](http://localhost:8000/web/) to access the web interface of the calculator app.

## Running Tests
To run the tests for the Django app:
```
docker-compose run web python manage.py test
```

## Stopping the Services
To halt the services:
```
docker-compose down
```
