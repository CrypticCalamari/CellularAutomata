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
