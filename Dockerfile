# Multi-stage build. Used to make entrypoint.sh
# an executable.
FROM alpine as content
WORKDIR /app
COPY src entrypoint.sh requirements.txt ./
RUN chmod +x entrypoint.sh

# Main image
FROM python:3.9.5-slim-buster

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# Create one layer with all the extra dependencies our
# application needs.
RUN apt-get update \
  && apt-get -y install netcat # gcc postgresql \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

COPY --from=content /app ./
RUN pip install -r requirements.txt

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
