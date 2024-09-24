#FROM ubuntu:latest

#RUN apt-get update && \
   # apt-get install -y nginx ssh nano iputils-ping && \
   # apt-get clean

#EXPOSE 80

#CMD ["nginx", "-g", "daemon off;"]


FROM python:3.12-slim

WORKDIR /app


COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


COPY . .


EXPOSE 5000


CMD ["python", "app.py"]

