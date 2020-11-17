FROM python:latest

RUN pip install --upgrade pip
WORKDIR '/usr/src/heart-beat-client'
COPY './client.py' '/usr/src/heart-beat-client'
EXPOSE 80

CMD ["python", "client.py"]