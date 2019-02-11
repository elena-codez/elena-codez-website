FROM python:3.7.2-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy the project folder
RUN mkdir elena_codez
WORKDIR /elena_codez
ADD . /elena_codez

# Instal Python dependencies
RUN pip install -r requirements/base.txt

ADD start.sh /elena_codez/start.sh
RUN chmod u+x start.sh
CMD /elena_codez/start.sh
