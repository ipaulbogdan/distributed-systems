FROM python:latest

RUN pip install --upgrade pip
WORKDIR '/usr/src/heart-beat-server'
COPY './server.py' '/usr/src/heart-beat-server'
EXPOSE 80

CMD ["python", "server.py"]