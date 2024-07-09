from flask import Flask, render_template, jsonify
import os
app = Flask(__name__)
def listdir_without_hidden(path):
    for file in os.listdir(path):
        if not file.startswith('.'):
            yield file


def back(file_path):
    parts = file_path.split('/')
    new_path = '/'.join(parts[:-1])
    return new_path

@app.route('/')
@app.route('/<path:path>')
def index(path=None):
    if path is None:
        path = '/'
    elif path =="/":
        pass
    else:
        path="/"+path
    print("1",path)
    previus=back(path)
    print("previus",previus)
    print("path",path)
    data = list(listdir_without_hidden(path))
    print(list(data))
    currentDirectory = os.path.abspath(path)
    
    return render_template('index.html', data_array=data, currentDirectory=path,previus=previus)


if __name__ == '__main__':
    app.run(debug=True)
