#!/usr/bin/python3
""" enerates a .tgz archive from the contents of the web_static folder"""
from fabric.api import local


def do_pack():
    """generates a .tgz archive """
    local("mkdir -p ./versions")
    filer = local("tar -cvzf versions/web_static_$(date '+%Y%m%d%H%M%S').tgz web_static")

    if (filer.succeeded):
        return local("echo \"versions/web_static_$(date '+%Y%m%d%H%M%S').tgz\"")
    else:
        return None
