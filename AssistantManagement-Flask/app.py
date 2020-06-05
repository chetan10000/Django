from flask import Flask,render_template,redirect,url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify,request
import requests
import json
from flask_migrate import Migrate
import re
import uuid
import os 
UPLOAD_FOLDER = 'C:\\Users\\chetan\\Desktop'
app = Flask(__name__)
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///C:/Users/chetan/Desktop/Assistant.db'
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
db = SQLAlchemy(app)
migrate = Migrate(app,db)

class Assistant(db.Model):
    _tablename_ = 'assistant'
    id = db.Column(db.Integer ,primary_key=True)
    name = db.Column(db.String(20),nullable=False)
    image = db.Column(db.LargeBinary)
    job_id = db.Column(db.Integer,db.ForeignKey('job.id'))
    job = db.relationship('Job',backref=db.backref('assistant',lazy=True))
    
    def __repr__(self):
        return '<Assistant %r>' % self.name

class Job(db.Model):
    __tablename__='job'
    id = db.Column('id', db.Text(length=36), default=lambda: str(uuid.uuid4()), primary_key=True)
    name = db.Column(db.String(30))
    category_id = db.Column(db.Integer,db.ForeignKey('category.id'))
    category = db.relationship('Category',backref=db.backref('job',lazy=True))

class Category(db.Model):
    __tablename__='category'
    id = db.Column('id', db.Text(length=36), default=lambda: str(uuid.uuid4()), primary_key=True)
    name = db.Column(db.String(30))




@app.route('/assistants',methods=['GET','POST'])
def get_assistant():
    if request.method=='GET':
        return jsonify({'message':'work under progress'})
    else:
        assistant_name =request.form.get('name')
        job_name = request.form['job']
        image = request.files.get('inputImage','')
        file_name = image.filename or '  '
        image.save(app.config['UPLOAD_FOLDER'],file_name)
        category_pro = re.findall(r'\w+(?:\?|\.|er|or|ist|st|man\b)',job_name[3:])
        print(assistant_name,job_name,category_pro)
        print(type(assistant_name))
        print(type(job_name))
        print(type(category_pro[0]))
        category =Category(name=category_pro[0])
        job_detail = Job(name=job_name,category=category)
        assistant= Assistant(name=assistant_name,job=job_detail,image=image)
        db.session.add(assistant)
        db.session.commit()
        return jsonify({'message':'success'})
        

        
        


@app.route('/assistants/create')
def hello_world():
    res = requests.get('http://api.dataatwork.org/v1/jobs')
    json_res = res.json()
    print(json_res)

    return render_template('jobs.html',jobs=json_res)


    


if __name__ == '__main__':
    app.run()
