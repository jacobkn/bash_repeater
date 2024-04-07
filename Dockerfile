FROM python:3.8
USER 0
RUN cat /etc/os-release
RUN python --version
RUN pip --version
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt && pip freeze



