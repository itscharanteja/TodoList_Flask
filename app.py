import flask
from flask import render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default= datetime.utcnow)

    def __repr__(self):
        return f"<Task {self.id}>"
    
@app.route("/", methods=["GET", "POST"])
def index():
    if flask.request.method == "POST":
        todo_content = flask.request.form.get("content")
        if todo_content:
            new_todo = Todo(content=todo_content)
            db.session.add(new_todo)
            db.session.commit()
    todos = Todo.query.all()
    return render_template("index.html", todos=todos)

@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    todo = Todo.query.get_or_404(id)
    if flask.request.method == "POST":
        new_content = flask.request.form.get("content")
        if new_content:
            todo.content = new_content
            db.session.commit()
            return flask.redirect(flask.url_for("index"))
    return render_template("update.html", todo=todo)

@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return flask.redirect(flask.url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)