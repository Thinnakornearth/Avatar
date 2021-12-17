FROM python:3.9
COPY . /app
WORKDIR /app
RUN pip install pipenv
RUN pipenv install
ENTRYPOINT ["/bin/sh", "-c", "pipenv run flask db upgrade && pipenv run flask run --host=check-visa-status"]

