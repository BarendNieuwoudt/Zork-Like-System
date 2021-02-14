class node:

	# Create a new node with an optional title and text.
	def __init__(self, title, text):
		self.title = title
		self.text = text
		self.edges = {}
		
	# Add an Edge that leads to a destination node.
	def addEdge(self, node, title = ''):
		self.edges[title] = node
	
	# Add Multiple Edges that lead to the same destination node.
	def addEdges(self, titles, node):
		for title in titles:
			self.edges[title] = node
	
	# Copy this node
	def copy(self):
		return node(self.title, self.text)
	
	# Print all the valid inputs for this node.
	def printEdges(self):
		for edge in self.edges:
				print(' - ' + edge.capitalize())
	
	# Method to handle inputs available at every node. 
	def defaultInputs(self, input):
		if input == 'quit':
			print('Good Bye')
			exit()
		if input == 'help':
			self.printEdges()
			self.visit()
	
	# Print node details.
	def printNode(self):
		banner = '==================================='
		print(banner + banner)
		
		if not self.title == '':
			print(' ~ ' + self.title)
		print('     ' + self.text)
	
	# Visit this node
	def visit(self):
		self.printNode()
		
		# Get input from the player
		inp = input().lower()
		
		self.defaultInputs(inp)
		
		# Actionable will assume the player entered an incorrect value. 
		actionable = False
		
		for edge in self.edges:
			# In all the cases where the player entered a valid value, set
			# 'actionable' to true.
			if edge == '':
				# case for pressing enter to continue
				# and empty edge will always be visited
				actionable = True
				self.edges[edge].visit()
			elif inp == edge.lower():
				# player types a valid response, visit the node
				actionable = True
				self.edges[edge].visit()
		
		# If not actionable, player entered invalid value, restart current node. 
		if not actionable:
			print('Invalid Input')
			self.visit()