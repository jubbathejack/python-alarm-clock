FROM ubuntu:18.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get upgrade -y && apt-get install -y python3 mplayer
COPY bin/python-alarm.py /root/python-alarm.py
RUN chmod +x /root/python-alarm.py

CMD ["/root/python-alarm.py"]