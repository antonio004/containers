#!/usr/bin/python

from vsdnemul.dataplane import Dataplane
from vsdnemul.lib.log import get_logger
from vsdnemul.link import LinkType
from vsdnemul.models.link.linkpair import LinkPair
from vsdnemul.models.node.host.host import Host
from vsdnemul.models.node.switch.whitebox import Whitebox
from vsdnemul.models.node.controller.onos import Onos
from vsdnemul.cli import Cli



if __name__ == '__main__':

    logger = get_logger(__name__)

    dp = Dataplane()

    # Adding Controller
    controller = dp.addNode(Onos(name="controller"))
    mgnt = "tcp:{ip}:6653".format(ip=controller.getIpController())

    # add nodes, switches first...
    NewYork = dp.addNode(Whitebox(name='NewYork'))
    Chicago = dp.addNode(Whitebox(name='Chicago'))
    WashingtonDC = dp.addNode(Whitebox(name='WashingtonDC'))
    Seattle = dp.addNode(Whitebox(name='Seattle'))
    Sunnyvale = dp.addNode(Whitebox(name='Sunnyvale'))
    LosAngeles = dp.addNode(Whitebox(name='LosAngeles'))
    Denver = dp.addNode(Whitebox(name='Denver'))
    KansasCity = dp.addNode(Whitebox(name='KansasCity'))
    Houston = dp.addNode(Whitebox(name='Houston'))
    Atlanta = dp.addNode(Whitebox(name='Atlanta'))
    Indianapolis = dp.addNode(Whitebox(name='Indianapolis'))

    # ... and now hosts
    Host_NewYork = dp.addNode(Host(name='Host_NewYork', ip='10.0.0.1', mask='24'))
    Host_Chicago = dp.addNode(Host(name='Host_Chicago', ip='10.0.0.2', mask='24'))
    Host_WashingtonDC = dp.addNode(Host(name='Host_WashingtonDC', ip='10.0.0.3', mask='24'))
    Host_Seattle = dp.addNode(Host(name='Host_Seattle', ip='10.0.0.4', mask='24'))
    Host_Sunnyvale = dp.addNode(Host(name='Host_Sunnyvale', ip='10.0.0.5', mask='24'))
    Host_LosAngeles = dp.addNode(Host(name='Host_LosAngeles', ip='10.0.0.6', mask='24'))
    Host_Denver = dp.addNode(Host(name='Host_Denver', ip='10.0.0.7', mask='24'))
    Host_KansasCity = dp.addNode(Host(name='Host_KansasCity', ip='10.0.0.8', mask='24'))
    Host_Houston = dp.addNode(Host(name='Host_Houston', ip='10.0.0.9', mask='24'))
    Host_Atlanta = dp.addNode(Host(name='Host_Atlanta', ip='10.0.0.10', mask='24'))
    Host_Indianapolis = dp.addNode(Host(name='Host_Indianapolis', ip='10.0.0.11', mask='24'))

    # add edges between switch and corresponding host
    link_host0 = dp.addLink(LinkPair(name='link_host0', node_source=NewYork , node_target= Host_NewYork , type=LinkType.HOST))
    link_host1 = dp.addLink(LinkPair(name='link_host1', node_source=Chicago , node_target= Host_Chicago , type=LinkType.HOST))
    link_host2 = dp.addLink(LinkPair(name='link_host2', node_source=WashingtonDC , node_target= Host_WashingtonDC , type=LinkType.HOST))
    link_host3 = dp.addLink(LinkPair(name='link_host3', node_source=Seattle , node_target= Host_Seattle , type=LinkType.HOST))
    link_host4 = dp.addLink(LinkPair(name='link_host4', node_source=Sunnyvale , node_target= Host_Sunnyvale , type=LinkType.HOST))
    link_host5 = dp.addLink(LinkPair(name='link_host5', node_source=LosAngeles , node_target= Host_LosAngeles , type=LinkType.HOST))
    link_host6 = dp.addLink(LinkPair(name='link_host6', node_source=Denver , node_target= Host_Denver , type=LinkType.HOST))
    link_host7 = dp.addLink(LinkPair(name='link_host7', node_source=KansasCity , node_target= Host_KansasCity , type=LinkType.HOST))
    link_host8 = dp.addLink(LinkPair(name='link_host8', node_source=Houston , node_target= Host_Houston , type=LinkType.HOST))
    link_host9 = dp.addLink(LinkPair(name='link_host9', node_source=Atlanta , node_target= Host_Atlanta , type=LinkType.HOST))
    link_host10 = dp.addLink(LinkPair(name='link_host10', node_source=Indianapolis , node_target= Host_Indianapolis , type=LinkType.HOST))

    # add edges between switches
    link_wh0 = dp.addLink(LinkPair(name='link_wh0', node_source=NewYork , node_target=Chicago , type=LinkType.dIRECT))
    link_wh1 = dp.addLink(LinkPair(name='link_wh1', node_source=NewYork , node_target=WashingtonDC , type=LinkType.dIRECT))
    link_wh2 = dp.addLink(LinkPair(name='link_wh2', node_source=Chicago , node_target=Indianapolis , type=LinkType.dIRECT))
    link_wh3 = dp.addLink(LinkPair(name='link_wh3', node_source=WashingtonDC , node_target=Atlanta , type=LinkType.dIRECT))
    link_wh4 = dp.addLink(LinkPair(name='link_wh4', node_source=Seattle , node_target=Sunnyvale , type=LinkType.dIRECT))
    link_wh5 = dp.addLink(LinkPair(name='link_wh5', node_source=Seattle , node_target=Denver , type=LinkType.dIRECT))
    link_wh6 = dp.addLink(LinkPair(name='link_wh6', node_source=Sunnyvale , node_target=LosAngeles , type=LinkType.dIRECT))
    link_wh7 = dp.addLink(LinkPair(name='link_wh7', node_source=Sunnyvale , node_target=Denver , type=LinkType.dIRECT))
    link_wh8 = dp.addLink(LinkPair(name='link_wh8', node_source=LosAngeles , node_target=Houston , type=LinkType.dIRECT))
    link_wh9 = dp.addLink(LinkPair(name='link_wh9', node_source=Denver , node_target=KansasCity , type=LinkType.dIRECT))
    link_wh10 = dp.addLink(LinkPair(name='link_wh10', node_source=KansasCity , node_target=Houston , type=LinkType.dIRECT))
    link_wh11 = dp.addLink(LinkPair(name='link_wh11', node_source=KansasCity , node_target=Indianapolis , type=LinkType.dIRECT))
    link_wh12 = dp.addLink(LinkPair(name='link_wh12', node_source=Houston , node_target=Atlanta , type=LinkType.dIRECT))
    link_wh13 = dp.addLink(LinkPair(name='link_wh13', node_source=Atlanta , node_target=Indianapolis , type=LinkType.dIRECT))

    # Connecting Switchs on Controller
    NewYork.setController(target=mgnt, bridge='br_oper0')
    Chicago.setController(target=mgnt, bridge='br_oper0')
    WashingtonDC.setController(target=mgnt, bridge='br_oper0')
    Seattle.setController(target=mgnt, bridge='br_oper0')
    Sunnyvale.setController(target=mgnt, bridge='br_oper0')
    LosAngeles.setController(target=mgnt, bridge='br_oper0')
    Denver.setController(target=mgnt, bridge='br_oper0')
    KansasCity.setController(target=mgnt, bridge='br_oper0')
    Houston.setController(target=mgnt, bridge='br_oper0')
    Atlanta.setController(target=mgnt, bridge='br_oper0')
    Indianapolis.setController(target=mgnt, bridge='br_oper0')

    #showing cli interface
    cli = Cli(dp)
    cli.cmdloop()

    #stop and close all nodes
    dp.stop()
