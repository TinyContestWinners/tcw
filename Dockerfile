FROM python:3.10-buster

# compile and install driver for postgresql
RUN apt-get update && apt-get install -y libpq-dev gcc
RUN pip install psycopg2

RUN mkdir /tcw
WORKDIR /tcw

COPY ./requirements.txt /tcw
RUN pip install -r requirements.txt

COPY . /tcw

ENV FLASK_RUN_HOST 0.0.0.0
EXPOSE 8080

# Run Flask command
CMD ["gunicorn", "-b", "0.0.0.0:8080", "tcw.app:app"]
