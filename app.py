from flask import Flask, render_template
import os
import datetime

IMAGE_RESOURCE = os.path.join('static', 'image')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = IMAGE_RESOURCE



@app.route('/')
def hello():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    logo = os.path.join(app.config['UPLOAD_FOLDER'], 'ku_wears_hoodie.jpeg')
    templateData = {
            'title' : 'Hello!',
            'time' : timeString,
            'logo' : logo
            }
    

    return render_template('home.html', **templateData)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)