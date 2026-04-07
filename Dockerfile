# Dockerfile
# Simple Python environment for the Traffic Signal RL project.
# No external ML libraries required — only the Python standard library.

FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all project files
COPY . .

# No pip install needed — project uses only Python's standard library

# Default command: run the simulation
CMD ["python", "main.py"]
