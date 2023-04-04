FROM python:3.11-slim-bullseye AS python

ENV PYTHONPATH=python

COPY requirements.txt requirements.txt

RUN apt-get update \
    && apt-get install -y \
    gcc \
    libpq-dev

RUN pip install -r requirements.txt

COPY ./python ./python

EXPOSE 5000

CMD ["python", "-m", "app"]
