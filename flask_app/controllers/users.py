from flask_app import app
from flask import Flask, render_template, redirect, request, session
from flask_app.models import user

# READ
@app.route('/')
def index():
    users = user.User.get_all()
    print(users)
    return render_template("index.html", all_users = users)

@app.route('/users/new')
def new_user():
    return render_template('create_user_form.html')

# CREATE
@app.route('/create_user', methods=["POST"])
def create_user():
    user.User.save(request.form)
    return redirect('/')

#show one user route page
@app.route('/users/<int:user_id>')
def show_one_user(user_id):
    user1 = user.User.show_one_user(user_id)
    return render_template('one_user.html', user=user1)


#edit user route page
@app.route('/users/<int:user_id>/edit')
def edit_one_user(user_id):
    user1 = user.User.show_one_user(user_id)
    return render_template('edit_user.html', user=user1)

#edit user database route
@app.route('/users/edit', methods=["POST"])
def update_user():
    user.User.update(request.form)
    return redirect('/')

#delete user database route
@app.route('/delete/<int:user_id>')
def delete_user(user_id):
    user.User.delete(user_id)
    return redirect('/')
