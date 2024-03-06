#!/usr/bin/python3
# generates a .tgz archive from the contents of the web_static folder
from datetime import datetime
from fabric.api import local
import os


def do_pack():
    """
    """
    local("sudo mkdir -p versions")
    time = datetime.today()
    ts = time.strftime("%Y%m%d%H%M%S")
    local(f"sudo tar -cvzf versions/web_static_{ts}.tgz web_static")
    path = f"versions/web_static_{ts}.tgz"
    if os.path.exists(path):
        size = os.path.getsize(path)
        return path
    else:
        return None
