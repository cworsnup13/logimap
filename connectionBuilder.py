import json
class ConnectionBuilder:
	def buildConnections(self, connection_file, server_file):
		converge_conn_file = open("./converged_connections.json","w")
		print "Build Connections Method"
		conn = open(connection_file,"r")
		serv = open(server_file,"r")
	 	conn_loaded = json.loads(conn.read())
		for connect in conn_loaded["Connections"]:	
			print connect
			#If there is a role then expand to full server list. 
			# and print out to converged server list


