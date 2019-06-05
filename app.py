import os
import signal
from flask import Flask
from buzz import generator

app = Falsk(__name__)

signal.signal(signal.SIGINT, lambda s, f: os._exit(0))

@app.route("/")
def generate_buzz():
    page = "<html><body><h2>"
    page += generator.generate_buzz()
    page += "</h2></body></html>"

if __name__="__main__":
    app.run(host = '0.0.0.0', port = os.getenv('PORT')) #5000 by default