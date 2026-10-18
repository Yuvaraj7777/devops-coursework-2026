# Exercise 5: AppArmor with Docker

## Objective

Run a Flask application in Docker and explore how AppArmor can restrict
container operations.

## Project Structure

- `app.py` — Flask web application.
- `Dockerfile` — Builds the application image.
- `requirements.txt` — Python dependencies.
- `apply_apparmor.py` — Builds and runs the container with an AppArmor profile.
- `test_restricted_actions.py` — Tests file reading and command execution.
- `evidence/` — Stores genuine screenshots of the implementation and tests.

## Requirements

- Docker Desktop
- Python 3
- A Linux Docker host with AppArmor support for profile enforcement

## Build the Image

Run from this directory:

```bash
docker build -t flask-apparmor .