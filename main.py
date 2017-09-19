from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method="POST">
            <label for="rot">
                Rotate by:
            </label>
            <input id="rot" type="text" name="rot" />
            <textarea name="text">{0}</textarea>
            <input type='submit' value='Rotate!' />
        </form>
    </body>
</html>
"""
@app.route('/', methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    text = request.form['text']
    new_text = rotate_string(text, rot)
    return form.format(new_text)
@app.route("/")
def index():
    return form.format('')

app.run()