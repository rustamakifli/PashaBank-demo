from extensions import db, login_manager,admin
from flask_login import UserMixin
from flask_admin.contrib.sqla import ModelView



class QueueNumber(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    queue = db.Column(db.Integer(),nullable=False)

    def __repr__(self):
        return f"{self.queue}"
    def __init__(self,queue):
        self.queue = queue
    
    def save(self):
        db.session.add(self)
        db.session.commit()  
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Slider(db.Model):
    id = db.Column(db.Integer(),primary_key=True)   
    image_url = db.Column(db.String(255),nullable = False)
    slider_top_pic = db.Column(db.String(255))
    slider_top_line = db.Column(db.String(255),nullable = True)
    slider_title = db.Column(db.String(255),nullable = True)
    slider_text = db.Column(db.String(255),nullable = True)

    def __repr__(self):
        return self.image_url
    def __init__(self,image_url,slider_top_pic,slider_top_line,slider_title,slider_text):
        self.image_url = image_url
        self.slider_top_line = slider_top_line
        self.slider_top_pic = slider_top_pic
        self.slider_title = slider_title
        self.slider_text = slider_text
    def save(self):
        db.session.add(self)
        db.session.commit() 

admin.add_view(ModelView(Slider,db.session))

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)      

class User(UserMixin, db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    name = db.Column(db.String(30),nullable=False)
    surname = db.Column(db.String(30),nullable=False)
    number = db.Column(db.Integer(),nullable=False)
    email = db.Column(db.String(30),nullable=False)
    date = db.Column(db.Date(),nullable=False)
    time = db.Column(db.DateTime(),nullable=False)
    is_active = db.Column(db.Boolean,nullable=False)
    is_superuser = db.Column(db.Boolean,nullable=False)

    def __init__(self, name, surname ,number ,email ,date ,time ,is_active=True ,is_superuser=False):
        self.name = name
        self.surname = surname
        self.number = number
        self.email = email
        self.date = date
        self.time = time
        self.is_active = is_active
        self.is_superuser = is_active
      
    def save(self): 
        db.session.add(self)
        db.session.commit()  


admin.add_view(ModelView(User,db.session))
admin.add_view(ModelView(QueueNumber,db.session))


