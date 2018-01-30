from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "user"
    id= db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String)
    password = db.Column(db.String)
    def __init__(self,email,psw):
    	self.email=email
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

@app.route("/signup", methods= ["GET","POST"])
def signup():
	if request.method=="GET":
		return render_template('signup.html')
	else:
		email = request.form['email']
		psw = request.form['psw']
		x=User(email,psw)
		db.session.add(x)
		db.session.commit()
		return render_template('aftersignup.html')




if __name__ == '__main__':
	app.run()