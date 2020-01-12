from google.cloud import datastore
import os
import json

client = datastore.Client()

def alerts(request):
    kind = 'alerts-' + os.environ['ENV']
    if request.method == 'POST' or request.method == 'PUT':
        print(request.data) 
        request_json = request.get_json()
        incident = request_json['incident']
        state = incident['state']
        name = incident['policy_name']
        incident_id = incident['incident_id']
        key = client.key(kind, incident_id)

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
    elif request.method == 'GET':
        query = client.query(kind=kind)
        results = list(query.fetch(limit=50))
        output = {
            "count": results.count
            }
        output["alerts"].append(results) 
        return json.dumps(output)
