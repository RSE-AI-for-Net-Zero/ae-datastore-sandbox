import sys
from invenio_access.permissions import system_identity
from invenio_rdm_records.fixtures.tasks import current_rdm_records_service
from invenio_rdm_records.fixtures.demo import create_fake_record
from invenio_factory_patch.factory import create_api

id_ = sys.argv[1]

app = create_api()

with app.app_context():
    item = current_rdm_records_service.publish(identity=system_identity,
                                                     id_ = id_)
    print(item.to_dict())
    


    
'''
curl http://localhost:9200/v12-rdmdomainrecords-drafts-draft-v6.0.0/_search -H "Content-type: application/json" -d '{"query": {"match_all": {}}}' | python -m json.tool | tee index-search.json
'''

    
    
