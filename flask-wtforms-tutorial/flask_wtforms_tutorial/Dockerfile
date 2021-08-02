FROM python:3.8

EXPOSE 5002

WORKDIR /flask-wtforms-tutorial

COPY requirements.txt /flask-wtforms-tutorial
RUN pip install  -r requirements.txt --upgrade pip

COPY . /flask-wtforms-tutorial

CMD python routes.py