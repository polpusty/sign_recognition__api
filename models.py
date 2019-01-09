images = {
    'schema': {
        'image': {'type': 'media'},
        'collection': {
            'type': 'objectid',
            'data_relation': {
                'resource': 'collections',
                'field': '_id',
                'embeddable': True,
            }
        }
    },
    'resource_methods': ['GET', 'POST', 'DELETE'],
    'item_methods': ['GET', 'DELETE', 'PATCH']
}

collections = {
    'schema': {
        'name': {'type': 'string', 'minlength': 3, 'maxlength': 50},
        'class_code': {'type': 'string', 'maxlength': 5, 'unique': True},
    },
    'resource_methods': ['GET', 'POST', 'DELETE'],
    'item_methods': ['GET', 'DELETE', 'PATCH']
}

networks = {
    'schema': {
        'name': {'type': 'string', 'maxlength': 50},
        'collections': {
            'type': 'list',
            'schema': {
                'type': 'objectid',
                'data_relation': {
                    'resource': 'collections',
                    'embeddable': True,
                }
            }
        },
        'trained': {'type': 'media'}
    },
    'resource_methods': ['GET', 'POST', 'DELETE'],
    'item_methods': ['GET', 'DELETE', 'PATCH']
}

operations = {
    'schema': {
        'name': {'type': 'string', 'maxlength': 50},
        'step': {'type': 'float'},
    },
    'resource_methods': ['GET', 'POST', 'DELETE'],
    'item_methods': ['GET', 'DELETE', 'PATCH']
}
