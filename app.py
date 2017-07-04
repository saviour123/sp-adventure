import os
from bottle import route, run, template, static_file

host = '127.0.0.1'
static_dir = os.path.join(os.path.dirname(__file__), "static")


@route('/static/<filename:path>')
def server_static(filename):
	return static_file(filename, root=static_dir)

@route('/')
def index():
    return template('base.tpl')


@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>', name=name)


run(host=host, port=8888, reloader=True, debug=True)
