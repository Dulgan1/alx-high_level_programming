#!/usr/bin/node

let fileA = process.argv[1];
let fileB = process.argv[2];
let fileC = process.argv[3];
const fs = require('fs');
let textA = fs.readFileSync(fileA, 'utf8');
let textB = fs.readFileSync(fileB, 'utf8');
fs.writeFileSync(fileC, textA + textB);
