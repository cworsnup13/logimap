import json
from connection import Connection

filee = open("./testdata.json","r")
loaded = json.loads(filee.read())

connection_collection = []

print "Loaded Information"
for conn in loaded["Connections"]:
	temp = Connection(json.dumps(conn[0]),json.dumps(conn[1]))
	connection_collection.append(temp)

for c in connection_collection:
	print c.showConnection()
