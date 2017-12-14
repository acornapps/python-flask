FROM python:3
ENV PYTHONUNBUFFERED 1
MAINTAINER acornsoft <skyikho@acornsoft.com>

WORKDIR /app

ADD    ./manage.py            /app/
ADD    ./requirements.txt     /app/
RUN    pip install -r requirements.txt

ADD    ./djangosample/        /app/djangosample/

ADD    ./start-dev.sh       /start-dev.sh


RUN chmod +x /*.sh

EXPOSE 8000

CMD ["/bin/sh","/start-dev.sh"]
