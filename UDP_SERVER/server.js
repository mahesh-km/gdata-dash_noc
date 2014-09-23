#!/usr/bin/node
//
//  UDP server to receive system status message from vscout
//  vscout is a raspberry pi based server
//
//  Chandra V - Dec 20
//
//

var PORT = 33333;
var HOST = '162.243.16.178';

var dgram = require('dgram');
var server = dgram.createSocket('udp4');

server.on('listening', function () {
    var address = server.address();
    console.log('UDP Server listening on ' + address.address + ":" + address.port);
});

server.on('message', function (message, remote) {
    console.log(remote.address + ':' + remote.port +' \n ' + message.toString());

});

server.bind(PORT, HOST);

