#!/usr/bin/python3

###############################################################################
####	Point2D	#################################################################
###############################################################################
class Point2D:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def __repr__(self):
		return "(" + str(self.x) + "," + str(self.y) + ")"
	def __eq__(self, other):
		return self.x == other.x and self.y == other.y
	def __add__(self, other):
		return Point2D(self.x + other.x, self.y + other.y)
	def __iadd__(self, other):
		self.x += other.x
		self.y += other.y
		return self
	def __sub__(self, other):
		return Point2D(self.x - other.x, self.y - other.y)
	def __isub__(self, other):
		self.x -= other.x
		self.y -= other.y
		return self
###############################################################################
####	State	###################################################################
###############################################################################
class State:
	def __init__(self, value, name):
		self.value = value
		self.name = name
	def __repr__(self):
		return "State:{value:" + str(self.value) + ", name:\"" + str(self.name) + "\"}"
	def __str__(self):
		return repr(self)
	def __radd__(self, other):
		return other + self.value
	def __rsub__(self, other):
		return other - self.value
	def __add__(self, other):
		if isinstance(other, State):
			return self.value + other.value
		else:
			return self.value + other
State.ZERO = State(0, "ZERO")
State.ONE = State(1, "ONE")
###############################################################################
####	Rule	###################################################################
###############################################################################
class Rule:
	def __init__(self, state):
		self.state = state
		self.new_states = {}
	def get_new_state(self, key):
		if key not in self.new_states:
			return None
		else:
			return self.new_states[key]
###############################################################################
####	Cell2D	#################################################################
###############################################################################
class Cell2D:
	def __init__(self, x, y, state):
		self.x = x
		self.y = y
		self.old_state = state
		self.state = state
		self.new_state = state
		self.town = None
	def __str__(self):
		return ("Cell2D:{x:"		+ str(self.x) +
						" ,y:"					+ str(self.y) +
						" ,old_state:"	+ str(self.old_state) +
						" ,state:"			+ str(self.state) +
						" ,new_state:"	+ str(self.new_state) + "}")
	def __repr__(self):
		return str(self) + str(self.town)
	def update_new_state(self, new_state):
		self.new_state = new_state or self.state
	def update_state(self):
		self.old_state = self.state
		self.state = self.new_state
###############################################################################
####	Region	#################################################################
###############################################################################
class Region:
	def __init__(self, board):
		self.board = board		
		self.cells = set()
		self.rules = {}				#Keyed by State
		self.town_locks = {}	#Keyed by State

	def update_new_state(self):
		for c in self.cells:
			key = self.town_locks[c.state](c.town)
			c.update_new_state( self.rules[c.state].get_new_state(key) )

	def update_state(self):
		for c in self.cells:
			c.update_state()
###############################################################################
####	Town2D	#################################################################
###############################################################################
class Town2D:
	def __init__(self, town_type, board, x, y):
		self.cells = town_type(board, x, y)
		self.town_type = town_type
	def __iter__(self):
		self.i = -1
		return self
	def __next__(self):
		if self.i >= len(self.cells)-1:
			del self.i
			raise StopIteration
		self.i += 1
		return self.cells[self.i]
	@staticmethod
	def MOORE(board, x, y):
		town = []
		town.append(board.get_cell(x - 1, y - 1))		#NW
		town.append(board.get_cell(x,			y - 1))		#N
		town.append(board.get_cell(x + 1, y - 1))		#NE
		town.append(board.get_cell(x + 1, y))				#E
		town.append(board.get_cell(x + 1, y + 1))		#SE
		town.append(board.get_cell(x,			y + 1))		#S
		town.append(board.get_cell(x - 1, y + 1))		#SW
		town.append(board.get_cell(x - 1, y))				#W
		return town
	@staticmethod
	def VONNEUMANN(board, x, y):
		town = []
		town.append(board.get_cell(x,			y - 1))
		town.append(board.get_cell(x,			y + 1))
		town.append(board.get_cell(x - 1, y))
		town.append(board.get_cell(x + 1, y))
		return town
	@staticmethod
	def sum(town):
		s = 0
		for cell in town:
			s += cell.state
		return s
	def state_count(town):
		return NotImplemented
###############################################################################
####	Board2D	#################################################################
###############################################################################
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
			if (x < 0 or x >= self.w or
					y < 0 or y >= self.h):
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

###############################################################################
####	TESTING	#################################################################
###############################################################################
board = Board2D(80, 40, True)
zero = Rule(State.ZERO)
one = Rule(State.ONE)

zero.new_states[3] = State.ONE
one.new_states[0] = State.ZERO
one.new_states[1] = State.ZERO
one.new_states[4] = State.ZERO
one.new_states[5] = State.ZERO
one.new_states[6] = State.ZERO
one.new_states[7] = State.ZERO
one.new_states[8] = State.ZERO

board.preset_region.rules[State.ZERO] = zero
board.preset_region.rules[State.ONE] = one
board.preset_region.town_locks[State.ZERO] = Town2D.sum
board.preset_region.town_locks[State.ONE] = Town2D.sum

board.set_state(1,0,State.ONE)
board.set_state(2,1,State.ONE)
board.set_state(2,2,State.ONE)
board.set_state(1,2,State.ONE)
board.set_state(0,2,State.ONE)

def print_board(board):
	view = []
	x = 0

	for c in board.cells:
		if c.state is State.ZERO:
			view.append(".")
		else:
			view.append("O")

		if x == board.w - 1:
			view.append("\n")

		x += 1
		x %= board.w
	print("".join(view))

import time

while True:
	print_board(board)
	board.update_new_state()
	board.update_state()
	time.sleep(1)















