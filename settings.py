from models import images, collections, networks, operations

DOMAIN = {'images': images, 'collections': collections, 'networks': networks, 'operations': operations}

RETURN_MEDIA_AS_BASE64_STRING = False
MEDIA_ENDPOINT = 'media'
RETURN_MEDIA_AS_URL = True

MONGO_HOST = 'db'

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']
