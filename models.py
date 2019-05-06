from datetime import datetime
from main import app,db


class Post(db.Model):
  id = db.Column(db.Integer,primary_key=True)
  title = db.Column(db.String(2000),nullable=False)
  date_posted = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
  content = db.Column(db.Text,nullable=False)
  addresses = db.relationship("Answer",backref="post",lazy=True)

  def __repr__(self):
    return "Post('{0}','{1}')".format(self.title,self.date_posted)

class Answer(db.Model):
  id = db.Column(db.Integer,primary_key=True)
  name = db.Column(db.String(100),nullable=False)
  date_posted = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
  content = db.Column(db.Text,nullable=False)
  person_id = db.Column(db.Integer,db.ForeignKey('post.id'),nullable=False)

  def __repr__(self):
    return "Answer('{0}','{1}')".format(self.name,self.date_posted)

