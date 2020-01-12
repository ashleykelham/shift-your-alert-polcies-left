from google.cloud import datastore
import os

client = datastore.Client()

def alerts(request):
    request_json = request.get_json()
    incident = request_json['incident']
    state = incident['state']
    name = incident['policy_name']
    incident_id = incident['incdent_id']
    key = client.key('alerts-' + os.environ['ENV'], incident_id)

    if state == 'open':
        entity = datastore.Entity(key=key)
        entity.update({
            'state': state,
            'name': name
        })
        client.put(entity)
    else:
        client.delete(key)

    return 'success'
