#!/bin/bash

set -e 

deb='task_linux_amd64.deb'
wget https://github.com/go-task/task/releases/download/v3.38.0/${deb}
sudo dpkg -i ${deb}
rm -f ${deb}


pipenv install --ignore-pipfile
git config --global --add safe.directory /workspaces/shiv-cli-example
