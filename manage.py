from flask_wtf import CSRFProtect
from redis import StrictRedis
from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_script import Manager


class Config(object):
    """项目配置"""

    DEBUG = True
    SECRETY_KEY = 'sdfsfsdfds'
    # mysql
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost:3306/news'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # redis
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

    # session
    SESSION_TYPE = 'redis'
    # 指定session保存到redis
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    SESSION_USE_SIGNER = True  # 数字签名
    SESSION_PERMANENT = False  # 设置过期时间
    PERMANENT_SESSION_LIFETIME = 86400


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
# 开启csrf 保护
CSRFProtect(app)
# session保存配置
Session(app)

manager = Manager(app)


@app.route('/index')
def index():
    session['name'] = 'haha'  # 添加值
    return 'index'


if __name__ == '__main__':
    manager.run()
