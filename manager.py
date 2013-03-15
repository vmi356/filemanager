# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template
from filesystem import Folder

app = Flask(__name__)
app.config.update(
    DEBUG=False,
    FILES_ROOT=os.path.dirname(os.path.abspath(__file__)),
)

@app.route('/')
@app.route('/files/<path:path>')
def index(path=''):
    path_join = os.path.join(app.config['FILES_ROOT'], path)
    if os.path.isdir(path_join):
        folder = Folder(app.config['FILES_ROOT'], path)
        folder.read()
        return render_template('folder.html', folder=folder)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run()
