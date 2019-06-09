from flask import session
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from info import create_app, db


app = create_app('developement')
manager = Manager(app)
Migrate(app, db)  # 关联app ,db
manager.add_command('db', MigrateCommand)  # 迁移命令


@app.route('/')
def index():
    session['name'] = 'haha'  # 添加值
    return 'index'


if __name__ == '__main__':
    manager.run()
