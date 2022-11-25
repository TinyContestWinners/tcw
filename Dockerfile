# Use slim buster images
FROM python:3.10-buster

# Make a working directory
RUN mkdir /tcw
WORKDIR /tcw

COPY ./requirements.txt /tcw
RUN pip install -r requirements.txt

COPY . /tcw

ENV FLASK_RUN_HOST 0.0.0.0
EXPOSE 5000

# Run Flask command
CMD ["gunicorn", "-b", "0.0.0.0:5000", "tcw.run:app"]
