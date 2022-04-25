from .utils import DbConnector, ContextManager, notification


class Budgets(DbConnector):
    '''Budget class for the application'''
    def create_db(self):
        connection = self.connector.connect(
            host=self.host, user=self.user, password=self.password, database=self.database)
        try:
            cursor = connection.cursor()
            return cursor, connection
        except Exception as e:
            print(f'\nDatabase Connection Error! {e}\n')

    def initialise_db(self, filename, cursor):
        '''initialise the database'''
        with ContextManager(filename, 'r') as sql_handler:
            cursor[0].execute(sql_handler.read(), multi=True)

    def check_rules(self, cursor):
        '''check the rules for the application'''
        check_expired = f'''
            SELECT * FROM t_budgets WHERE a_percent >= 50
            '''
        cursor[0].execute(check_expired)
        for row in cursor[0].fetchall():
            data = dict(a_shop_id=row[0],
                        a_budget_amount=row[2],
                        a_month=row[1],
                        a_amount_spent=row[3],
                        a_percent=row[4])
            notification(cursor, data)
            data = {}
