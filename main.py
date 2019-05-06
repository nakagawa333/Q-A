# coding: UTF-8
import os
from flask import Flask,request,redirect,render_template,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


from forms import PostForm,AnswerForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

@app.route("/")
@app.route("/home")
def index():
  from models import Post
  posts = Post.query.all()

  return render_template("index.html",posts=posts)

@app.route("/post/new",methods=['GET','POST'])
def new_post():
  from models import Post
  form = PostForm()
  if request.method == "POST":
    post = Post(title=form.title.data,content=form.content.data)
    db.session.add(post)
    db.session.commit()
    return redirect("/home")
  return render_template("create_post.html",title="New Post",form=form,legend="Question")

@app.route("/post/<int:post_id>",methods=["GET","POST"])
def post(post_id):
  from models import Post
  from models import Answer
  form =  AnswerForm()
  post = Post.query.get_or_404(post_id)
  answers = Answer.query.filter(Answer.person_id==post_id).all()
  if request.method == "POST":
    answer = Answer(name=form.name.data,content=form.content.data,person_id=post_id)
    db.session.add(answer)
    db.session.commit()
  return render_template("post.html",post=post,answers=answers,form=form,legend="Answer")

@app.route("/answer",methods=["GET","POST"])
def answer():
  from models import Answer
  answers = Answer.query.all()
  return render_template("answer.html",answers=answers)

if __name__ == '__main__':
  app.run(debug=True,port='9000', host='0.0.0.0')

