
from flask_script import Manager

from utils import config
from utils.App import create_app

app = create_app()


manage = Manager(app)


if __name__ == '__main__':
    manage.run()