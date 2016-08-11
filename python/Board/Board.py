
###############################################################################
####	State Dummy	#############################################################
###############################################################################
class State:
	"""Dummy Class"""
	def __init(self, value):
		self.value = value
State.ZERO = State(0)
###############################################################################
####	Region Dummy	###########################################################
###############################################################################
class Region:
	"""Dummy Class"""
	def __init__(self, board):
		self.board = board

###############################################################################
####	Board		#################################################################
###############################################################################
class Board:
	def __init__(self, wrapped=True, border=None):
		self.wrapped = wrapped
		self.border = border
		self.cells = []
		self.regions = set()
		self.preset_region = Region(self)
	def update_new_state(self):
		for region in self.regions:
			region.update_new_state()
	def update_state(self):
		for region in self.regions:
			region.update_state()
	def add_cell_to_region(self, region, cell):
		self.regions[region].cells.add( cell )
	def remove_cell_from_region(self, region, cell):
		self.regions[region].cells.discard( cell )

###############################################################################
####	Board1D	#################################################################
###############################################################################
class Board1D(Board):
	def __init__(self, w, wrapped=True):
		Board.__init__(self, wrapped, (None if wrapped else Cell1D(-1, State.ZERO)))
		self.w = w

		for i in range(w):
			self.cells.append( Cell1D(i, State.ZERO) )

		for c in self.cells:
			c.town = Town1D(self, c.x)

		self.preset_region.cells.update(self.cells)
		self.regions.add(self.preset_region)
	def get_cell(self, x):
		if not self.wrapped:
			if not (0 <= x < self.w):
				return self.border
			else:
				return self.cells[x]
		else:
			return self.cells[x % self.x]
###############################################################################
####	Board2D	#################################################################
###############################################################################
class Board2D(Board):
	def __init__(self, w, h, wrapped=True):
		Board.__init__(self, wrapped, None if wrapped else Cell2D(-1,-1,State.ZERO))
		self.w = w
		self.h = h

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
				return self.cells[x + (y * self.w)]
		else:
			return self.cells[((x % self.w) +
												((y % self.h) * self.w))]
###############################################################################
####	Board3D	#################################################################
###############################################################################
class Board3D(Board):
	def __init__(self, w, h, l, wrapped=True):
		Board.__init__(self, wrapped, None if wrapped else Cell3D(-1, -1, -1, State.ZERO))
		self.w = w
		self.h = h
		self.l = l

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
				return self.cells[x + (y * self.w) + (z * self.h)]
		else:
			return self.cells[((x % self.w) +
												((y % self.h) * self.w) +
												((z % self.l) * self.h))]
###############################################################################
####	Board4D	#################################################################
###############################################################################
class Board4D(Board):
	def __init__(self, w, h, l, t, wrapped=True):
		Board.__init__(self, wrapped, None if wrapped else Cell4D(-1, -1, -1, -1, State.ZERO))
		self.w = w
		self.h = h
		self.l = l
		self.t = t

		for s in range(t):
			for i in range(l):
				for j in range(h):
					for k in range(w):
						self.cells.append( Cell4D(k, j, i, s, State.ZERO) )

		for c in self.cells:
			c.town = Town4D( Town4D.MOORE, self, c.x, c.y, c.z, c.t )

		self.preset_region.cells.update(self.cells)
		self.regions.add(self.preset_region)
	def get_cell(self, x, y, z, t):
		if not self.wrapped:
			if (not (0 < x < self.w) or
					not (0 < y < self.h) or
					not (0 < z < self.l) or
					not (0 < t < self.t)):
				return self.border
			else:
				return self.cells[x + (y * self.w) + (z * self.h) + (t * self.l)]
		else:
			return self.cells[((x % self.w) +
												((y % self.h) * self.w) +
												((z % self.l) * self.h) +
												((t % self.t) * self.l)]
###############################################################################
####	BoardM	#################################################################
###############################################################################
class BoardM(Board):
	def __init__(self, extent, wrapped=True):
		Board.__init__(self, wrapped, None if wrapped else CellM(None, State.ZERO))
		self.extent = extent

		#create board vector
		#--here--
		#-------------------

		for c in self.cells:
			c.town = TownM( TownM.MOORE, self, c.point )
		
		self.preset_region.cells.update(self.cells)
		self.regions.add(self.preset_region)
		







