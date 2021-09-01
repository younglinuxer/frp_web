#!/usr/bin/env python
# encoding: utf-8
from flask import Flask, render_template, request, flash,redirect,url_for
from base.frp_base import *
#



app = Flask(__name__)
app.secret_key = 'kjsensldfneapk'


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        app_name = request.form['app_name']
        local_ip = request.form['local_ip']
        local_port = request.form['local_port']
        remote_port = request.form['remote_port']
        compile_ip = re.compile(
            '^(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[1-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)$')

        if not compile_ip.match(local_ip):
            print('IP地址不合法')
            flash(u'IP地址不合法')
            return render_template('index.html')
        c = add_frp(app_name=app_name,local_ip=local_ip,local_port=local_port,remote_port=remote_port)
        flash(c)
        return redirect(url_for('index'))
    if request.method == 'GET':
        return render_template('index.html', jxjl=json.loads(get_frpc()),remarks=get_frpc_remarks())
        # return render_template('index.html')
    return render_template('index.html')

@app.route('/delete_fpc', methods=["POST"])
def delete_fpc():
    app_name = request.form['app_name']
    sql = 'DELETE FROM frp_config WHERE app_name="%s";' % app_name
    print("删除%s" % app_name)
    exec_sql(sql=sql)
    make_frp_config()
    return '更新完成'


# make_frp_config()
#
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081,debug=True)


