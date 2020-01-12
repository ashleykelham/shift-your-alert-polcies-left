from google.cloud import datastore
client = datastore.Client()

def alerts(request):
    key = client.key('alerts', 1234)
    entity = datastore.Entity(key=key)
    entity.update({
        'foo': u'bar',
        'baz': 1337,
        'qux': False,
    })
    client.put(entity)
    return request
