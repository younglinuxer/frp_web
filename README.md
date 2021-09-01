### frp_web

```text
frp客服端动态配置
页面实现 对frp映射的新增删除 避免每次新增删除都需要对frpc.ini进行编辑的操作 
```

#### 运行方式
```bash
# 确保已经安装docker及docker-compose 
docker-compose up -d

# docker中已经运行frp客户端无需独立安装 如果需要特定版本 请使用-v 将frpc文件挂载到 /frp-web/bin/frpc
```

#### 大概原理
```bash
# frpc配置支持 动态加载 即可使用reload进行操作
admin_port = 7400
admin_user = admin
admin_pwd = admin

# 使用jinja2 生成对应模板 从数据库获取数据并生成对应的配置文件

[common]
server_addr = {{ SERVER_IP }}
server_port = {{ SERVER_PORT }}
admin_port = 7400
admin_user = admin
admin_pwd = admin

{% for FRPC in FRPC_LIST %}
[{{ FRPC.app_name }}]
type = tcp
local_ip = {{ FRPC.local_ip }}
local_port = {{ FRPC.local_port }}
remote_port = {{ FRPC.remote_port }}
{% endfor %}

# python实现接口 支持动态添加配置及删除
# 使用docker-compose内置网络进行配置数据库连接 所以数据库配置地址为 frp-web

```