
node={"value": "String","next": "node"}


def kth_ToLastNode(k,node):
	next_node = 0
	if k != 0:
		for k,v in node.items():			
			if k == "next":
				next_node = v
			if k == 'value':
				print(v)				
			yield v
			
			

	

k =kth_ToLastNode(1,node)

 
next(k)









