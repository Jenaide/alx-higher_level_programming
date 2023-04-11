#!/usr/bin/node
const arg = process.argv.length;
if (arg > 3) {
  console.log('Arguments found');
} else if (arg === 3) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
