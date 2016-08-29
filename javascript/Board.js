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
