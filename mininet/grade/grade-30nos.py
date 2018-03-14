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
	s15 = net.addSwitch( 's15' )
	s16 = net.addSwitch( 's16' )
	s17 = net.addSwitch( 's17' )
	s18 = net.addSwitch( 's18' )
	s19 = net.addSwitch( 's19' )
	s20 = net.addSwitch( 's20' )
	s21 = net.addSwitch( 's21' )
	s22 = net.addSwitch( 's22' )
	s23 = net.addSwitch( 's23' )
	s24 = net.addSwitch( 's24' )
	s25 = net.addSwitch( 's25' )
	s26 = net.addSwitch( 's26' )
	s27 = net.addSwitch( 's27' )
	s28 = net.addSwitch( 's28' )
	s29 = net.addSwitch( 's29' )


	info( 'Criando os links\n' )
	net.addLink(s0,s1)
	net.addLink(s1,s2)
	net.addLink(s2,s3)
	net.addLink(s3,s4)
	net.addLink(s0,s5)
	net.addLink(s1,s6)
	net.addLink(s2,s7)
	net.addLink(s3,s8)
	net.addLink(s4,s9)
	net.addLink(s5,s6)
	net.addLink(s6,s7)
	net.addLink(s7,s8)
	net.addLink(s8,s9)
	net.addLink(s5,s10)
	net.addLink(s6,s11)
	net.addLink(s7,s12)
	net.addLink(s8,s13)
	net.addLink(s9,s14)
	net.addLink(s10,s11)
	net.addLink(s11,s12)
	net.addLink(s12,s13)
	net.addLink(s13,s14)
	net.addLink(s10,s15)
	net.addLink(s11,s16)
	net.addLink(s12,s17)
	net.addLink(s13,s18)
	net.addLink(s14,s19)
	net.addLink(s15,s16)
	net.addLink(s16,s17)
	net.addLink(s17,s18)
	net.addLink(s18,s19)
	net.addLink(s15,s20)
	net.addLink(s16,s21)
	net.addLink(s17,s22)
	net.addLink(s18,s23)
	net.addLink(s19,s24)
	net.addLink(s20,s21)
	net.addLink(s21,s22)
	net.addLink(s22,s23)
	net.addLink(s23,s24)
	net.addLink(s20,s25)
	net.addLink(s21,s26)
	net.addLink(s22,s27)
	net.addLink(s23,s28)
	net.addLink(s24,s29)
	net.addLink(s25,s26)
	net.addLink(s26,s27)
	net.addLink(s27,s28)
	net.addLink(s28,s29)

	net.addLink( h1, s0 )
	net.addLink( h2, s29 )

	net.start()
	CLI( net )
	net.stop()
if __name__ == '__main__':
	setLogLevel( 'info' )
	emptyNet()