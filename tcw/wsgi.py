# wsgi entry point

from tcw import create_app
from tcw.config import Development, Production

app = create_app(Production.PROJECT, Production)

if __name__ == '__main__':
    app.run()
