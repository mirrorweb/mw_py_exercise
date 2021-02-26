import logging


class Records(object):
    def __init__(self, connection):
        self.connection = connection

    def get_company_all(self):
        with self.connection.cursor() as cursor:
            logging.info('Reading data from DB')
            sql = "SELECT *  FROM company"
            cursor.execute(sql)
            result = cursor.fetchall()
            logging.info(f'Result from DB: {result}')
        return result

    def get_company(self, company_id):
        try:
            with self.connection.cursor() as cursor:
                logging.info('Reading company data from DB')
                sql = f"SELECT *  FROM company Where id= {company_id}"
                cursor.execute(sql)
                return cursor.fetchone()
        except Exception as error:
            logging.error(f'Exception: {error}')

    # def add_company(self, name, safe_name, address, telephone, enterprise, active, staff=None):
    #     with self.connection.cursor() as cursor:
    #         sql = "INSERT INTO company (name, safe_name, address, telephone, enterprise, active) VALUES (%s, %s, %s, %s, %s, %s)"
    #         val = (name, safe_name, address, int(telephone), int(enterprise), int(active))
    #         logging.info('Company insert started...')
    #         cursor.execute(sql, val)
    #         logging.info('Company insert completed...')
    #         company_id = self.connection.insert_id()
    #         if staff:
    #             for e in staff:
    #                 username = e['username']
    #                 email = e['email']
    #                 first_name = e['first_name']
    #                 last_name = e['last_name']
    #                 address = ' '.join(filter(None, [e['street'], e['city'], e['country'], e['post_code']]))
    #                 department = e['department']
    #                 job = e['job']
    #
    # def add_employee(self, company_id, username, email, first_name, last_name, address, department, job, connection= False):
    #     if connection:
    #         pass
    #     sql_emp = "INSERT INTO employee (username, email, firstname, lastname, address, department, job, company_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    #     val_emp = (username, email, first_name, last_name, address, department, job, company_id)
    #     logging.info('Employees insert started...')
    #     cursor.execute(sql_emp, val_emp)
    #     logging.info('Employees insert completed...')


    def update_company(self, company_id, name=None, safe_name=None, address=None, telephone=None):
        try:
            with self.connection.cursor() as cursor:

                sql = f"UPDATE company set name=%s, safe_name=%s, address=%s, telephone=%s where id=%s"
                val = (name, safe_name, address, int(telephone), company_id)
                cursor.execute(sql, val)

        except Exception as error:
            self.connection.rollback()
            logging.error(f'Exception: {error}')

    def get_employees(self, company_id):
        try:
            with self.connection.cursor() as cursor:
                logging.info('Reading employees data from DB')
                sql = f"SELECT *  FROM `employee` Where company_id= {company_id}"
                cursor.execute(sql)
                result = cursor.fetchall()
            return result
        except Exception as error:
            logging.error(f'Exception: {error}')
