class DbConnector:
    '''Database Connector for MySQL'''
    def __init__(self, connector, host, database, user, password):
        self.connector = connector
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def __enter__(self):
        with self.connector.connect(host=self.host, database=self.database, user=self.user, password=self.password) as self.connection:
            return self.connection

    def __exit__(self, exc_type, exc_value, exc_traceback):
        ''' this is to close the connection after database transaction'''
        self.connection.close()


class ContextManager:
    '''Context Manager for file handling'''
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()


def notification(cursor, data):
    '''Notification for expired budget'''
    notify = f'''
        Dear Customer, your shop with ID {data['a_shop_id']},
        has exceeded the budget of ${data['a_budget_amount']} for {data['a_month']}
        by {data['a_percent']}%  haven spent ${data['a_amount_spent']}% of your total budget for the month.
        '''
    notify_ofline = notify + \
        ('''your shop is now offline, please renew your subscription. Thank you.''')
    a_shop_id = data['a_shop_id']
    if float(data['a_percent']) >= 100:
        set_offline = f'UPDATE t_shops SET a_online ={0} WHERE a_id = {a_shop_id};'
        cursor[0].execute(set_offline)
        print(notify_ofline)
    else:
        print(notify)
