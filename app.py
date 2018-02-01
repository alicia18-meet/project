from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/desi.db'
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "user"
    id= db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    psw = db.Column(db.String)
    def __init__(self,name,psw):
    	self.name=name
    	self.psw=psw

db.create_all()


@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html')

@app.route("/projects")
def projects():
	return render_template('projects.html')

@app.route("/galleries")
def galleries():
	return render_template('galleries.html')

@app.route("/staff")
def staff():
	return render_template('staff.html')

@app.route("/terms")
def terms():
	return render_template('terms.html')

@app.route("/signuplogin")
def signuplogin():
	return render_template('signuplogin.html')

@app.route("/afternologin")
def afternologin():
	return render_template('afternologin.html')

@app.route("/signup", methods= ["GET","POST"])
def signup():
	if request.method=="GET":
		return render_template('signup.html')
	else:
		name = request.form['name']
		psw = request.form['psw']
		x=User(name=name,psw=psw)
		db.session.add(x)
		db.session.commit()
		return render_template('aftersignup.html')

@app.route("/login", methods= ["GET","POST"])
def login():
	if request.method=="POST":
		user = User.query.filter_by(name=request.form['name']).first()
		if user==None:
			return render_template('afternologin.html')
		else:
			return render_template('home.html', xx=user)
	else:
		return render_template('login.html')







if __name__ == '__main__':
	app.run()