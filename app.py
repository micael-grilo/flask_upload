import os

from flask import (
    Flask,
    request,
    render_template,
    abort,
    send_from_directory
)
from werkzeug.exceptions import NotFound
from pathlib import Path


PORT = '5053'
UPLOAD_FOLDER = 'filestore'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)

upload_folder_path = Path(__file__).resolve().parent / UPLOAD_FOLDER
app.config['UPLOAD_FOLDER'] = str(upload_folder_path)
upload_folder_path.mkdir(exist_ok=True)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/',  methods=['GET', 'POST'])
def index():
    """
    """
    file_exists = False

    if request.method == 'GET':
        return render_template('index.html')
    else:
        _name = request.form.get('name')
        _file = request.files.get('file')
        _filename = f"{_name}.{_file.filename.split('.')[1]}"

        if _file and allowed_file(_filename):
            _path = os.path.join(app.config['UPLOAD_FOLDER'], _filename)
            if os.path.exists(_path):
                file_exists = True

            _file.save(_path)
            return render_template('index.html', done=True, name=_name, file_exists=file_exists)
        else:
            return render_template('index.html')


@app.route('/img/<filename>')
def uploaded_file(filename):
    """
        /img/<filename>
        Try to get image in the available extensions.
    """
    for extension in ALLOWED_EXTENSIONS:
        try:
            return send_from_directory(app.config['UPLOAD_FOLDER'], f"{filename}.{extension}")
        except NotFound:
            continue

    return abort(404)


@app.route('/image/<filename>')
def get_file(filename):
    """
        /image/<filename>
        Try to get image in the available extensions, and display it with a title.
    """
    for extension in ALLOWED_EXTENSIONS:
        _path = os.path.join(
            app.config['UPLOAD_FOLDER'],
            f"{filename}.{extension}"
        )
        if os.path.exists(_path):
            return render_template('image.html', filename=filename)

    return abort(404)


if __name__ == '__main__':
    app.run(port=PORT)
