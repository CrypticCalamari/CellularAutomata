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
