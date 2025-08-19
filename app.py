#to Run app.py
#1. activate enviroment -> .\env\Scripts\activate.ps1
#2. python .\app.py
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/hp/OneDrive/Desktop/Rohan/flask/todo.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class ToDo(db.Model):
    SNO = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable = False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"{self.SNO} - {self.title}"
@app.route('/' , methods=['GET', 'POST'])
def hello_world():
    if request.method=='POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = ToDo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()
    allTodo = ToDo.query.all()
    return render_template('index.html' , allTodo=allTodo)

@app.route('/show')
def products():
    allTodo = ToDo.query.all()
    print(allTodo)
    return 'this is products page'

@app.route('/update/<int:SNO>', methods=['GET', 'POST'])
def update(SNO):
    if request.method=='POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = ToDo.query.filter_by(SNO=SNO).first()
        todo.title = title
        todo.desc = desc
        db.session.add(todo)
        db.session.commit()
        return redirect("/")
    todo = ToDo.query.filter_by(SNO=SNO).first()
    return render_template('update.html' , todo=todo)


@app.route('/delete/<int:SNO>')
def delete(SNO):
    todo = ToDo.query.filter_by(SNO=SNO).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True , port=8000) # run in debug mode which show in brower , you can change port
#static folder serve file aztice
#render_template is used with return, used for render template file like html
#bootsrap has already written some website code platform