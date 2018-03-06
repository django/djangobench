ARG IMAGE=conda/miniconda2
FROM ${IMAGE} as build

RUN apt-get -qq update && apt-get -qq -y install git \
    && apt-get -qq -y autoremove \
    && apt-get autoclean \
    && rm -rf /var/lib/apt/lists/* /var/log/dpkg.log \
    && useradd -ms /bin/bash djangobench

USER djangobench

ARG TESTFORK=django
ARG TESTBRANCH=master
ARG TESTREPO=git://github.com/${TESTFORK}/django.git

RUN git clone -b ${TESTBRANCH} ${TESTREPO} /home/djangobench/django
WORKDIR /home/djangobench/django

USER root
RUN conda install -y -c anaconda pytz

COPY . /src
RUN pip install /src
USER djangobench

ENTRYPOINT ["djangobench"]
