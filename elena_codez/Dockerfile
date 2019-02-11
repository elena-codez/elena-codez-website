FROM ubuntu:18.04

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install Python
RUN apt-get update -y \
    && apt-get install -y \
    python3.7 \
    python3.7-venv \
    python3.7-dev \
    python3-pip

# Copy the project folder
RUN mkdir elena_codez
WORKDIR /elena_codez
ADD . /elena_codez

# Instal Python dependencies
RUN python3.7 -m venv venv && . venv/bin/activate
RUN pip3 install -r requirements/base.txt

RUN chmod u+x entrypoint.sh
CMD gunicorn config.wsgi --bind 0.0.0.0:8000
