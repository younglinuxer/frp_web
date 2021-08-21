FROM python:3.8
MAINTAINER younglinuxer younglinuxer@gamil.com

COPY frp-web/ /frp-web

ADD frp-web/start.sh /bin/start
RUN chmod +x /bin/start
RUN chmod a+x /frp-web/bin/frpc
RUN pip install -r /frp-web/requirements.txt
CMD ["/bin/bash","-c","start"]
