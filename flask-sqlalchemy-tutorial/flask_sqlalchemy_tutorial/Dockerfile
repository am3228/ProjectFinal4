FROM python:3.9

EXPOSE 5008

WORKDIR /flask-sqlalchemy-tutorial

COPY requirements.txt /flask-sqlalchemy-tutorial
RUN pip install  -r requirements.txt --upgrade pip

COPY . /flask-sqlalchemy-tutorial

CMD python routes.py