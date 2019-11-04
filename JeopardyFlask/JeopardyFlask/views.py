"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from flask import request
from JeopardyFlask import app
import json
import requests
from json2html import *

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    params = {"count":100}
    data = requests.get('http://jservice.io/api/categories',params).json()
    categories = []
    for i in data:
        categories.append((i["id"],i["title"]))
    
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        category_list=categories
    )

@app.route('/handle_data', methods=['POST'])
def handle_data():
    t_api_url = 'http://jservice.io/api/clues'
    params = {"count":100}
    data = requests.get('http://jservice.io/api/categories',params).json()
    categories = []
    for i in data:
        categories.append((i["id"],i["title"]))
        

    params = {}
    t_category = request.form['category']
    selectedCategory = '0'
    if t_category != '0':
        params.update({"category":t_category})
        selectedCategory = t_category

    t_amount = request.form['amount']
    selectedAmount = '0'
    if t_amount != '0':
        params.update({"value":t_amount})
        selectedAmount = t_amount
    print(params)

    return render_template(
        'index.html',
        title='Got It',
        year=datetime.now().year,
        category_list=categories,
        trivia=json2html.convert(requests.get(t_api_url,params).json(),table_attributes='class=\"w3-table-all w3-small\"'))