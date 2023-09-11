from flask_app import app
from flask import Flask, render_template, redirect, request, session
from flask_app.models import dojo, ninja

@app.route('/ninjas')
def ninja_page():
    all_dojos = dojo.Dojo.get_all_dojos()
    return render_template('new_ninja_creation_page.html', all_dojos=all_dojos)

@app.route('/create/ninja', methods=["POST"])
def create_ninja():
    ninja_id = ninja.Ninja.create_ninja(request.form)
    print("******************** Creating ninja: ", ninja_id)
    dojo_id = request.form['dojo']
    return redirect(f'/dojos/{dojo_id}')