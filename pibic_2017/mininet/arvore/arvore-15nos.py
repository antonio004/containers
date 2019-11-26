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
	h3 = net.addHost( 'h3', ip='192.0.1.2', netmask='255.255.255.0' )
	h4 = net.addHost( 'h4', ip='192.0.1.3', netmask='255.255.255.0' )
	h5 = net.addHost( 'h5', ip='192.0.1.4', netmask='255.255.255.0' )
	h6 = net.addHost( 'h6', ip='192.0.1.5', netmask='255.255.255.0' )
	h7 = net.addHost( 'h7', ip='192.0.1.6', netmask='255.255.255.0' )
	h8 = net.addHost( 'h8', ip='192.0.1.7', netmask='255.255.255.0' )

	info( 'Add switch\n' )
	s0 = net.addSwitch( 's0' )
	s1 = net.addSwitch( 's1' )
	s2 = net.addSwitch( 's2' )
	s3 = net.addSwitch( 's3' )
	s4 = net.addSwitch( 's4' )
	s5 = net.addSwitch( 's5' )
	s6 = net.addSwitch( 's6' )
	s7 = net.addSwitch( 's7' )
	s8 = net.addSwitch( 's8' )
	s9 = net.addSwitch( 's9' )
	s10 = net.addSwitch( 's10' )
	s11 = net.addSwitch( 's11' )
	s12 = net.addSwitch( 's12' )
	s13 = net.addSwitch( 's13' )
	s14 = net.addSwitch( 's14' )
	
	info( 'Criando os links\n' )
	net.addLink(s0,s1)
	net.addLink(s1,s2)
	net.addLink(s2,s3)
	net.addLink(s2,s4)

	net.addLink(s1,s5)
	net.addLink(s5,s6)
	net.addLink(s5,s7)

	net.addLink(s0,s8)
	net.addLink(s8,s9)
	net.addLink(s9,s10)
	net.addLink(s9,s11)

	net.addLink(s8,s12)
	net.addLink(s12,s13)
	net.addLink(s12,s14)


	net.addLink( h1, s6 )
	net.addLink( h2, s7 )
	net.addLink( h3, s4 )
	net.addLink( h4, s3 )
	net.addLink( h5, s10 )
	net.addLink( h6, s11 )
	net.addLink( h7, s13 )
	net.addLink( h8, s14 )
	net.start()
	CLI( net )
	net.stop()
if __name__ == '__main__':
	setLogLevel( 'info' )
	emptyNet()