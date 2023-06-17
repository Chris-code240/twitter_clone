import os
SQLALCHEMY_DATABASE_URI = 'postgres://postgres:Liukangs240@localhost:5432/twitter'
# SQLALCHEMY_DATABASE_URI = "postgres://pasquo3:MyynLIScI5Qlr0unO4o9fmcBcu5hydwX@dpg-ci15nse7avjfjakvtqa0-a.oregon-postgres.render.com/pasquo3"

SQLALCHEMY_TRACK_MODIFICATIONS = True
os.environ['SECRETE_KEY'] = "plBbjQJl699AIc6w"
os.environ['TOKEN'] = ""
os.environ['MASTER_TOKEN'] = ""

ADMIN = False