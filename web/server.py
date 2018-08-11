import os
from flask import Flask, request, render_template
import werkzeug
from run_script import run_script


app = Flask(__name__)

import os
global scripts_path
scripts_path = os.environ.get('SCRIPTS_PATH', os.path.dirname(os.path.realpath(__file__))) + "/scripts/"


@app.route("/")
def index():
    return render_template('index.html', message="Hey!")

@app.route("/update", methods=["POST"])
def update_script():
    active_script = scripts_path + request.form['script']
    with open('store.json', 'r+') as f:
        data = json.load(f)
        data['script_to_run'] = active_script
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()

    

@app.route("/upload", methods=["GET", "POST"])
def upload_new_script():
    pass
#    UPLOAD_FOLDER = '../scripts'
#    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 
#    if request.method == 'POST':
#        if file:
#                script = werkzeug.datastructures.FileStorage(stream=file,
#                        filename=file.name)
#                filename = file.name
#                script.save(os.path.join(UPLOAD_FOLDER, filename))
#                return filename

@app.route("/run", methods=["POST"])
def execute_script():
    return str(run_script())


if __name__ == "__main__":
   
    app.run(debug=True)
