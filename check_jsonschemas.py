from invenio_factory_patch.factory import create_app

app = create_app()
store = app.extensions["invenio-jsonschemas"].refresolver_store()

print(store)
