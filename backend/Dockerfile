FROM python:3.10-slim-buster
ADD requirements.txt .
RUN pip install -r requirements.txt
COPY src/ /var/app/src/
CMD [ "python3", "/var/app/src/main.py"]
