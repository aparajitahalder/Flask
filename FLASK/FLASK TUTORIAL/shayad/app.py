from flask_sqlalchemy import SQLAlchemy     # 1. Import sqlAlchemy
from flask import Flask, render_template, request, redirect
from datetime import datetime
from jinja2 import Template

app = Flask(__name__) 


# 2. initialize sqlachemy
# Copy paste the sqlite database command from documentaion.

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///courses.db'  


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# A warning will arrive without this. Either make it true or false, but don't leave it.


db=SQLAlchemy(app)
# 3. Calling the sqlAlchemy nd checking if it works.


# 4. defining schema of database using class
class courses(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    title = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"       #Things that we want to view
   



    
    
@app.route("/", methods=['GET','POST'])
def home():
    if request.method=='POST':
        title=request.form['title']
        content=request.form['content'] 
        c=courses(content = content, title = title)
        db.session.add(c)
        db.session.commit()
    show=courses.query.all()
    return render_template('index.html', show=show)



@app.route("/show")
def show():
    show_all=courses.query.all()
    print(show_all)
    return render_template('index.html')





@app.route("/update/<int:sno>",methods=['GET','POST'])
def update(sno):
    if request.method=='POST':
        title=request.form['title']
        content=request.form['content'] 
        up=courses.query.filter_by(sno=sno).first()
        up.title=title
        up.content=content
        db.session.add(up)
        db.session.commit()
        return redirect("/")

    up=courses.query.filter_by(sno=sno).first()
        
    #rint(show_all)
    return render_template('update.html',up=up)




@app.route("/delete/<int:sno>")
def delete(sno):
    d=courses.query.filter_by(sno=sno).first()
    db.session.delete(d)
    db.session.commit()
    return redirect('/')



if __name__=="__main__":
    app.run()

    