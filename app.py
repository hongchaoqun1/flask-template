from app import create_app
from app import scheduler


# 使用装饰器定义定时任务
@scheduler.task('interval', id='my_job', seconds=5)
def my_task():
    print('定时任务执行了！')


if __name__ == '__main__':
    web = create_app("development")
    scheduler.start()
    web.run(debug=True)
