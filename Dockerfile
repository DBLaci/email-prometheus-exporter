FROM python:3.9-slim

COPY email_exporter.py /app/email_exporter.py
WORKDIR /app
RUN pip install flask

CMD ["python", "/app/email_exporter.py"]
