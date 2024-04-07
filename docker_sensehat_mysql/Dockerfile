FROM arm64v8/ubuntu

WORKDIR /tmp

RUN apt-get update && apt-get install -y curl python3 librtimulib7 git libopenjp2-7 python3-distutils python3-apt build-essential sense-hat nano python3-pip
RUN pip install mysql-connector-python

ADD ./sensehat.py /home/

RUN rm -f /tmp/*.deb
RUN apt-get clean

WORKDIR /

ENTRYPOINT ["python3", "/home/sensehat.py"]
