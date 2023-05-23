#!/usr/bin/python3
''' Fabric script that generates a .tgz archive from the contents of the web_static folder
    using the function do_pack
'''
from fabric.api import run, local, put
import datetime


def do_pack():
    '''generates a .tgz archive from the contents of the web_static folder'''
    now = datetime.datetime.now()
    date = (str(now.year) + str(now.month) + str(now.day) + str(now.hour) +
            str(now.minute) + str(now.second))
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz ./web_static".format(date))
        return "./versions/web_static_{}.tgz".format(date)
    except:
        return None
