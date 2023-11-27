FROM protik77/python3-sensehat:latest
RUN curl  'https://bootstrap.pypa.io/pip/3.4/get-pip.py' -o get-pip.py && python3 get-pip.py && pip install datadog
WORKDIR /home
COPY sensehat_weather_.py /home
CMD ["python3", "./sensehat_weather_.py"]
