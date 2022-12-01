FROM python:3.10-buster

RUN mkdir /tcw
WORKDIR /tcw

COPY ./requirements.txt /tcw
RUN pip install -r requirements.txt
RUN pip install -e .

COPY . /tcw

ENV FLASK_RUN_HOST 0.0.0.0
EXPOSE 80

# Run Flask command
CMD ["gunicorn", "-b", "0.0.0.0:80", "tcw.run:app"]
