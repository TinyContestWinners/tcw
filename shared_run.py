# for running on the cpanel shared host system
# wsgi entry point: tcw:app

from tcw import create_app
from tcw.config import Development, Production

def app(environ, start_response):
    application = create_app(Production.PROJECT, Production)
    application.run()
