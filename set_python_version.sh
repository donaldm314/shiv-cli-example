#!/bin/bash

# Update the following files based on MY_PYTHON_VERSION, because DRY.
DOCKERFILE=Dockerfile
PIPFILE=Pipfile
GITHUB_ACTIONS='.github/workflows/github-actions.yml'


exit_code=0
if [ -z ${MY_PYTHON_VERSION} ]; then
    echo "ERROR: MY_PYTHON_VERSION must be set!"
    exit_code=1
fi

if [ 0 -ne $exit_code ]; then
    exit $exit_code
fi

set -e

write_dockerfile() {
    cat > ${DOCKERFILE} <<EOF
FROM mcr.microsoft.com/devcontainers/python:1-${MY_PYTHON_VERSION}-bookworm
EOF
}

update_pipfile() {
    sed -i -r -e "s,^python_version = \".*\",python_version = \"${MY_PYTHON_VERSION}\"," ${PIPFILE}
}

update_github_actions() {
    devcontainer_prefix='mcr.microsoft.com/devcontainers/python:1-'
    sed -i -r -e "s,([ ]+container.[ ]+).*,\1${devcontainer_prefix}${MY_PYTHON_VERSION}-bookworm," ${GITHUB_ACTIONS}
}

write_dockerfile
update_pipfile
update_github_actions