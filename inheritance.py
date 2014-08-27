class parent:
	def __init__(self):
		print "parentHello"
		
	def parent_method(self):
		print "yo"
		
class child(parent):
	def child_method(self):
		print "child"

c = child()
c.child_method()
c.parent_method()
p = parent()
