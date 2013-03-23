# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template
from filesystem import Folder, File

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
        my_file = File(app.config['FILES_ROOT'], path)
        my_file.as_view()

if __name__ == '__main__':
    app.run()
