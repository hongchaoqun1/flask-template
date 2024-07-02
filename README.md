# Flask Web Project Scaffold

## 简介

这是一个基于Flask框架的简单Web项目脚手架，支持蓝图(Blueprints)组织视图函数，集成了Flask-SQLAlchemy扩展以方便数据库操作，并能以JSON格式返回数据。

## 功能特点

- **蓝图支持**：使用蓝图组织和注册视图函数，提高项目的模块化。
- **数据库集成**：通过Flask-SQLAlchemy简化数据库模型的创建和管理。
- **JSON数据返回**：支持以JSON格式返回数据，方便前后端分离开发。
- **定时任务**：支持flask_apscheduler 定时任务

## 环境要求

- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flask-Migrate（可选，用于数据库迁移）

## 安装指南

1. 克隆项目到本地环境：
   ```bash
   git clone https://gitee.com/hongchaoqun/flask-template.git
   ```
2. 进入项目目录：

3. 创建虚拟环境（推荐）：
   ```
   python -m venv venv
   ```

激活虚拟环境：
Windows:
   ```
   venv\Scripts\activate
   ```
Unix or MacOS:
   ```
   source venv/bin/activate
   ```

安装依赖：
   ```
      pip install -r requirements.txt
   ```

## 运行项目
启动应用：
python app.py

访问 http://127.0.0.1:5000/ 来查看应用。
