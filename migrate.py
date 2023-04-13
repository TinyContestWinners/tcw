import os
import subprocess

modules = [
    'tcw',
    'tcw-tasks'
]

subprocess.run(["pip", "install"] + modules)
