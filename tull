#!/usr/bin/env python3
import sys
import os
from uuid import uuid4
from os.path import expanduser

from flask import Flask
from flask import request

home = expanduser("~")

LOG_PATH=home + "/.tull/"

if len(sys.argv) > 1 and sys.argv[1] == "server":
    app = Flask(__name__)

    @app.route('/tull/<tull_id>')
    def get_logs(tull_id):
        with open(LOG_PATH + tull_id) as f:
            return f.read()

    @app.route('/tull')
    def get_list():
        return "<br>".join([ "<a href=\"" + x + "\"/>" for x in os.listdir(LOG_PATH)])


    app.run()



sid = str(uuid4())
cnt = 0 
print("http://localhost:5000/" + sid)

try:
    if not os.path.isdir(LOG_PATH):
        os.mkdir(LOG_PATH)
except:
    raise Exception("Can't create the .tull folder")

try:
    with open(LOG_PATH + sid,"a+") as f:
        for line in sys.stdin:
            f.write(line)
            sys.stdout.write(line)
            cnt += 1
finally:
    if  cnt==0:
        os.remove(LOG_PATH + sid)

