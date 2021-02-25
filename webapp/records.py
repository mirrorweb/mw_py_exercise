import logging


class Records(object):
    def __init__(self, connection):
        self.connection = connection

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
