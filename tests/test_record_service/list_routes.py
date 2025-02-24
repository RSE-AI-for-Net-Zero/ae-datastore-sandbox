from invenio_factory_patch.factory import create_api

api = create_api()

ext = api.extensions['invenio-rdm-records']
url_rules = [(r['rule'], r['methods'], r['view_func'].__module__, r['view_func'].__name__) \
             for r in ext.records_resource.create_url_rules()]



