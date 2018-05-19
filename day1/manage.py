# 初始化，__name__代表主模块名或者包
#1
from flask_script import Manager
#3
from App import create_app

blue = create_app()

# 第三种启动方式
manager = Manager(app=blue)


if __name__ == '__main__':
    # 启动项目
    # 方法二启动
    # import sys
    # args = sys.argv
    # app.run(debug=True, port=args[1],host=args[2])
    # 方法一启动
    # app.run(debug=True,port='8000', host='127.0.0.1')

    # 方法3启动
    manager.run()
