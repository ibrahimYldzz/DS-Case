FROM python:3.10.14-bullseye

RUN mkdir /app
WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8080
CMD ["gunicorn","--config", "gunicorn_config.py", "app:app"]