FROM ubuntu:18.04
LABEL MAINTAINER = "Ashish Kumar Ashish@Ashishkumar.org"
LABEL Version = "1.0"


RUN apt-get update -y && \
    apt-get install -y python-pip python-dev python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]
