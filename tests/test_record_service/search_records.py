from invenio_access.permissions import system_identity
from invenio_factory_patch.factory import create_api

api = create_api()

records_service = api.extensions['invenio-rdm-records'].records_service

with api.app_context():
    result = records_service.search(identity=system_identity)
    for hit in result.hits:
        print(hit['id'], hit['metadata']['domain_metadata'])
