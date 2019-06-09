from flask import session
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from info import app, db

manager = Manager(app)
Migrate(app, db)  # 关联app ,db
manager.add_command('db', MigrateCommand)  # 迁移命令


@app.route('/index')
def index():
    session['name'] = 'haha'  # 添加值
    return 'index'


if __name__ == '__main__':
    manager.run()
