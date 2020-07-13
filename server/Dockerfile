FROM python:3.6-slim as builder

MAINTAINER shankha.shuvro@hotmail.com
RUN apt-get update \
    && apt-get install -y \
    pkg-config python3-pip python3-dev python3-venv python3-setuptools libhunspell-dev libsm6 \
    libxext6 libxrender-dev libxrender1 libfontconfig1 \
     && rm -rf /var/lib/apt/lists/*
#FROM ubuntu:18.04
#MAINTAINER shankha.shuvro@hotmail.com
#RUN apt-get update -y \
#    && apt-get install -y\
#    pkg-config \
#    python3-setuptools \
#    python3-venv \
#    python3-dev \
#    gcc \
#    python3-pip \
#    && rm -rf /var/lib/apt/lists/*




RUN python3 -m venv /opt/venv
# use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
ARG REQS=base
RUN pip3 install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt

FROM python:3.6-slim
MAINTAINER shankha.shuvro@hotmail.com
COPY --from=builder /opt/venv /opt/venv

# use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"

RUN apt-get update \
    && apt-get install -y \
    pkg-config python3-pip python3-dev python3-venv python3-setuptools libhunspell-dev libsm6 \
    libxext6 libxrender-dev libxrender1 libfontconfig1 \
     && rm -rf /var/lib/apt/lists/*


COPY . /app
WORKDIR /app
ENV HOME /app

EXPOSE 8081

#CMD ["gunicorn", "--reload", "routes:api", "--workers=3", "--timeout", "10000", "-b :8081"]

#CMD ["sh", "run.sh"]