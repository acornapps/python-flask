FROM python:3
ENV PYTHONUNBUFFERED 1
MAINTAINER acornsoft <apps@acornsoft.com>

WORKDIR /app

ADD    ./flaskapp /app
ADD    ./requirements.txt     /app/
RUN    pip install -r requirements.txt

ADD    ./start-dev.sh       /start-dev.sh

RUN chmod +x /*.sh

ENV MESSAGE "hello from Docker"

EXPOSE 5000

CMD ["/bin/sh","/start-dev.sh"]
