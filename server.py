from flask import Flask, render_template, request
from flask_paginate import Pagination, get_page_parameter

from data import DATA

app = Flask(__name__)

@app.route('/')
def index():

    # Get the current page number from the query string
    page = request.args.get(get_page_parameter(), type=int, default=1)

    # Get a list of all items
    cryptos = DATA

    # Create a Pagination object
    pagination = Pagination(page=page, total=len(cryptos), per_page=10)

    # Get a sublist of items for the current page
    start_index = (page - 1) * pagination.per_page
    end_index = start_index + pagination.per_page
    items_on_page = cryptos[start_index:end_index]

    return render_template('index.html', pagination=pagination, cryptos=items_on_page)

if __name__ == '__main__':
    app.run(debug=True)