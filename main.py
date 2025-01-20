#!/bin/python3

from flask import Flask, session, request
from service.htmlcontainer import HtmlContainer

# from flask_cors import CORS
# import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'oh_so_secret'
# CORS(app)  # This will enable CORS for all routes

htmlcontainer = HtmlContainer()


@app.route("/")
def home():
    session['itemlist'] = []
    page = (
        htmlcontainer.header() +
        htmlcontainer.top_bar() +
        htmlcontainer.meal_picker() +
        htmlcontainer.bottom_bar()
    )
    return page


@app.route("/values", methods=['POST'])
def hello():
    item = request.form.getlist('item')
    session['itemlist'].append(item)
    session.modified = True
    stored_value = session['itemlist']
    return f"""
        {htmlcontainer.top_bar()}
        {htmlcontainer.meal_picker()}
        {item} added to {stored_value}
        {htmlcontainer.bottom_bar()}
    """
