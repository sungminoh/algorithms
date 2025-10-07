module.exports = function fact(x) {
  if (x < 0) return;
  if (x === 0) return 1;
  return x * fact(x - 1);
}
