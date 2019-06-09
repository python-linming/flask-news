from flask import session, current_app
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from info import create_app, db, logging

app = create_app('developement')
manager = Manager(app)
Migrate(app, db)  # 关联app ,db
manager.add_command('db', MigrateCommand)  # 迁移命令





if __name__ == '__main__':
    manager.run()
