import django.utils.simplejson as json

def serialize_post(post):
    fields = [i.name for i in post._meta.fields]
    data = {}
    for i in fields:
        data[i] = post.__dict__[i]
    return json.dumps(data)