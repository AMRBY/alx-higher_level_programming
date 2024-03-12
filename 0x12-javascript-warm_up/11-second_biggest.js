#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const b = [];
  for (let i = 2; i < process.argv.length; i++) {
    b[i - 2] = Number(process.argv[i]);
  }
  b.sort(function (a, b) { return b - a; });
  console.log(b[1]);
}
