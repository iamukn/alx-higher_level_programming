#!/usr/bin/node

exports.esrever = function (list) {
  return (list.sort((a, b) => a - b));
};
