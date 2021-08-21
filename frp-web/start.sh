#!/bin/bash
nohup /frp-web/bin/frpc -c  /frp-web/frpc.ini  > /frp-web/frpc.log 2>&1 &
cd /frp-web && python run.py