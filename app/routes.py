from flask import Flask, render_template, url_for, redirect, jsonify, request, Response
from app.Forms import *
from requests.auth import HTTPBasicAuth
import requests
from werkzeug.utils import secure_filename
import base64
import urllib.request, json
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('home.html', title = "home")

@app.route('/explore')
def explore():
    return render_template('explore.html', title = "explore")

@app.route('/login')
def login():
    return render_template('login.html', title = "login")

@app.route('/signup')
def signup():
    return render_template('signup.html', title = "signup")

@app.route('/contact')
def contact():
    return render_template('contact.html', title = "contact")

@app.route('/listing')
def listing():
    return render_template('listing-page.html', title = "listing")

@app.route('/get-listing-images')
def get_listing_images():
    response = json.loads(requests.get('https://demoepoce-apacaseanset01.cec.ocp.oraclecloud.com/content/management/api/v1.1/items', auth=('oic.user02', 'Oic12345####')).content)
    processed_response = response.get('items')
    for item in processed_response:
        print("hi")

    return processed_response


@app.route('/test')
def test():

    return requests.post('https://demoepoce-apacaseanset01.cec.ocp.oraclecloud.com/content/management/api/v1.1/items/_download', auth=('oic.user02', 'Oic12345####')).content




@app.route('/uploadFile', methods=['GET','POST'])
def uploadFile():
    form = APIForm()
    if form.validate_on_submit():
        
        filename = secure_filename(form.file.data.filename)
        scanning_file = request.files['file']
        form.file.data.save('uploads/' + filename)
        vision_api = "https://aseanoic-apacaseanset01-ia.integration.ocp.oraclecloud.com:443/ic/api/integration/v1/flows/rest/SCAN_API/1.0/image"
        username= open("C:\\Users\\prist\\Desktop\\Study\\ORACLE WORK\\Novaland Stuff\\username.txt","r").read()
        password= open("C:\\Users\\prist\\Desktop\\Study\\ORACLE WORK\\Novaland Stuff\\password.txt","r").read()
        with open('uploads/' + filename, "rb") as f:
            r= requests.request(url=vision_api, method='POST', data=f.read(),headers={'Content-Type': 'application/octet-stream', 'Data':'Binary'},auth=HTTPBasicAuth(username,password))
        print(r.text)
        return redirect(url_for('uploadFile'))
    else:
        print("invalid")
    
    return render_template('upload.html',form=form)

if __name__ == '__main__':
    app.run(debug=True)