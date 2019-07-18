import httplib
from jinja2 import Template
from flask import Flask
from flask import request
# from flask import jsonify
app = Flask(__name__)

html = open('c.html').read()
template = Template(html)

@app.route("/")
def ip():

    head=str(request.headers)
    mas=head.split(';')

    return (template.render(name=str(request.remote_addr),name1=mas))


if __name__ == "__main__":
    # app.run()
    app.run(host='0.0.0.0', port=1456)