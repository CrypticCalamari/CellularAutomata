#!/usr/bin/node
class State {
	constructor (name, value, color) {
		this.name = name;
		this.value = value;
		this.color = color;
	}
}
State.ZERO = new State("ZERO", 0, "rgb(0,0,0)");
State.ONE = new State("One", 1, "rgb(255,255,255)");
class Rule {
	constructor (state) {
		this.curr_state = state;
		this.next_states = new Map();
	}
}
class KeyGen {
	static sum (town) {
		let s = 0;

		for (const cell of town.cells) {
			s += cell.curr_state.value;
		}

		return s;
	}
}
class Town {
	constructor (board, cell, town_type) {
		this.cells = town_type(board, cell.x, cell.y);
	}
	static MOORE (board, x, y) {
		let town = [];

		town.push(board.get_cell(x - 1, y - 1));
		town.push(board.get_cell(x,			y - 1));
		town.push(board.get_cell(x + 1, y - 1));
		town.push(board.get_cell(x + 1, y));
		town.push(board.get_cell(x + 1, y + 1));
		town.push(board.get_cell(x,			y + 1));
		town.push(board.get_cell(x - 1, y + 1));
		town.push(board.get_cell(x - 1, y));

		return town;
	}
	static VON_NEUMANN (board, x, y) {
		let town = [];

		town.push(board.get_cell(x,			y - 1));
		town.push(board.get_cell(x + 1, y));
		town.push(board.get_cell(x,			y + 1));
		town.push(board.get_cell(x - 1, y));

		return town;
	}
	static X (board, x, y) {
		let town = [];

		town.push(board.get_cell(x - 1, y - 1));
		town.push(board.get_cell(x + 1, y - 1));
		town.push(board.get_cell(x + 1, y + 1));
		town.push(board.get_cell(x - 1, y + 1));

		return town;
	}
}
class Cell {
	constructor (x, y, state) {
		this.x = x;
		this.y = y;
		this.prev_state = state;
		this.curr_state = state;
		this.next_state = state;
		this.town = null;
	}
	transition() {
		this.prev_state = this.curr_state;
		this.curr_state = this.next_state;
	}
}
class Region {
	constructor (board) {
		this.board = board;
		this.cells = new Set();
		this.rules = new Map();
		this.key_gens = new Map();
	}
	step () {
		for (const cell of this.cells) {
			let rule = this.rules.get(cell.curr_state);
			let key_gen = this.key_gens.get(cell.curr_state);
			let key = key_gen(cell.town);
			cell.next_state = rule.next_states.get(key) || cell.next_state;
		}
	}
}
class Board {
	constructor (w, h, wrapped=false) {
		this.w = w;
		this.h = h;
		this.wrapped = wrapped;
		this.border = (wrapped ? null : new Cell(-1, -1, State.ZERO));
		this.cells = [];
		this.regions = new Set();
		this.preset_region = new Region(this);

		this.regions.add(this.preset_region);

		for (let j = 0; j < this.h; j++)
			for (let i = 0; i < this.w; i++)
				this.cells.push(new Cell(i, j, State.ZERO));

		for (const cell of this.cells) {
			cell.town = new Town(this, cell, Town.MOORE);
			this.preset_region.cells.add(cell);
		}
	}
	get_cell (x, y) {
		if (this.wrapped) {
			let x_x = (x < 0 ? this.w - (-x % this.w) : x % this.w);
			let y_y = (y < 0 ? this.h - (-y % this.h) : y % this.h);
			return this.cells[x_x + (this.w * y_y)];
		}
		else {
			if (x < 0 || y < 0 || x >= this.w || y >= this.h)
				return this.border;
			else
				return this.cells[x + (this.w * y)];
		}
	}
	step () {
		for (const region of this.regions)
			region.step();
	}
	transition () {
		for (const cell of this.cells)
			cell.transition();
	}
}
let board = new Board(4, 4, true);

let dead = new Rule(State.ZERO);
let alive = new Rule(State.ONE);

dead.next_states.set(3, State.ONE);

alive.next_states.set(0, State.ZERO);
alive.next_states.set(1, State.ZERO);
alive.next_states.set(4, State.ZERO);
alive.next_states.set(5, State.ZERO);
alive.next_states.set(6, State.ZERO);
alive.next_states.set(7, State.ZERO);
alive.next_states.set(8, State.ZERO);

board.preset_region.rules.set(State.ZERO, dead);
board.preset_region.rules.set(State.ONE, alive);

board.preset_region.key_gens.set(State.ZERO, KeyGen.sum);
board.preset_region.key_gens.set(State.ONE, KeyGen.sum);
	setInterval(function () {
		console.log("LOOP");
		board.step();
		board.transition();
	}, 1000);
