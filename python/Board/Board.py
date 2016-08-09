class State:
	"""Dummy Class"""
	def __init(self, value):
		self.value = value
State.ZERO = State(0)
class Region:
	"""Dummy Class"""
	def __init__(self, board):
		self.board = board

class Board1D:
	def __init__(self, size, wrapped=False):
		self.size = size
		self.wrapped = wrapped
		self.border = None if wrapped else Cell1D(-1, State.ZERO)
		self.cells = []
		self.regions = set()
		self.preset_region = Region(self)
class Board2D:
	def __init__(self, w, h, wrapped=False):
		self.w = w
		self.h = h
		self.wrapped = wrapped
		self.border = None if wrapped else Cell2D(-1,-1,State.ZERO)
		self.cells = []
		self.regions = set()
		self.preset_region = Region(self)

		for i in range(h):
			for j in range(w):
				self.cells.append( Cell2D(j, i, State.ZERO) )

		for c in self.cells:
			c.town = Town2D( Town2D.MOORE, self, c.x, c.y )

		self.preset_region.cells.update(self.cells)
		self.regions.add(self.preset_region)
	def __repr__(self):
		return "Board2D:{}"
	def get_cell(self, x, y):
		if not self.wrapped:
			if (not (0 < x < self.w) or
					not (0 < y < self.h)):
				return self.border
			else:
				return self.cells[x + y * self.w]
		else:
			return self.cells[(x % self.w) + (y % self.h) * self.w]
	def set_state(self, x, y, state):
		self.get_cell(x,y).state = state
	def update_new_state(self):
		for region in self.regions:
			region.update_new_state()
	def update_state(self):
		for region in self.regions:
			region.update_state()
	def add_cell_to_region(self, region, x, y):
		self.regions[region].cells.add( self.get_cell(x, y) )
	def remove_cell_from_region(self, region, x, y):
		self.regions[region].cells.discard( self.get_cell(x, y) )
class Board3D:
	def __init__(self, w, h, l, wrapped=False):
		self.w = w
		self.h = h
		self.l = l
		self.wrapped = wrapped
		self.border = None if wrapped else Cell3D(-1, -1, -1, State.ZERO)
		self.cells = []
		self.regions = set()
		self.preset_region = Region(self)

		for i in range(l):
			for j in range(h):
				for k in range(w):
					self.cells.append( Cell3D(k, j, i, State.ZERO) )

		for c in self.cells:
			c.town = Town3D( Town3D.MOORE, self, c.x, c.y, c.z )

		self.preset_region.cells.update(self.cells)
		self.regions.add(self.preset_region)
	def get_cell(self, x, y, z):
		if not self.wrapped:
			if (not (0 < x < self.w) or
					not (0 < y < self.h) or
					not (0 < z < self.l)):
				return self.border
			else:
				#TODO: Left off at this spot.
				return self.cells[x + y * self.w + z * ]
		else:
			return self.cells[(x % self.w) + (y % self.h) * self.w]
class BoardM:
	def __init__(self, size, wrapped=False):
		self.size = size
		self.wrapped = wrapped
		self.border = None if wrapped else CellM(None, State.ZERO)
		self.cells = []
		self.regions = set()
		self.preset_region = Region(self)

		







