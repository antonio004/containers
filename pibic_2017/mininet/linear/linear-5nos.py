#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def emptyNet():
	net = Mininet( controller=RemoteController )
	info( "Adicionando o IP do Controller SDN e a porta" )
	net.addController( 'c0',controller=RemoteController,ip='172.28.5.0',port=6653 )
	info( 'Add hosts\n' )
	h1 = net.addHost( 'h1', ip='192.0.1.0', netmask='255.255.255.0' )
	h2 = net.addHost( 'h2', ip='192.0.1.1', netmask='255.255.255.0' )
	#h3 = net.addHost( 'h3', ip='192.0.1.2', netmask='255.255.255.0' )
	#h4 = net.addHost( 'h4', ip='192.0.1.3', netmask='255.255.255.0' )
	info( 'Add switch\n' )
	s0 = net.addSwitch( 's0' )
	s1 = net.addSwitch( 's1' )
	s2 = net.addSwitch( 's2' )
	s3 = net.addSwitch( 's3' )
	s4 = net.addSwitch( 's4' )
	info( 'Criando os links\n' )
	net.addLink(s0,s1)
	net.addLink(s1,s2)
	net.addLink(s2,s3)
	net.addLink(s3,s4)
	net.addLink( h1, s0 )
	net.addLink( h2, s4 )
	net.start()
	CLI( net )
	net.stop()
if __name__ == '__main__':
	setLogLevel( 'info' )
	emptyNet()