import logging
from quart import render_template, Blueprint, current_app, jsonify, json

mod_app = Blueprint('mirror', __name__)


@mod_app.route('/', methods=['GET'])
async def index():
    try:
        conn = current_app.sac

        with conn:
            with conn.cursor() as cursor:
                logging.info('Reading data from DB')
                sql = "SELECT *  FROM `company`"
                cursor.execute(sql)
                result = cursor.fetchall()
                logging.info(f'Result from DB: {result}')
        url_data = result
        return await render_template("index.html", data=url_data)
    except Exception as error:
        logging.error(f'Error: {error}')


@mod_app.route('/add', methods=['POST'])
async def add_data():
    print('hahahahha')
