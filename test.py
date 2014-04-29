import json
from connection import Connection
from connectionBuilder import ConnectionBuilder

conn_file = open("./testdata.json","r")
server_file = open("./serverlist.json","r")
conn_loaded = json.loads(conn_file.read())
server_loaded = json.loads(server_file.read())
builder  = ConnectionBuilder()

connection_collection = []

builder.buildConnections("./testdata.json","./serverlist.json")	

conn_file = open("./converged_connections.json","r")

for conn in conn_loaded["Connections"]:
	temp = Connection(json.dumps(conn[0]),json.dumps(conn[1]))
	connection_collection.append(temp)

for c in connection_collection:
#	print "From: " + c.getFrom() + " To: " + c.getTo()
	print "a"
