FROM python:3.7-alpine
# directory for work
WORKDIR /app
RUN apk add --no-cache gcc musl-dev linux-headers  build-base 
# Copy requirements to docker container
COPY requirements.txt requirements.txt
# Install requirements on docker container
RUN pip3 install -r requirements.txt
# Expose port 5000 of container
EXPOSE 5000

