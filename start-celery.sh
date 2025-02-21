#!/bin/bash

pipenv run celery --app invenio_factory_patch.celery worker --beat --events --loglevel INFO
