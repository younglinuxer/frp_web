# coding=utf8
from jinja2 import Environment, FileSystemLoader
import json,re,os
import pymysql
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:yuan@127.0.0.1:3306/frp_web?charset=utf8mb4')
