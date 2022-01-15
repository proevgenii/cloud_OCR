from flask import Flask
from flask import request, render_template
from werkzeug.utils import secure_filename
import os
import pytesseract
from PIL import Image

#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = r'static/'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submitImage/', methods=['POST', ])
def submitImage():
    image = request.files['ocrImage']
    filename = secure_filename(image.filename)
    image.save(app.config['UPLOAD_FOLDER']+filename)
    img = Image.open(app.config['UPLOAD_FOLDER']+filename)
    text = pytesseract.image_to_string(img)
    f = open(os.path.join(app.config['UPLOAD_FOLDER'], filename) + '.txt', 'w')
    f.write(text)
    f.close()
    return render_template('exm.html', text=text, filename=f)


if __name__ == '__main__':
    app.run('0.0.0.0', 8000)
