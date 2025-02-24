import sys

from invenio_access.permissions import system_identity
from invenio_factory_patch.factory import create_api

id_ = sys.argv[1]

api = create_api()

records_service = api.extensions['invenio-rdm-records'].records_service

with api.app_context():
    data["metadata"]["domain_metadata"]["colour"] = "blue"
    result = records_service.update_draft(identity=system_identity, id_ = id_, data=data)

with api.app_context():
    result = records_service.read_draft(identity=system_identity, id_ = id_)
    assert result.data["metadata"]["domain_metadata"] == {"entry_type": {"longitude": 66.0,
                                                                         "latitude": -22.0},
                                                          "colour": "blue"}




    
    
'''
curl http://localhost:9200/v12-rdmdomainrecords-drafts-draft-v6.0.0/_search -H "Content-type: application/json" -d '{"query": {"match_all": {}}}' | python -m json.tool | tee index-search.json
'''

    
    
