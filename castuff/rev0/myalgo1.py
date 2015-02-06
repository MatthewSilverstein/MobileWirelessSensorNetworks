""" My algo for first problem.  Idea is to base it off the one with the forces and add another force 
for the radius sensor"""

class MySensor:

	def __init__(self, rc, rs):
		self.rc = rc
		self.rs = rs

	def iterate(self):
		
