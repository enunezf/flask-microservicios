FROM python:3.6.1

# configura directorio de trabajo
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# agregar requirements
ADD ./requirements.txt /usr/src/app/requirements.txt

# install requirements
RUN pip install -r requirements.txt

# add app
ADD . /usr/src/app

# run server
CMD python manage.py runserver -h 0.0.0.0