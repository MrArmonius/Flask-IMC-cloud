from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from source.db import get_db, execute_db, get_all_database

bp = Blueprint('index', __name__, url_prefix='/')

@bp.route('/', methods=['GET'])
def index():
    return render_template('index/index.html', Data_base=get_data_show()), 201

@bp.route('/', methods=['POST'])
def index_post():
    # Information we get from the form send by the user
    weight = float(request.form['weight'])
    height = float(request.form['height'])
    name = request.form['name']
    imc = round(weight / ((height/100.0)*(height/100.0)), 2)
    print("Weight: ", weight, " type: ", type(weight), " | Height: ", height, " type: ", type(height), " | Imc: ", imc)

    # Command to create value in the database
    command_string = "INSERT INTO `data_tp1` (`author`, `weight_id`, `height_id`, `imc_id`) VALUES ('{}', {}, {}, {});".format(name,weight, height, imc)
    print("Command executed:\n", command_string)

    # Execute command
    execute_db(command_string)

    # Get data from all the table
    data_show = get_data_show()
    return render_template('index/index.html', Imc=str(imc), Data_base=data_show), 201

def get_data_show():
    # Function to get all the values aand show it to the user
    datas = get_all_database()
    data_show = []
    for data in datas:
        data_row = {
            'id':data[0],
            'name': data[1],
            'weight': data[3],
            'height': data[4],
            'imc': data[5],
            'timestamp': data[2].strftime("%m/%d/%Y, %H:%M:%S")
        }
        data_show.append(data_row)
    return data_show
