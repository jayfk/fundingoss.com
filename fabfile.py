# -*- coding: utf-8 -*-
"""
This is a collection of useful utility functions when working with docker on different environments.
In order to use these functions, install fabric on your local machine with::
    pip install fabric
Please note: Fabric is a remote code execution tool, NOT a remote configuration tool. While you can copy files
from here to there, it is not a good replacement for salt or ansible in this regard.
There is a function called `production` where you need to fill in the details about your production machine(s).
You can then run::
    fab production status
to get the status of your stack
To list all available commands, run::
    fab -l
"""

from __future__ import absolute_import, print_function, unicode_literals
from fabric.operations import local as lrun, run, sudo, put
from fabric.api import *
from fabric.colors import green, red, yellow, blue
from fabric.contrib.console import confirm
import os
import requests
from requests.auth import HTTPBasicAuth


def local():
    """
    Work on the local environment
    """
    env.compose_file = "dev.yml"
    env.project_dir = "."
    env.run = lrun
    env.cd = lcd


def production():
    """
    Work on the production environment
    """
    env.hosts = ["fundingoss.com"]  # list the ip addresses or domain names of your production boxes here
    env.port = 56565  # ssh port
    env.user = "root"  # remote user, see `env.run` if you don't log in as root

    env.compose_file = "docker-compose.yml"
    env.project_dir = "/code/fundingoss.com"  # this is the project dir where your code lives on this machine

    # if you don't use key authentication, add your password here
    # env.password = "foobar"
    # if your machine has no bash installed, fall back to sh
    # env.shell = "/bin/sh -c"

    env.run = run  # if you don't log in as root, replace with 'env.run = sudo'
    env.cd = cd


def copy_secrets():
    """

    :return:
    """
    secrets = [".env"]
    for secret in secrets:
        remote_path = "/".join([env.project_dir, secret])
        print(blue("Copying {secret} to {remote_path} on {host}".format(
            secret=secret, remote_path=remote_path, host=env.host
        )))
        put(secret, remote_path)


def rollback(commit="HEAD~1"):
    """
    Rollback to a previous commit and build the stack
    :param commit: Commit you want to roll back to. Default is the previous commit
    """
    with env.cd(env.project_dir):
        env.run("git checkout {}".format(commit))

    docker_compose("build")


def deploy():
    """
    Pulls the latest changes from master, rebuilt and restarts the stack
    """
    lrun("git push origin master")
    copy_secrets()
    with env.cd(env.project_dir):
        env.run("git pull origin master")

    build()
    restart()





def restart():
    """
    Restart all services
    """
    docker_compose("stop")


def build(cache=True):
    """
    Builds the the stack
    :param cache: Use docker cache. Default is True
    """
    docker_compose("build" if cache else "build --no-cache")


def status():
    """
    Display the status of all services
    """
    docker_compose("ps")


def django_shell():
    """
    Starts a Django shell
    """
    docker_compose("run django python manage.py shell")





def migrate_database():
    """
    Run a Django database migration
    """
    docker_compose("run django python manage.py migrate")







def logs(service=""):
    """
    Display logs
    :param service: Service to display the logs from. Default is all
    """
    docker_compose("logs" if not service else "logs {}".format(service))





def docker_compose(command):
    """
    Run a docker-compose command
    :param command: Command you want to run
    """
    with env.cd(env.project_dir):
        return env.run("docker-compose -f {file} {command}".format(file=env.compose_file, command=command))

