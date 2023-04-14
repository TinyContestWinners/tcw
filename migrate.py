import os
import subprocess

modules = [
    'psycopg2-binary',
    'tcw',
    'tcw-tasks'
]

subprocess.run(["pip", "install"] + modules)
