# Career Peek - Setup Guide

This document provides instructions for setting up the Career Peek application for development.

## Prerequisites

- Docker and Docker Compose
- Git
- Python 3.11 (for local development outside Docker)
- Node.js and npm (for frontend development)

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/knail1/career-peek.git
cd career-peek
```

### 2. Start the Docker Containers

```bash
docker-compose up -d
```

This will:
- Start a PostgreSQL database container
- Build and start the Flask API container
- Mount the local directories for development

### 3. Verify the Setup

Check if the containers are running:

```bash
docker-compose ps
```

Test the API health endpoint:

```bash
curl http://localhost:5000/health
```

You should see a response like:

```json
{
  "status": "healthy",
  "database": "connected"
}
```

### 4. Running Tests

To run the backend tests:

```bash
docker-compose exec api pytest
```

### 5. Development Workflow

- Backend code is in the `backend/` directory
- Frontend code will be in the `frontend/` directory
- Database migrations and seeds are in the `database/` directory

Changes to the code will be automatically reflected in the running containers due to the volume mounts.

### 6. Stopping the Application

```bash
docker-compose down
```

To remove all data (including the database volume):

```bash
docker-compose down -v
```