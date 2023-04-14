import urllib.request
from flask import Flask, jsonify, request
import json
from pyresparser import ResumeParser

application = Flask(__name__)
@application.route('/')

def index():
    resume = request.args.get('resume')
    resume = resume or "https://res.cloudinary.com/dhtgqzkse/image/upload/v1681132590/personal/Resume-AbdulBateen-Jolaoshoo_djmeh0.pdf"
    res = resume.split(".")
    ext = res[len(res) - 1]
    
    print([res, resume, ext])
    
    urllib.request.urlretrieve(resume, "resume." + ext )
    data = ResumeParser("resume."+ext).get_extracted_data()
    
    print(data)
    return jsonify(data)
application.run()
# 66586986647
