from flask import Blueprint

#创建蓝图
index_blu = Blueprint('index', __name__)



from .index import views