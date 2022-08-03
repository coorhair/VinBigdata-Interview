FROM python:3.10-alpine3.16
LABEL MAINTAINER="Rega Ng <manhtu.htk@gmail.com>"
# RUN apt-get update -y
# RUN apt-get install -y python3-pip
RUN pip3 install --upgrade pip
# install requirement packages
COPY ./requirements.txt /var/www/requirements.txt
RUN pip3 install -r /var/www/requirements.txt
# copy virtual environment settings
COPY . /var/www
WORKDIR /var/www
RUN pip3 install gunicorn
EXPOSE 5001
# CMD [ "gunicorn", "-w", "4", "--bind", "0.0.0.0:5001", "flaskr:create_app()"]
CMD ["flask", "--app", "flaskr", "--debug", "run", "--port", "5001", "--host", "0.0.0.0"]
