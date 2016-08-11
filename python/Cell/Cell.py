###############################################################################
####	Cell		#################################################################
###############################################################################
class Cell:
	def __init__(self, state):
		self.old_state = state
		self.state = state
		self.new_state = state
		self.town = None
	def __repr__(self):
		return str(self) + str(self.town)
	def update_new_state(self, new_state):
		self.new_state = new_state or self.state
	def update_state(self):
		self.old_state = self.state
		self.state = self.new_state
###############################################################################
####	Cell1D		###############################################################
###############################################################################
class Cell1D(Cell):
	def __init__(self, x, state)
		Cell.__init__(self, state)
		self.x = x
	def __str__(self):
		return ("Cell1D:{x:"		+ str(self.x) +
						" ,old_state:"	+ str(self.old_state) +
						" ,state:"			+ str(self.state) +
						" ,new_state:"	+ str(self.new_state) + "}")
###############################################################################
####	Cell2D		###############################################################
###############################################################################
class Cell2D(Cell):
	def __init__(self, x, y, state):
		Cell.__init__(self, state)
		self.x = x
		self.y = y
	def __str__(self):
		return ("Cell2D:{x:"		+ str(self.x) +
						" ,y:"					+ str(self.y) +
						" ,old_state:"	+ str(self.old_state) +
						" ,state:"			+ str(self.state) +
						" ,new_state:"	+ str(self.new_state) + "}")
###############################################################################
####	Cell3D		###############################################################
###############################################################################
class Cell3D(Cell):
	def __init__(self, x, y, z, state):
		Cell.__init__(self, state)
		self.x = x
		self.y = y
		self.z = z
	def __str__(self):
		return ("Cell3D:{x:"		+ str(self.x) +
						" ,y:"					+ str(self.y) +
						" ,z:"					+ str(self.z) +
						" ,old_state:"	+ str(self.old_state) +
						" ,state:"			+ str(self.state) +
						" ,new_state:"	+ str(self.new_state) + "}")
###############################################################################
####	Cell4D		###############################################################
###############################################################################
class Cell4D(Cell):
	def __init__(self, x, y, z, t, state):
		Cell.__init__(self, state)
		self.x = x
		self.y = y
		self.z = z
		self.t = t
	def __str__(self):
		return ("Cell4D:{x:"		+ str(self.x) +
						" ,y:"					+ str(self.y) +
						" ,z:"					+ str(self.z) +
						" ,t:"					+ str(self.t) +
						" ,old_state:"	+ str(self.old_state) +
						" ,state:"			+ str(self.state) +
###############################################################################
####	CellM			###############################################################
###############################################################################
class CellM(Cell):
	def __init__(self, point, state):
		Cell.__init__(self, state)
		self.point = point















