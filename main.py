#!/bin/python3

from flask import Flask, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes


@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mobile Webpage with Top and Bottom Bars</title>
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
            width: 100%;
            padding: 10px;
            border: none;
            border-radius: 5px;
            outline: none;
        }

        .checkbox-button {
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

        .checkbox-button.checked {
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
        <button class="checkbox-button" onclick="toggleCheckbox(this)">Rice</button>
        <button class="checkbox-button" onclick="toggleCheckbox(this)">Potatoes</button>
        <button class="checkbox-button" onclick="toggleCheckbox(this)">Pasta</button>
        <button class="checkbox-button" onclick="toggleCheckbox(this)">Bread</button>
        <button class="checkbox-button" onclick="toggleCheckbox(this)">Cheese</button>
        <button class="checkbox-button" onclick="toggleCheckbox(this)">Chicken</button>
        <button class="checkbox-button" onclick="toggleCheckbox(this)">Beef</button>
        <button class="checkbox-button" onclick="toggleCheckbox(this)">Fish</button>
        <button class="checkbox-button" onclick="toggleCheckbox(this)">Vegetables</button>
        <button class="checkbox-button" onclick="toggleCheckbox(this)">Fruits</button>
        <button class="checkbox-button" onclick="toggleCheckbox(this)">Salad</button>
        <button class="checkbox-button" onclick="toggleCheckbox(this)">Soup</button>
        <button class="checkbox-button" onclick="toggleCheckbox(this)">Eggs</button>
        <button class="checkbox-button" onclick="toggleCheckbox(this)">Milk</button>
        <button class="checkbox-button" onclick="toggleCheckbox(this)">Yogurt</button>
    </main>

    <div class="bottom-bar" onclick="alert('Proceeding to the next step')">
        <span>Set Values <i class="arrow"></i></span>
    </div>
</body>
</html>
"""
