from node import node

inv = ['investigate', 'look around']
invNothing = node('', 'You look around but see nothing of interest.')

# ==========================================================
# NPCs
# ==========================================================

def genericGuard(exitNode):
	guard = node('Guard', 'How are you today?')
	guardResponse = node('Guard', 'All right')
	guard.addEdge(guardResponse)
	guardResponse.addEdge(exitNode)
	return guard

# ==========================================================
# Player's House
# ==========================================================

def bedroomHouse():
	br = node('Bed Room', 'You are standing in your room, next to a bed and a desk.')
	
	# Investigate the Bedroom 
	iBr = invNothing.copy()
	br.addEdges(inv, iBr)
	iBr.addEdge(br)
	
	return br
	
def livingRoom(bedroom):
	livingroom = node('Living Room', 'You are standing next to your couch.')
	livingroom.addEdge(bedroom, 'bedroom')
	
	# Investigate the Living room
	invLivingRoom = invNothing.copy()
	livingroom.addEdges(inv, invLivingRoom)
	invLivingRoom.addEdge(livingroom)
	
	return livingroom

# ==========================================================
# Village
# ==========================================================

def roadFrontDoor(livingroom):

	title = 'Road'
	text = 'You are standing on a gravel road in front of your house. There is an on-duty guard patrolling past here.'

	roadFrontDoor = node(title, text)
	
	roadFrontDoor.addEdges(['talk to guard', 'guard', 'speak to guard', 'talk', 'speak', 'say hello', 'hello', 'hi'], genericGuard(roadFrontDoor))
	roadFrontDoor.addEdges(['enter', 'house', 'door', 'front door', 'go inside', 'inside'], livingroom)
	
	return roadFrontDoor

# ==========================================================
# Game
# ==========================================================

bedroom = bedroomHouse()
livingroom = livingRoom(bedroom)
bedroom.addEdges(['exiT', 'leave', 'door'], livingroom)

roadFrontDoor = roadFrontDoor(livingroom)
livingroom.addEdges(['exit', 'leave', 'door', 'outside', 'road', 'go outside'], roadFrontDoor)

bedroom.visit()