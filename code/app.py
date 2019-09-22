from flask import Flask
import sys
from datetime import datetime
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "<h1>Hello,  GDG SF Members!!</br>The current time is : {}</br>Version  = 1.0.0</h1>".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
