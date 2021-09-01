import json

from config import *

def exec_sql(sql="SELECT * FROM frp_server;"):
    """直接执行sql 操作数据库"""
    return engine.execute(sql)



def make_frp_config():
    name = './frpc.ini'
    env = Environment(loader=FileSystemLoader("./"))
    template = env.get_template('./templates/frpc.ini.j2')
    frp_list = []
    for i in exec_sql(sql='SELECT server_ip,server_port FROM frp_server;'): server_ip, server_port = i[0], i[1]

    for frp in exec_sql(sql='SELECT `app_name`,`local_ip`,`local_port`,`remote_port` FROM frp_config;'):
        app_name, local_ip,local_port, remote_port = frp[0],frp[1],frp[2],frp[3]
        frp_list.append({"app_name": app_name, "local_ip": local_ip, "local_port": local_port, "remote_port": remote_port})

    content = template.render(SERVER_IP=server_ip, SERVER_PORT=server_port, FRPC_LIST=frp_list)
    with open(name, 'w') as fp:fp.write(content)
    os.system('/frp-web/bin/frpc -c /frp-web/frpc.ini reload')


def get_frpc():
    frp_list = []
    for i in exec_sql(sql='SELECT server_ip FROM frp_server;'): server_ip = i[0]
    for frp in exec_sql(sql='SELECT `app_name`,`local_ip`,`local_port`,`remote_port` FROM frp_config;'):
        app_name, local_ip,local_port, remote_port = frp[0],frp[1],frp[2],frp[3]
        frp_list.append({"app_name": app_name, "local_ip": local_ip, "local_port": local_port, "remote_addr": server_ip + ':' + remote_port})
    # print(json.dumps(frp_list))
    return json.dumps(frp_list)

def get_frpc_remarks():
    for i in exec_sql(sql='SELECT remarks FROM frp_server;'): remarks = i[0]

    return remarks



def add_frp(app_name='xxx',local_ip='127.0.0.1',local_port='22',remote_port='6000'):
    sql1 = 'select * from frp_config where local_ip="%s" and local_port="%s";' % (local_ip,local_port)
    sql2 = 'select * from frp_config where app_name="%s" or remote_port="%s";' % (app_name,remote_port)
    sql3 = 'INSERT INTO `frp_web`.`frp_config` (`app_name`, `local_port`, `local_ip`, `remote_port`) VALUES ("%s","%s","%s","%s")' % (app_name, local_port,local_ip,remote_port)

    for s1 in exec_sql(sql=sql1):
        if len(s1)!=0:
            print('本地ip和端口重复')
            return '本地ip和端口重复'
    for s2 in exec_sql(sql=sql2):
        if len(s2)!=0:
            print('远程端口冲突 or 服务名重复')
            return '远程端口冲突 or 服务名重复'
    exec_sql(sql=sql3)
    make_frp_config()
    return '数据更新完成请稍后查看'



