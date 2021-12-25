# Multi-stage build. Used to make entrypoint.sh
# an executable.
FROM alpine as content
WORKDIR /app
COPY src entrypoint.sh requirements.txt ./
RUN chmod +x entrypoint.sh

# Main image
FROM python:3.9.5-slim-buster


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# Create one layer with all the extra dependencies our
# application needs.
RUN apt-get update \
  && apt-get -y install netcat # gcc postgresql \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*


WORKDIR /usr/src/app
# NOTE(hector) Comment this out for a moments
#   since it is faster to run the code from a volume
#   (specified in compose) than building the image
#   each time the code is changed.
#   Once we have a final version we can change this 
#   behavior and copy the code into the image.
# COPY --from=content /app ./
#RUN pip install -r requirements.txt
# ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

COPY requirements.txt .
RUN pip install -r requirements.txt
