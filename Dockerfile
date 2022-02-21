
FROM python:3.8-slim

# FROM ubuntu:20.04

LABEL MAINTAINER="Dennis Wanyonyi"

ENV LNM_SERVICE_DEBUG=FALSE

# To add these two to secrets on k8s
ENV C2B_CONSUMER_KEY="J4UIXDNoRAr1DRLg4gDqAycnW9dTreuM"
ENV C2B_CONSUMER_SECRET="2V07vlD0MSSkiGXz"

WORKDIR  /app

COPY . .

RUN apt update && apt -y upgrade

# RUN apt install -y python3-pip

RUN python -m pip install --upgrade pip 

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "lnm_service/manage.py", "runserver"]