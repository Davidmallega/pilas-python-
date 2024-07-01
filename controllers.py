from flask import Blueprint, render_template, request, redirect, url_for
from models import TaskManager

task_manager = TaskManager()

admin_bp = Blueprint('admin', __name__)
user_bp = Blueprint('user', __name__)

@admin_bp.route('/')
def admin_dashboard():
    users_tasks = {user: task_manager.get_user_tasks(user) for user in task_manager.users}
    return render_template('admin.html', users_tasks=users_tasks)

@admin_bp.route('/assign', methods=['POST'])
def assign_task():
    username = request.form['username']
    task_description = request.form['task_description']
    task_manager.assign_task(username, task_description)
    return redirect(url_for('admin.admin_dashboard'))

@admin_bp.route('/pop_task', methods=['POST'])
def pop_task():
    username = request.form['username']
    task_manager.pop_task(username)
    return redirect(url_for('admin.admin_dashboard'))

@admin_bp.route('/replace_task', methods=['POST'])
def replace_task():
    username = request.form['username']
    task_index = int(request.form['task_index'])
    new_description = request.form['new_description']
    task_manager.replace_task(username, task_index, new_description)
    return redirect(url_for('admin.admin_dashboard'))

@user_bp.route('/<username>')
def user_dashboard(username):
    tasks = task_manager.get_user_tasks(username)
    return render_template(f'{username}.html', tasks=tasks, username=username)

@user_bp.route('/<username>/complete', methods=['POST'])
def complete_task(username):
    task_index = int(request.form['task_index'])
    task_manager.complete_task(username, task_index)
    return redirect(url_for('user.user_dashboard', username=username))
