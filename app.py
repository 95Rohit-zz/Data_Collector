from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy
from send_email import send_email

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ddytpceyrcwwnj:462d4ba9587fc166359ae7799db5825394da0e2d7c55bb4d0461fb3fd4b1ff06@ec2-54-83-203-198.compute-1.amazonaws.com:5432/df6cg60ej56mc5?sslmode=require'
db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__="data"
    id=db.Column(db.Integer, primary_key=True)
    email_=db.Column(db.String(120), unique=True)
    height_=db.Column(db.Integer)

    def __init__(self,email_,height_):
        self.email_ = email_
        self.height_ = height_

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
    if request.method=='POST':
        email = request.form["email_name"]
        height = request.form["height_name"]
        send_email(email, height)
        if db.session.query(Data).filter(Data.email_==email).count() == 0:
            data=Data(email,height)
            db.session.add(data)
            db.session.commit()
            return render_template("success.html")
        return render_template("index.html", text = "oops same email again")

if __name__ == '__main__':
    app.debug =True
    app.run()



#postgresql://postgres:postgres123@localhost/height
