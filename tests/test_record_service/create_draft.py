from invenio_access.permissions import system_identity
from invenio_rdm_records.fixtures.demo import create_fake_record
from invenio_factory_patch.factory import create_api

data = create_fake_record()
data["metadata"]["domain_metadata"] = \
    {
        "entry_type": {
            "longitude": 66.0,
            "latitude": -22.0
        }
    }


api = create_api()

records_service = api.extensions['invenio-rdm-records'].records_service

with api.app_context():
    result = records_service.create(data=data, identity=system_identity)
    id_ = result.id
    print(f"id: {id_}")

with api.app_context():
    result = records_service.read_draft(identity=system_identity, id_ = id_)
    assert result.data["metadata"]["domain_metadata"] == {"entry_type": {"longitude": 66.0,
                                                                         "latitude": -22.0}}
    
    
'''
curl http://localhost:9200/v12-rdmdomainrecords-drafts-draft-v6.0.0/_search -H "Content-type: application/json" -d '{"query": {"match_all": {}}}' | python -m json.tool | tee index-search.json
'''

    
    
