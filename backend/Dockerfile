FROM python:3.10-slim-buster
ADD requirements.txt .
RUN pip install -r requirements.txt
COPY src/ /var/app/src/
EXPOSE 8089
CMD [ "uvicorn", "main:app", "--app-dir", "/var/app/src/", "--port",  "8089", "--host", "0.0.0.0"]
