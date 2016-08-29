setInterval(() => {
	console.log("LOOP");
	board.step();
	board.transition();
}, 1000);
