import logging


class Records(object):
    def __init__(self, connection):
        self.connection = connection

    def get_company(self, company_id):
        try:
            with self.connection.cursor() as cursor:
                logging.info('Reading company data from DB')
                sql = f"SELECT *  FROM company Where id= {company_id}"
                cursor.execute(sql)
                return cursor.fetchone()
        except Exception as error:
            logging.error(f'Exception: {error}')

    def update_company(self, company_id, name=None, safe_name=None, address=None, telephone=None):
        try:
            with self.connection.cursor() as cursor:

                sql = f"UPDATE company set name=%s, safe_name=%s, address=%s, telephone=%s where id=%s"
                val = (name, safe_name, address, int(telephone), company_id)
                cursor.execute(sql, val)

        except Exception as error:
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
