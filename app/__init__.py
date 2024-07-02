#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_apscheduler import APScheduler

# 延后加载
# 创建了数据库，此时数据库对象还没有跟app关联
db = SQLAlchemy()

scheduler = APScheduler()

def create_app(config_name):
    app = Flask(__name__)
    # 配置定时任务
    app.config['SCHEDULER_API_ENABLED'] = True  # 启用调度器 API


    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    config_class = config[config_name]
    app.config.from_object(config_class)

    app.config.from_envvar('CONFIG', silent=True)

    # 懒加载
    db.init_app(app)
    scheduler.init_app(app)

    return app
