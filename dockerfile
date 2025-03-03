FROM python:3.11-slim

WORKDIR /locadora

COPY . /locadora/
COPY ./requirements.txt /locadora/requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]