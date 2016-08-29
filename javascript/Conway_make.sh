#!/bin/bash

touch ConwaysGameOfLife.js

echo '#!/usr/bin/node' > ConwaysGameOfLife.js
cat State.js >> ConwaysGameOfLife.js
cat Rule.js >> ConwaysGameOfLife.js
cat KeyGen.js >> ConwaysGameOfLife.js
cat Town.js >> ConwaysGameOfLife.js
cat Cell.js >> ConwaysGameOfLife.js
cat Region.js >> ConwaysGameOfLife.js
cat Board.js >> ConwaysGameOfLife.js
cat Conway_setup.js >> ConwaysGameOfLife.js
cat main.js >> ConwaysGameOfLife.js

chmod +x ConwaysGameOfLife.js
