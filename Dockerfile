FROM ubuntu:18.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt upgrade -y && apt install -y python3 mpc mpd
COPY bin/python-alarm.py /root/python-alarm.py
RUN chmod +x /root/python-alarm.py

CMD ["/root/python-alarm.py"]