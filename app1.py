import httplib
import socket
import requests
from jinja2 import Template
from flask import Flask
from flask import request
# from flask import jsonify
app = Flask(__name__)

html = open('c.html').read()
template = Template(html)

# @app.route("/")
# def hello():
#     return "Hello World"

@app.route("/")
def ip():
    # conn = httplib.HTTPConnection("mock.kite.com")
    # res = conn.getresponse()
    # res.getheaders()
    #
    a=str(request.remote_addr)
    b=socket.gethostbyaddr(a)
    c='https://{0}'.format(str(b),)


    # return jsonify({'ip': request.remote_addr}), 200
    return template.render(name=str(request.get(c)))
    # return (template.render(name=str(request.remote_addr)))


if __name__ == "__main__":
    app.run()