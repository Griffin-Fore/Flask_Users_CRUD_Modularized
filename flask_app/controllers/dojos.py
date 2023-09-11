from flask_app import app
from flask import Flask, render_template, redirect, request, session
from flask_app.models import dojo, ninja

# READ
@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def new_user():
    dojos = dojo.Dojo.get_all_dojos()
    return render_template('index.html', dojos=dojos)

@app.route('/dojos/creation', methods=["POST"])
def create_dojo():
    dojo_id = dojo.Dojo.create_dojo(request.form)
    print("******************** Creating Dojo: ", dojo_id)
    return redirect(f'/dojos/{dojo_id}')

@app.route('/dojos/<int:dojo_id>')
def display_one_dojo(dojo_id):
    selected_dojo = dojo.Dojo.get_one_dojo_with_ninjas(dojo_id)
    return render_template('one_dojo.html', selected_dojo = selected_dojo)