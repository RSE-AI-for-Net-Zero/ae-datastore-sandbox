#!/bin/bash

pipenv run flask --app invenio_factory_patch.factory:create_app run \
       --debug \
       --cert docker/nginx/test.crt \
       --key docker/nginx/test.key \
       --extra-files invenio.cfg
