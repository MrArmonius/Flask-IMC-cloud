from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from source.db import get_db

bp = Blueprint('index', __name__, url_prefix='/')

@bp.route('/', methods=['GET'])
def index():
    return render_template('index/index.html'), 201

@bp.route('/', methods=['POST'])
def index_post():
    weight = float(request.form['weight'])
    height = float(request.form['height'])
    imc = round(weight / (height*height), 2)
    print("Weight: ", weight, " type: ", type(weight), " | Height: ", height, " type: ", type(height), " | Imc: ", imc)
    data_test = [{
        'id': 1,
        'name': "Robert",
        'weight': "80",
        'height': "156",
        'imc': "25"
    },
    {
        'id': 2,
        'name': "Albert",
        'weight': "80",
        'height': "1742",
        'imc': "25"
    },
    {
        'id': 3,
        'name': "Albert",
        'weight': "80",
        'height': "1742",
        'imc': "25"
    }]
    return render_template('index/index.html', Imc=str(imc), Data_base=data_test), 201
