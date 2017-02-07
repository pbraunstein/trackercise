from flask import render_template, redirect, url_for, flash

from app.main import main_blueprint as main


@main.app_errorhandler(404)
def error_404(e):
    return render_template('error_404.html'), 404


@main.app_errorhandler(401)
def not_logged_in(e):
    flash('Please login to see that page')
    return redirect(url_for('.login'))
