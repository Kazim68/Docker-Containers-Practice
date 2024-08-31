# Pull base image
FROM python:3.12.4-slim-bullseye

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY ./Requirements.txt .
RUN pip install -r Requirements.txt

# Copy project
COPY . .