from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)



class User(db.Model):
    __tablename__ = "User"
    id = db.Column(db.Integer,primary_key=True)
    firstname= db.Column(db.String(),nullable=False)
    lastname= db.Column(db.String(),nullable=False)
    email = db.Column(db.String(),unique=True)
    telephone = db.Column(db.String(),unique=True)
    followers = db.Column(db.String())
    following = db.Column(db.String())

    def __repr__(self) -> str:
        return f"<id: {self.id}, name: {self.firstname} >"
    
    def __init__(self,firstname,lastname,email,telephone,followers,following) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.email= email
        self.telephone = telephone
        self.followers = followers
        self.following = following
    
    def getUser(self):
        return {"id":self.id,"firstname":self.firstname,"lastname":self.lastname,"email":self.email,"telephone":self.telephone,"followers":self.followers,"following":self.following}
    
    def adduser(self):
        db.session.add(self)
        db.session.commit()
        

class Post(db.Model):
    __tablename__ = "Post"
    id = db.Column(db.Integer(),primary_key=True)
    user_id =  db.Column(db.Integer,db.ForeignKey('User.id'), nullable=False)
    text = db.Column(db.String(),nullable=False)
    time = db.Column(db.String(),nullable=False)
    public = db.Column(db.Boolean,default=True)

    def __init__(self,user_id,text,time,public) -> None:
        self.user_id = user_id
        self.text = text
        self.time = time
        self.public = public
    
    def addPost(self):
        db.session.add(self)
        db.session.commit()
    
    def getPost(self):
        return {"id":self.id,"user_id":self.user_id,"text":self.text,"time":self.time,"public":self.public}
    

class PostImages(db.Model):
    id = db.Column(db.Integer(),primary_key = True)
    post_id = db.Column(db.Integer,db.ForeignKey('Post.id'), nullable=False)
    filename = db.Column(db.String(),nullable=False)
    file = db.Column(db.LargeBinary,nullable=False)

    def __init__(self,post_id,filename,file) -> None:
        self.post_id = post_id
        self.filename = filename
        self.file = file
    
    def addImage(self):
        db.session.add(self)
        db.session.commit()
    
    def __repr__(self) -> str:
        return f"<id: {self.id}, post_id: {self.post_id}, filename: {self.filename} >"
    

# Work on retweets
    