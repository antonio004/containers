#!/usr/bin/python
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info

if __name__ == '__main__':
	
	net = Mininet( controller=RemoteController )
	info( "Adicionando o IP do Controller SDN e a porta" )
	net.addController( 'c0',controller=RemoteController,ip='172.17.0.2',port=6653)
	info( 'Add hosts\n' )
	h1 = net.addHost( 'h1', ip='10.0.0.1', netmask='255.255.255.0' )
	h2 = net.addHost( 'h2', ip='10.0.0.2', netmask='255.255.255.0' )
	info( 'Add switch\n' )
	# Create Switch Nodes
	wth = 64
	for i in range(1, wth):
		locals()['s'+str(i)] = net.addSwitch('s'+str(i))

	info( 'Criando os links\n' )
	net.addLink(s1,s2)
	net.addLink(s1,s33)
	net.addLink(s2,s3)
	net.addLink(s2,s18)
	net.addLink(s3,s4)
	net.addLink(s3,s11)
	net.addLink(s4,s5)
	net.addLink(s4,s8)
	net.addLink(s5,s6)
	net.addLink(s5,s7)
	net.addLink(s8,s9)
	net.addLink(s8,s10)
	net.addLink(s11,s12)
	net.addLink(s11,s15)
	net.addLink(s12,s13)
	net.addLink(s12,s14)
	net.addLink(s15,s16)
	net.addLink(s15,s17)
	net.addLink(s18,s19)
	net.addLink(s18,s26)
	net.addLink(s19,s20)
	net.addLink(s19,s23)
	net.addLink(s20,s21)
	net.addLink(s20,s22)
	net.addLink(s23,s24)
	net.addLink(s23,s25)
	net.addLink(s26,s27)
	net.addLink(s26,s30)
	net.addLink(s27,s28)
	net.addLink(s27,s29)
	net.addLink(s30,s31)
	net.addLink(s30,s32)
	net.addLink(s33,s34)
	net.addLink(s33,s49)
	net.addLink(s34,s35)
	net.addLink(s34,s42)
	net.addLink(s35,s36)
	net.addLink(s35,s39)
	net.addLink(s36,s37)
	net.addLink(s36,s38)
	net.addLink(s39,s40)
	net.addLink(s39,s41)
	net.addLink(s42,s43)
	net.addLink(s42,s46)
	net.addLink(s43,s44)
	net.addLink(s43,s45)
	net.addLink(s46,s47)
	net.addLink(s46,s48)
	net.addLink(s49,s50)
	net.addLink(s49,s57)
	net.addLink(s50,s51)
	net.addLink(s50,s54)
	net.addLink(s51,s52)
	net.addLink(s51,s53)
	net.addLink(s54,s55)
	net.addLink(s54,s56)
	net.addLink(s57,s58)
	net.addLink(s57,s61)
	net.addLink(s58,s59)
	net.addLink(s58,s60)
	net.addLink(s61,s62)
	net.addLink(s61,s63)
	net.addLink(h1,s7)
	net.addLink(h2,s58)


	net.start()
	CLI( net )
	net.stop()
