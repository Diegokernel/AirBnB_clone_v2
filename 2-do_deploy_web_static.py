#!/usr/bin/python3
""" enerates a .tgz archive from the contents of the web_static folder"""
from fabric.api import *
from os.path import exists
env.hosts = ['35.243.178.239', '35.237.166.91']

def do_pack():
    """generates a .tgz archive """
    local("mkdir -p ./versions")
    filer = local("tar -cvzf versions/web_static_$(date '+%Y%m%d%H%M%S').tgz web_static")

    if (filer.succeeded):
        return local("echo \"versions/web_static_$(date '+%Y%m%d%H%M%S').tgz\"")
    else:
        return None

def do_deploy(archive_path):
    """Uncompress the archive to the folder """
    if exists(archive_path) is False:
        return False
    try:
        upload = put(archive_path, "/tmp/")
        name = archive_path[9:-4]
        rmt_path = "/data/web_static/releases/" + name
        run("sudo mkdir {}".format(rmt_path))
        run("sudo tar -xvzf /tmp/{}.tgz --directory {}/".format(name, rmt_path))
        run("sudo rm /tmp/{}.tgz".format(name))
        run("sudo rm /data/web_static/current")
        run("sudo ln -nsf /data/web_static/releases/{} /data/web_static/current"
            .format(name))
        run("sudo mv {}/web_static/* {}".format(rmt_path, rmt_path))
        run("sudo rm -d {}/web_static/".format(rmt_path))
        return True
    except:
        return False
