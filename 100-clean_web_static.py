#!/usr/bin/python3
''' script (based on the file 3-deploy_web_static.py) that deletes out-of-date archives,
    using the function do_clean
'''
from fabric.api import run, local, put, env
import datetime
import os


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


env.hosts = ['35.190.188.208', '35.227.47.184']


def do_deploy(archive_path):
    '''distributes an archive to your web servers'''
    if os.path.exists(archive_path) is False:
        return False
    try:
        upload = put(archive_path, "/tmp/")
        name = archive_path[11:-4]
        rmt_path = "/data/web_static/releases/" + name
        run("mkdir {}".format(rmt_path))
        run("tar -xvzf /tmp/{}.tgz --directory {}/".format(name, rmt_path))
        run("rm /tmp/{}.tgz".format(name))
        run("rm /data/web_static/current")
        run("ln -nsf /data/web_static/releases/{} /data/web_static/current"
            .format(name))
        run("mv {}/web_static/* {}".format(rmt_path, rmt_path))
        run("rm -d {}/web_static/".format(rmt_path))
        return True
    except:
        return False


def deploy():
    '''creates and distributes an archive to your web servers'''
    path = do_pack()
    print("este es el path: ", path)
    if path is None:
        return False
    return do_deploy(path)


def do_clean(number=0):
    '''deletes out-of-date archives'''
    num_files = local("ls -1t versions/ | wc -l", capture=True)
    if number == "0":
        number = "1"
    dif = int(num_files) - int(number)
    if dif > 0:
        for i in range(0, dif):
            local("rm  versions/$(ls -1t versions/ | tail -1)")
