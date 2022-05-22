import os
import secrets
from PIL import Image
from flask import url_for, current_app, flash
from flask_mail import Message
from flaskblog import mail


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)#8bytes
    f_name , f_ext = os.path.splitext(form_picture.filename)
    #form_picture is the data from the field that the user submitted
    #and it will have a filename attribute
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics' , picture_fn)

    output_size = (125,125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)


    #form_picture.save(picture_path) #so instead of form_picture we save i
    i.save(picture_path)
    return picture_fn

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request' , sender = 'stevdevsone@gmail.com',
                    recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}
If you did not make this request then simply ignore this email
and no changes will be made.'''
    try:
        mail.send(msg)
        flash("An email has been sent with instructions to reset your password.", "info")
    except:
        flash("Error occured!", "warning")
