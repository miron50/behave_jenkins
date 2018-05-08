import os
import subprocess


def before_scenario(context, scenario):
    context.server = subprocess.Popen('Python .\\features\\server.py')


def after_scenario(context, scenario):
    context.server.terminate()
    try:
        os.remove(context.PATH)
    except:
        pass