from flask import render_template, request
from app import app, db, models
import datetime

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    posts = [  # fake array of posts
        { 
            'author': {'nickname': 'John'}, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': {'nickname': 'Susan'}, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)

@app.route('/add_user')
def add_user():
	u = models.User(nickname='sbres', email='sbres@email.com')
	db.session.add(u)
	db.session.commit()
	return 'user added!'

@app.route('/add_post')
def add_post():
	u = models.User.query.get(3)
	p = models.Post(body='first post, bitch!', timestamp=datetime.datetime.utcnow(), author=u)
	db.session.add(p)
	db.session.commit()
	return "post added"

@app.route('/view_posts')
def view_posts():
	user = request.args.get('user')
	u = models.User.query.get(user)
	posts = u.posts.all()
	print "\n+++++++++++++++++++++++++\n", posts, "\n++++++++++++++++++++++++++\n"
	return "OK" 
