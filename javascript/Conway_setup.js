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
