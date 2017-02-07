from flask import render_template, redirect

from app.main import main_blueprint as main


@main.app_errorhandler(404)
def not_logged_in(e):
    return render_template('error_404.html'), 404


@main.app_errorhandler(401)
def not_logged_in(e):
    return redirect('/login'), 401
