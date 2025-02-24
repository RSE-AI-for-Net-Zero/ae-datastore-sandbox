import sys

from invenio_access.permissions import system_identity
from invenio_factory_patch.factory import create_api

id_ = sys.argv[1]

api = create_api()

records_service = api.extensions['invenio-rdm-records'].records_service

with api.app_context():
    record = records_service.read(identity=system_identity, id_=id_).to_dict()
    record["metadata"]["domain_metadata"]["colour"] = "red"
    result = records_service.update(identity=system_identity, id_ = id_, data=record)


#NotImplementedError: Records should be updated via their draft.
    
    
'''
curl http://localhost:9200/v12-rdmdomainrecords-drafts-draft-v6.0.0/_search -H "Content-type: application/json" -d '{"query": {"match_all": {}}}' | python -m json.tool | tee index-search.json
'''

    
    


