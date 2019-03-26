images = {
    'schema': {
        'image': {'type': 'media'},
    },
}

collections = {
    'schema': {
        'name': {'type': 'string'},
        'class_code': {'type': 'string', 'maxlength': 5, 'unique': True},
        'images': {
            'type': 'list',
            'schema': {
                'type': 'objectid',
                'data_relation': {
                    'resource': 'images',
                    'embeddable': True,
                }
            }
        },
    }
}

networks = {
    'schema': {
        'name': {'type': 'string'},
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
}

operations = {
    'schema': {
        'name': {'type': 'string'},
        'step': {'type': 'float'},
        'network': {
            'type': 'objectid',
            'data_relation': {
                'resource': 'networks',
                'field': '_id',
                'embeddable': True,
            }
        },
    },
}
