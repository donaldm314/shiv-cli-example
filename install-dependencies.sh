#!/bin/bash

# Is task already installed?
which task
rc=$?

set -e 
if [ 0 -ne $rc ]; then
    deb='task_linux_amd64.deb'
    wget https://github.com/go-task/task/releases/download/v3.37.2/${deb}
    sudo dpkg -i ${deb}
    rm -f ${deb}
fi

pipenv install --ignore-pipfile
