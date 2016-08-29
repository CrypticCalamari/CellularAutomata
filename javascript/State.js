class State {
	constructor (name, value, color) {
		this.name = name;
		this.value = value;
		this.color = color;
	}
}
State.ZERO = new State("ZERO", 0, "rgb(0,0,0)");
State.ONE = new State("One", 1, "rgb(255,255,255)");
