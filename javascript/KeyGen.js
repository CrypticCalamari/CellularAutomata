class KeyGen {
	static sum (town) {
		let s = 0;

		for (const cell of town.cells) {
			s += cell.curr_state.value;
		}

		return s;
	}
}
