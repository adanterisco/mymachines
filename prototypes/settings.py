
MONGO_HOST   = 'localhost'
MONGO_PORT   = 27017
MONGO_DBNAME = 'machinestest'

RESOURCE_METHODS = [ 'GET', 'POST', 'DELETE' ]
ITEM_METHODS     = [ 'GET', 'PATCH', 'PUT', 'DELETE' ]

schema = {
    'shortname': {
        'type': 'string',
        'minlength': 7,
        'maxlength': 20,
        'required': True
    },
    'fqdn': {
        'type': 'string',
        'minlength': 7,
        'maxlength': 40
    },
    #Create a custom type called ipaddr for the following
    'public-ip': {
        'type': 'string',
        'required': True,
        'unique': True
    },
    'private-ip': {
        'type': 'string'
    }
}

machines = {
    'item_title': 'machine',
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'shortname',
    },
    'schema': schema
}

DOMAIN = { 'machines': machines }
