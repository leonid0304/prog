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
    c='http://{0}/'.format(str(b[0]),)

    # return jsonify({'ip': request.remote_addr}), 200
    # return str(b[0])

    d=request.get(c)
    return (template.render(name=d.text))

    # return template.render(name=str(request.get(c)))
    # return (template.render(name=str(request.remote_addr)))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4568)
