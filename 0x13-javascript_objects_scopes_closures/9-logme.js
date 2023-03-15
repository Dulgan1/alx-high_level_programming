#!/usr/bin/node
let logcnt = -1;
exports.logMe = function (item) {
  logcnt++;
  console.log(logcnt + ': ' + item);
}
