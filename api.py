from eve import Eve
from flask import current_app

app = Eve()
app.config['DEBUG'] = True


def after_deleted_collections(item):
    current_app.data.driver.db['images'].remove({"collection": item['_id']}, multi=True)


app.on_deleted_item_collections += after_deleted_collections

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
