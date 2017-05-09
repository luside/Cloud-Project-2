import couchdb

db_address = 'http://115.146.92.189:5984/'

db_server = couchdb.Server(db_address)

db_doc = db_server['testing']


print (db_doc.info())