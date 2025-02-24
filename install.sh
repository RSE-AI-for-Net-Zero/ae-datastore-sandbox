# invenio-cli install --help

# pre: install alpha releases?
# dev: install dev dependencies?
# production / development: copy vs. symlink statics/assets?

# pre: -------- False
# dev: -------- True
# production -- False

#install(cli_config, pre=False, dev=True, production=False)
#commands = InstallCommands(cli_config)
#steps = commands.install(pre=False, dev=True, flask_env="development")


CMD="pipenv run ae-datastore"


# steps:
#
# install_py_dependencies
## PackagesCommands.lock
pipenv lock --dev 
## PackagesCommands.install_locked_dependencies
pipenv sync --dev

#ADD NULL PATH FOR invenio_factory_patch_*.cfg FILES
#e.g., if not present then load entire ep group, as-is

# update_instance_path
## - run cmd
INVENIO_INSTANCE_PATH=$(${CMD} shell --no-term-title -c 'print(app.instance_path, end="")')
## - cli_config.update_instance_path (instance path ref'd by next cmd)

# symlink_project_file_or_folder invenio.cfg
python force_symlink.py ${INVENIO_INSTANCE_PATH} invenio.cfg
python force_symlink.py ${INVENIO_INSTANCE_PATH} invenio_factory_patch_api.cfg
python force_symlink.py ${INVENIO_INSTANCE_PATH} invenio_factory_patch_ui.cfg


# symlink_project_file_or_folder templates
python force_symlink.py ${INVENIO_INSTANCE_PATH} templates

# symlink_project_file_or_folder app_data
python force_symlink.py ${INVENIO_INSTANCE_PATH} app_data

export FLASK_ENV="development"

# update_statics_and_assets
${CMD} collect --verbose
${CMD} webpack clean create
${CMD} webpack install

/bin/cp --recursive static/* ${INVENIO_INSTANCE_PATH}/static
/bin/cp --recursive assets/* ${INVENIO_INSTANCE_PATH}/assets

${CMD} webpack build


