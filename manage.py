from flask_wtf import CSRFProtect
from redis import StrictRedis
from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
# 开启csrf 保护
CSRFProtect(app)
# session保存配置
Session(app)

manager = Manager(app)
Migrate(app, db)  # 关联app ,db
manager.add_command('db', MigrateCommand)  # 迁移命令


@app.route('/index')
def index():
    session['name'] = 'haha'  # 添加值
    return 'index'


if __name__ == '__main__':
    manager.run()
