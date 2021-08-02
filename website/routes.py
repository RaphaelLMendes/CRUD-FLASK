from flask import Blueprint, render_template, request, redirect, url_for
from .models import Task
from . import db

routes = Blueprint('routes', __name__)


@routes.route("/")
def home():
    return render_template("home.html")


@routes.route("/list")
def list():
    list = Task.query.all()
    return render_template("list.html", list=list)


@routes.route("/new-task", methods=['GET', 'POST'])
def new_task():
    if request.method == 'POST':
        task = request.form.get('task')

        if len(task)==0:
            return redirect(url_for('routes.new_task'))
        else:
            new_task_add = Task(task=task)

            db.session.add(new_task_add)
            db.session.commit()
            return redirect(url_for('routes.list'))

    else:
        return render_template("new_task.html")


@routes.route("/edit-task/<id>", methods=["GET", "POST"])
def edit_task(id):
    current_task = Task.query.filter_by(id=id).first()

    if request.method == 'POST':
        new_task = request.form.get('task')
        if len(new_task) == 0:
            return redirect(url_for('routes.edit_task', id=id))
        else:
            current_task.task = new_task
            db.session.commit()
            return redirect(url_for('routes.list'))

    else:
        return render_template("new_task.html", current_task=current_task)


@routes.route("/delete-task/<id>", methods=["GET", "POST"])
def delete_task(id):
    current_task = Task.query.filter_by(id=id).first()
    db.session.delete(current_task)
    db.session.commit()
    return redirect(url_for('routes.list'))

