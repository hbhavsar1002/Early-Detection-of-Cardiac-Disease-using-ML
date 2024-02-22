from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
# import MySQL
from model_cal import model_cal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:post123@localhost/heart'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(20), unique=True)

    def __init__(self, username_, passwd_):
        self.username_ = username_
        self.passwd_ = passwd_


class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    age_ = db.Column(db.Integer)
    sex_ = db.Column(db.Integer)
    cp_ = db.Column(db.Integer)
    trestbps_ = db.Column(db.Integer)
    chol_ = db.Column(db.Integer)
    fbs_ = db.Column(db.Integer)
    restecg_ = db.Column(db.Integer)
    thalach_ = db.Column(db.Integer)
    exang_ = db.Column(db.Integer)
    oldpeakst_ = db.Column(db.Float)
    slope_ = db.Column(db.Integer)
    ca_ = db.Column(db.Integer)
    thal_ = db.Column(db.Integer)

    def __init__(self, age_, sex_, cp_, trestbps_, chol_, fbs_, restecg_, thalach_, exang_, oldpeakst_, slope_, ca_, thal_):
        self.age_ = age_
        self.sex_ = sex_
        self.cp_ = cp_
        self.trestbps_ = trestbps_
        self.chol_ = chol_
        self.fbs_ = fbs_
        self.restecg_ = restecg_
        self.thalach_ = thalach_
        self.exang_ = exang_
        self.oldpeakst_ = oldpeakst_
        self.slope_ = slope_
        self.ca_ = ca_
        self.thal_ = thal_


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/calc", methods=['POST'])
def calc():
    if request.method == 'POST':
        username = request.form["username"]
        passwd = request.form["password"]
        if (db.session.query(User).filter(User.username == username and User.password == passwd).count()) == 1:
            db.session.commit()
            return render_template("calc.html")
        else:
            return render_template("signin.html")
    return render_template("calc.html")


@app.route("/result", methods=['POST'])
def result():
    if request.method == 'POST':
        age = request.form["age"]
        sex = request.form["sex"]
        cp = request.form["cp"]
        trestbps = request.form["trestbps"]
        chol = request.form["chol"]
        fbs = request.form["fbs"]
        restecg = request.form["restecg"]
        thalach = request.form["thalach"]
        exang = request.form["exang"]
        oldpeakst = request.form["oldpeakst"]
        slope = request.form["slope"]
        ca = request.form["ca"]
        thal = request.form["thal"]
        predicted_result = model_cal(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeakst, slope, ca, thal)
        value = Data(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeakst, slope, ca, thal)
        db.session.add(value)
        db.session.commit()
        print(predicted_result[0])
        if(predicted_result[0] == 1):
            print(predicted_result[0])
            prediction = "You have heart disease"
        else:
            prediction = "You do not have heart disease"

        return render_template("result.html", predicted_result=prediction)


@app.route("/home")
def home():
    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000 )


'''
import mysql.connector
from mysql.connector import Error
try:
   mySQLconnection = mysql.connector.connect(host='localhost',
                             database='heart',
                             user='phpmyadmin',
                             password='php123')
   sql_select_Query = "select * from data where id = "
   cursor = mySQLconnection .cursor()
   cursor.execute(sql_select_Query)
   records = cursor.fetchall()
   prediction  = model_cal(records)
   cursor.close()

except Error as e :
    print ("Error while connecting to MySQL", e)
finally:
    # closing database connection.
    if(mySQLconnection .is_connected()):
        connection.close()
        print("MySQL connection is closed")
'''
