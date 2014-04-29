# Class definition for Conneciton Type
class Connection:
	def __init__(self, conn_from, conn_to):
		self.connect_from = conn_from
		self.connect_to = conn_to
	def showConnection(self):
		return [self.connect_from, self.connect_to]
	def getFrom(self):
		return self.connect_from
	def getTo(self):
		return self.connect_to

