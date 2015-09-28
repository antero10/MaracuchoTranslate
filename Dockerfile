FROM ubuntu

RUN apt-get -y update
RUN apt-get -y upgrade

RUN apt-get install -y tar \
                   git \
                   curl \
                   nano \
                   wget \
                   dialog \
                   net-tools

RUN apt-get install  -y python python-dev python-distribute python-pip  python-setuptools python-dev build-essential libmysqlclient-dev

RUN pip install tweepy

RUN pip install python-instagram

RUN pip install SQLAlchemy

RUN  pip install pyyaml

RUN pip install mysql-python

