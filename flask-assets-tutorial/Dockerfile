FROM python:3.9

EXPOSE 5007

WORKDIR /flask-assets-tutorial

COPY requirements.txt /flask-assets-tutorial
RUN pip install  -r requirements.txt --upgrade pip

COPY . /flask-assets-tutorial

CMD python app.py