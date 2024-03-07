#!/usr/bin/python3
# distributes an archive to your web servers, using the function do_deploy
from fabric.api import env, put, run
from os.path import exists


env.hosts = ["52.91.202.237", "34.224.16.163"]
def do_deploy(archive_path):
    """
    """
    if exists(archive_path):
        try:
            # versions/web_static_20170315003959.tgz
            file_n = archive_path.split('/')[-1] # web_static_20170315003959.tgz
            no_ext = file_n.split('.')[0] # web_static_20170315003959
            path = '/data/web_static/releases/'
            put(archive_path, '/tmp/')
            run("sudo mkdir  -p {}{}".format(path, no_ext))
            run('tar -xzf /tmp/{} -C {}{}'.format(file_n, path, no_ext))
            run('sudo rn /tmp/{}'.format(file_n))
            run('sudo mv {0}{1}/web_static/* {0}{1}'.format(path, no_ext))
            run('sudo rm -rf {}{}/web_static'.format(path, no_ext))
            run('sudo rm -rf /data/web_static/current')
            run('sudo ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
            return True
        except:
            return False
    else:
        return False
