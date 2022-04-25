from utils.utils import ContextManager
from utils.app import Budgets
from decouple import config
import mysql.connector
import sys
arg = sys.argv


# create Buget instance and connect to database
create_instance = Budgets(mysql.connector,
                          config("HOST", default="", cast=str),
                          config("DATABASE", default="", cast=str),
                          config("DBUSER", default="", cast=str),
                          config("PASSWORD", default="", cast=str)
                          )

# create cursor
# os.system(f"mysql -u {create_instance.user} -p{create_instance.password} -h {create_instance.host} {create_instance.database} < {arg[1]}")

cursor = create_instance.create_db()

# execute assessment logic
create_instance.check_rules(cursor)
