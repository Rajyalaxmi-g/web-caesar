from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form="""
    <!DOCTYPE html>
    <html>
        <head>
            <style>
                form
                {{
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }}
                textarea{{
                    margin: 10px 0;
                    width:540px;
                    height: 120px;
                }}
            </style>
        </head>
        <body>
            <form action="/" method="post">
                <label for="rotate-by">
                    Rotate by:
                </label>
                <input type="text" id="rotate-by" value=0 name="rot">
                <br>
                <textarea name="text">{0}</textarea>
                <br>
                <input type="submit" >
            </form>
        </body>
    </html>
"""

@app.route("/")
def index():
    empty_str = ""
    return form.format(empty_str)

@app.route("/", methods=['POST'])
def encrypt():
    rotate = int(request.form['rot'])
    text = str(request.form['text'])
    rotatestring = rotate_string(text,rotate)
    rotatedstring = "<h1>" + rotatestring + "</h1>"
    return form.format(rotatestring)


app.run()
