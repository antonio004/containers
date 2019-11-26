#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info

if __name__ == '__main__':
	setLogLevel( 'info' )
	net = Mininet( controller=RemoteController )
	info( "Adicionando o IP do Controller SDN e a porta" )
	net.addController( 'c0',controller=RemoteController,ip='172.17.0.2',port=6653 )
	info( 'Add hosts\n' )
	h1 = net.addHost( 'h1', ip='10.0.0.1', netmask='255.255.255.0' )
	h2 = net.addHost( 'h2', ip='10.0.0.2', netmask='255.255.255.0' )

	info( 'Add switch\n' )
	aux1=256
	#result = random.sample(range(0,100), 4)
	for i in range(1, aux1):
	    locals()["s"+str(i)] = net.addSwitch("s"+str(i))

	info( 'Criando os links\n' )
    # Adding links to dataplane
	for i in range(1, (aux1-1)):
		net.addLink(s1,locals()["s"+str(i+1)])
        #locals()["hl"+str(i)] = net.addLink(name="hl"+str(i), node_source=locals()["sw1"], node_target=locals()["sw"+str(i+1)], type=LinkType.DIRECT))
	net.addLink( h1, s3 )
	net.addLink( h2, s7 )
	net.start()
	cli = CLI( net )
	cli.cmdloop()
	net.stop()
