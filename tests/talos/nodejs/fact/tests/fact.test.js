const assert = require('assert').strict;

const fact = require('../fact/fact');

assert.equal(fact(0), 1)
assert.equal(fact(1), 1)
assert.equal(fact(2), 2)
assert.equal(fact(3), 6)
