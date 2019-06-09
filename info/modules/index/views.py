from info import  redis_store
from info.modules import index_blu


@index_blu.route('/')
def index():
    # session['name'] = 'haha'  # 添加值
    # logging.debug('测试')
    # current_app.logger.error('错误')
    redis_store.set('name', 'itcast')
    return 'index'
