# -*- coding: utf-8 -*-
import logging
import json
import re

from quart import render_template, Blueprint, current_app, request, redirect, url_for
from webapp.records import Records

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
        logging.error(f'Exception: {error}')


@mod_app.route('/add')
async def read_data():
    try:
        logging.info('Loading json file')
        file = open('data/import_data.json', encoding="utf8")
        read_file = file.read()
        logging.info('Parsing')
        data = json.loads(read_file)
        for d in data:
            logging.info('Arrange data')
            name = d['name']
            safe_name = re.sub('[^A-Za-z0-9]+', '', name).lower()

            address = ' '.join(filter(None, [d['street'], d['city'], d['country'], d['post_code']]))
            telephone = d.get('telephone', 0).replace(" ", "")
            enterprise = d.get('enterprise', False)
            active = d.get('active', False)

            logging.info('Database Connection...')
            conn = current_app.sac

            with conn.cursor() as cursor:
                sql = "INSERT INTO company (name, safe_name, address, telephone, enterprise, active) VALUES (%s, %s, %s, %s, %s, %s)"
                val = (name, safe_name, address, int(telephone), int(enterprise), int(active))
                logging.info('Company insert started...')
                cursor.execute(sql, val)
                logging.info('Company insert completed...')
                company_id = conn.insert_id()
                logging.info('Arranging data of employees')
                for e in d['staff']:
                    username = e['username']
                    email = e['email']
                    first_name = e['first_name']
                    last_name = e['last_name']
                    address = ' '.join(filter(None, [e['street'], e['city'], e['country'], e['post_code']]))
                    department = e['department']
                    job = e['job']
                    sql_emp = "INSERT INTO employee (username, email, firstname, lastname, address, department, job, company_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                    val_emp = (username, email, first_name, last_name, address, department, job, company_id)
                    logging.info('Employees insert started...')
                    cursor.execute(sql_emp, val_emp)
                    logging.info('Employees insert completed...')
            logging.info('Committing...')
            conn.commit()
            conn.close()

        return await render_template("index.html")

    except Exception as error:
        logging.error(f'Exception: {error}')


@mod_app.route('/company/<int:company_id>/details', methods=['GET'])
async def company(company_id):
    try:
        conn = current_app.sac
        company_data = Records(connection=conn).get_company(company_id=company_id)
        employees_data = Records(connection=conn).get_employees(company_id=company_id)

        return await render_template("company.html", company_data=company_data, employees_data=employees_data)
    except Exception as error:
        logging.error(f'Exception: {error}')


@mod_app.route('/company/<int:company_id>/update', methods=['POST'])
async def update_company(company_id):
    try:
        conn = current_app.sac
        form =await request.form
        name = form.get('name')
        safe_name = re.sub('[^A-Za-z0-9]+', '', name).lower()
        address = form.get('address')
        telephone = form.get('telephone')
        Records(connection=conn).update_company(company_id, name, safe_name, address, telephone)
        conn.commit()
        return redirect(url_for('mirror.company', company_id=company_id))


    except Exception as error:
        logging.error(f'Exception: {error}')

@mod_app.route('/company/employees/<int:company_id>', methods=['GET'])
async def employees(company_id):
    try:
        conn = current_app.sac
        with conn.cursor() as cursor:
            logging.info('Reading employees data from DB')
            sql = f"SELECT *  FROM `employee` Where id= {company_id}"
            cursor.execute(sql)
            result = cursor.fetchall()
        return result
    except Exception as error:
        logging.error(f'Exception: {error}')
