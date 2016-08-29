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
