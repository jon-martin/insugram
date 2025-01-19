#!/bin/python3

from flask import Flask, session, request

# from flask_cors import CORS
# import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'oh_so_secret'

# CORS(app)  # This will enable CORS for all routes
# app.items = ''

# Attempts at getting session working on other than localhost
# Set cookie settings to ensure it's valid for network access
app.config.update(
    SESSION_COOKIE_DOMAIN='192.168.1.137',  # Replace with your IP or domain
    SESSION_COOKIE_SECURE=False,  # Set to True if using HTTPS
)
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'


@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mobile Webpage with Top and Bottom Bars</title>
    <script src="https://unpkg.com/htmx.org@1.9.12"></script>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            background-color: #f5f5f5;
        }

        main {
            padding: 20px;
          /*  min-height: calc(100vh - 120px); */
            margin-top: 60px;
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            justify-content: center;
        }

        .top-bar {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 60px;
            background-color: #0056b3;
            display: flex;
            align-items: center;
            padding: 0 15px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }

        .top-bar input[type="text"] {
            width: 86%;
            padding: 10px;
            border: none;
            border-radius: 5px;
            outline: none;
        }

        .button {
            padding: 6px 10px;
            text-align: center;
            border-radius: 5px;
            background-color: lightgrey;
            color: black;
            border: none;
            cursor: pointer;
            font-size: 18px;
            flex: none;
        }

        .button.checked {
            background-color: #007bff;
            color: white;
        }

        .bottom-bar {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 60px;
            background-color: #0056b3;
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            cursor: pointer;
        }

        .bottom-bar:hover {
            background-color: #004494;
        }

        .bottom-bar span {
            display: flex;
            align-items: center;
            font-size: 16px;
        }

        .bottom-bar span .arrow {
            margin-left: 10px;
            border: solid white;
            border-width: 0 3px 3px 0;
            display: inline-block;
            padding: 5px;
            transform: rotate(-45deg);
            -webkit-transform: rotate(-45deg);
        }
    </style>
    <script>
        function toggleCheckbox(button) {
            button.classList.toggle('checked');
        }
    </script>
</head>
<body>
    <div class="top-bar">
        <input type="text" placeholder="Search...">
    </div>

    <main>
        <button class="button" hx-trigger="click" hx-get="/add_item" hx-target="#results" hx-vals='{"item": "Rice"}'>Rice</button>
        <button class="button" hx-trigger="click" hx-get="/add_item" hx-target="#results" hx-vals='{"item": "Potatoes"}'>Potatoes</button>
        <button class="button" hx-trigger="click" hx-get="/add_item" hx-target="#results" hx-vals='{"item": "Pasta"}'>Pasta</button>
        <button class="button" hx-trigger="click" hx-get="/add_item" hx-target="#results" hx-vals='{"item": "Bread"}'>Bread</button>
        <button class="button" hx-trigger="click" hx-get="/add_item" hx-target="#results" hx-vals='{"item": "Cheese"}'>Cheese</button>
        <button class="button" hx-trigger="click" hx-get="/add_item" hx-target="#results" hx-vals='{"item": "Chicken"}'>Chicken</button>
        <button class="button" hx-trigger="click" hx-get="/add_item" hx-target="#results" hx-vals='{"item": "Beef"}'>Beef</button>
        <button class="button" hx-trigger="click" hx-get="/add_item" hx-target="#results" hx-vals='{"item": "Fish"}'>Fish</button>
        <button class="button" hx-trigger="click" hx-get="/add_item" hx-target="#results" hx-vals='{"item": "Vegetables"}'>Vegetables</button>
        <button class="button" hx-trigger="click" hx-get="/add_item" hx-target="#results" hx-vals='{"item": "Fruits"}'>Fruits</button>
        <button class="button" hx-trigger="click" hx-get="/add_item" hx-target="#results" hx-vals='{"item": "Salad"}'>Salad</button>
        <button class="button" hx-trigger="click" hx-get="/add_item" hx-target="#results" hx-vals='{"item": "Soup"}'>Soup</button>
        <button class="button" hx-trigger="click" hx-get="/add_item" hx-target="#results" hx-vals='{"item": "Eggs"}'>Eggs</button>
        <button class="button" hx-trigger="click" hx-get="/add_item" hx-target="#results" hx-vals='{"item": "Milk"}'>Milk</button>
        <button class="button" hx-trigger="click" hx-get="/add_item" hx-target="#results" hx-vals='{"item": "Yogurt"}'>Yogurt</button>
    </main>

    <div id="results">
        <!-- The results will be loaded here -->
    </div>

    <div class="bottom-bar" onclick="alert('Proceeding to the next step')">
        <span>Set Values <i class="arrow"></i></span>
    </div>
</body>
</html>
"""


@app.route("/add_item", methods=['GET'])
def hello():
    item = request.args.get('item', '')
    if session['itemlist']:
        session['itemlist'] += item
    else:
        session['itemlist'] = item
    # app.items_selected += item
    # stored_value = 'test'
    stored_value = session['itemlist']
    return f"{item} added to {stored_value}"  # {app.items_selected}"
