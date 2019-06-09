from redis import StrictRedis


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
