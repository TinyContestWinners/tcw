from tcw.application import create_app
from tcw.config import Development, Production

"""
Run the test development website
"""

app = create_app(Development.PROJECT, Development)

if __name__ == '__main__':
    app.run()
