FROM     python:3.9.7-slim AS builder
WORKDIR  /app
COPY	requirements.txt requirements.txt
COPY    . .
FROM     builder as dev-envs
RUN     pip install --upgrade pip --no-cache-dir
RUN	pip install -r /app/requirements.txt --no-cache-dir
CMD	[ "gunicorn", "-w", "3", "app:app", "--bind", "0.0.0.0:8000" ]