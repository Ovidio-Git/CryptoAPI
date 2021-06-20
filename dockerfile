FROM python:3.7-alpine
# directory for work
WORKDIR /app
# configuration enviroment variables
#ENV FLASK_APP=app.py
#ENV FLASK_RUN_HOST=0.0.0.0
#ENV FLASK_ENV=development
#ENV FLASK_DEBUG=1  
RUN apk add --no-cache gcc musl-dev linux-headers  build-base 
# Copy requirements to docker container
COPY requirements.txt requirements.txt
# Install requirements on docker container
RUN pip3 install -r requirements.txt
# Expose port 5000 of container
EXPOSE 5000
COPY . .
# run flask server
#CMD ["flask", "run"]

CMD ["python3", "aux.py"]
