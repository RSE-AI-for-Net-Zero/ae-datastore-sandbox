# AE Datastore Sandbox

Adapted from a local development install of InvenioRDM v12.0, with the following changes

- Optional support for authentication via LDAP
- [invenio-factory-patch](https://github.ic.ac.uk/aeronautics/invenio-factory-patch) enforces ordering in the loading of some extensions from entry points, providing replacements for the factory functions (e.g., `create_app`), wsgi and celery entry points defined in ``invenio-app``, as well as a replacement for the `invenio` CLI utility
- [invenio-rdm-domain-records](https://github.ic.ac.uk/aeronautics/invenio-rdm-domain-records) extends the internal data model, defined in [ae-datastore-schemas](https://github.ic.ac.uk/aeronautics/ae-datastore-schemas)


## Requirements

1. Docker
2. [pipenv](https://pipenv.pypa.io/en/latest/)
3. Python v3.9
4. Node v20.9.0 & NPM v10.1.0 (e.g., with [NVM](https://github.com/nvm-sh/nvm))

## Build

1. Clone the repo and cd into directory
```
git clone git@github.com:RSE-AI-for-Net-Zero/ae-datastore-sandbox.git
cd ae-datastore-sandbox
```
2. Run the install script
```
source install.sh
```
## Set up services

### Source the setup script
```
source setup-services.sh
```

### Start the docker containers

These sometimes take a few seconds to come up - repeating this command gives their current status
```
start_containers
```

### Initialise services and fixtures (& optionally) load the demo data
```
_setup && fixtures && demo
```   
or
```
_setup && fixtures
```

## Launch the app
First ensure the containers are running
```
source setup-services.sh && start_containers
```
### Launch the celery workers
In a terminal window
```
./start-celery.sh
```
Leave this running.  For a newly initialised service the workers have to clear the initial task queue - let this complete before the next step

### Launch the app
In a separate terminal window, enter
```
./start-app.sh
```
then navigate to https://127.0.0.1:5000

The app uses demo SSL certificates prompting your web browser to issue a warning - just ignore and continue

### Shut down services
```
source setup-services.sh && stop_containers
```
### Destroy DB, search indexes, clear task queue & wipe uploaded data :skull: :fire: ❗
```
source setup-services.sh && _cleanup
```
## Hints

1. After setting up a new user on the sign-up page a confirmation link is echoed to standard out in the terminal window in which you launched ```start-app.sh```.  Just copy and paste this link into your browser to confirm the new user's email address.
   
2. To access the CLI utility
   ```
   cd ae-datastore-sandbox
   pipenv run ae-datastore --help
   ```
   Use this rather than `pipenv run invenio ...` since it uses the correct factory function to load the app. 

## Overview

Following is an overview of the generated files and folders:

| Name | Description |
|---|---|
| ``Dockerfile`` | Dockerfile used to build your application image. |
| ``Pipfile`` | Python requirements installed via [pipenv](https://pipenv.pypa.io) |
| ``Pipfile.lock`` | Locked requirements (generated on first install). |
| ``app_data`` | Application data such as vocabularies. |
| ``assets`` | Web assets (CSS, JavaScript, LESS, JSX templates) used in the Webpack build. |
| ``docker`` | Example configuration for NGINX and uWSGI. |
| ``docker-compose.full.yml`` | Example of a full infrastructure stack. |
| ``docker-compose.yml`` | Backend services needed for local development. |
| ``docker-services.yml`` | Common services for the Docker Compose files. |
| ``invenio.cfg`` | The Invenio application configuration. |
| ``logs`` | Log files. |
| ``static`` | Static files that need to be served as-is (e.g. images). |
| ``templates`` | Folder for your Jinja templates. |
| ``.invenio`` | Common file used by Invenio-CLI to be version controlled. |
| ``.invenio.private`` | Private file used by Invenio-CLI *not* to be version controlled. |

## Documentation

To learn how to configure, customize, deploy and much more, visit
the [InvenioRDM Documentation](https://inveniordm.docs.cern.ch/).
