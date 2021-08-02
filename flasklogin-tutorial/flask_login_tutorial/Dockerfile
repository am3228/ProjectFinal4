FROM python:3.8

EXPOSE 5009

WORKDIR /flask_login_tutorial

COPY requirements.txt /flask_login_tutorial
RUN pip install  -r requirements.txt --upgrade pip

COPY .. /flask_login_tutorial

CMD python routes.py