import os
from flask import Flask, flash, render_template, request
# please note the import from `flask_uploads` - not `flask_reuploaded`!!
# this is done on purpose to stay compatible with `Flask-Uploads`
from flask_uploads import IMAGES, UploadSet, configure_uploads

app = Flask(__name__)
photos = UploadSet("photos", IMAGES)
app.config["UPLOADED_PHOTOS_DEST"] = "static/images"
app.config["SECRET_KEY"] = os.urandom(24)
configure_uploads(app, photos)


@app.route("/", methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file=request.files['photo']
        category="alumnos"
        pic=file.filename
        photo=pic.replace("'","")
        picture=photo.replace(" ","_")
        
        if picture.lower().endswith(('.png', '.jpg', '.jpeg')):
            save_photo = photos.save(file, folder=category)
            if save_photo:
                print(picture)
        flash("Photo saved successfully.")
        return render_template('index.html')
    return render_template('index.html')


if __name__=='__main__':
    app.run(debug=True)