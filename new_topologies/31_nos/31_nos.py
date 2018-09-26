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

    # Define Dataplane

    dp = Dataplane()

    # Adding nodes to dataplane
    # Create Switch Nodes

    sw1 = dp.addNode(Whitebox("sw1"))
    sw2 = dp.addNode(Whitebox("sw2"))
    sw3 = dp.addNode(Whitebox("sw3"))
    sw4 = dp.addNode(Whitebox("sw4"))
    sw5 = dp.addNode(Whitebox("sw5"))
    sw6 = dp.addNode(Whitebox("sw6"))
    sw7 = dp.addNode(Whitebox("sw7"))
    sw8 = dp.addNode(Whitebox("sw8"))
    sw9 = dp.addNode(Whitebox("sw9"))
    sw10 = dp.addNode(Whitebox("sw10"))
    sw11 = dp.addNode(Whitebox("sw11"))
    sw12 = dp.addNode(Whitebox("sw12"))
    sw13 = dp.addNode(Whitebox("sw13"))
    sw14 = dp.addNode(Whitebox("sw14"))
    sw15 = dp.addNode(Whitebox("sw15"))
    sw16 = dp.addNode(Whitebox("sw16"))
    sw17 = dp.addNode(Whitebox("sw17"))
    sw18 = dp.addNode(Whitebox("sw18"))
    sw19 = dp.addNode(Whitebox("sw19"))
    sw20 = dp.addNode(Whitebox("sw20"))
    sw21 = dp.addNode(Whitebox("sw21"))
    sw22 = dp.addNode(Whitebox("sw22"))
    sw23 = dp.addNode(Whitebox("sw23"))
    sw24 = dp.addNode(Whitebox("sw24"))
    sw25 = dp.addNode(Whitebox("sw25"))
    sw26 = dp.addNode(Whitebox("sw26"))
    sw27 = dp.addNode(Whitebox("sw27"))
    sw28 = dp.addNode(Whitebox("sw28"))
    sw29 = dp.addNode(Whitebox("sw29"))
    sw30 = dp.addNode(Whitebox("sw30"))
    sw31 = dp.addNode(Whitebox("sw31"))

    # Create Host Nodes

    h1 = dp.addNode(Host(name="h1", ip="10.0.0.1", mask="24"))
    h2 = dp.addNode(Host(name="h2", ip="10.0.0.2", mask="24"))

    # Adding links to dataplane

    l1 = dp.addLink(LinkPair(name="l1", node_source=sw1, node_target=sw2, type=LinkType.DIRECT))
    l2 = dp.addLink(LinkPair(name="l2", node_source=sw2, node_target=sw3, type=LinkType.DIRECT))
    l3 = dp.addLink(LinkPair(name="l3", node_source=sw3, node_target=sw4, type=LinkType.DIRECT))
    l4 = dp.addLink(LinkPair(name="l4", node_source=sw4, node_target=sw5, type=LinkType.DIRECT))
    l5 = dp.addLink(LinkPair(name="l5", node_source=sw4, node_target=sw6, type=LinkType.DIRECT))
    
    l6 = dp.addLink(LinkPair(name="l6", node_source=sw3, node_target=sw7, type=LinkType.DIRECT))
    l7 = dp.addLink(LinkPair(name="l7", node_source=sw7, node_target=sw8, type=LinkType.DIRECT))
    l8 = dp.addLink(LinkPair(name="l8", node_source=sw7, node_target=sw9, type=LinkType.DIRECT))
    
    l9 = dp.addLink(LinkPair(name="l9", node_source=sw2, node_target=sw10, type=LinkType.DIRECT))
    l10 = dp.addLink(LinkPair(name="l10", node_source=sw10, node_target=sw11, type=LinkType.DIRECT))
    l11 = dp.addLink(LinkPair(name="l11", node_source=sw11, node_target=sw12, type=LinkType.DIRECT))
    l12 = dp.addLink(LinkPair(name="l12", node_source=sw11, node_target=sw13, type=LinkType.DIRECT))
    l13 = dp.addLink(LinkPair(name="l13", node_source=sw10, node_target=sw14, type=LinkType.DIRECT))
    l14 = dp.addLink(LinkPair(name="l14", node_source=sw14, node_target=sw15, type=LinkType.DIRECT))
    l15 = dp.addLink(LinkPair(name="l15", node_source=sw14, node_target=sw16, type=LinkType.DIRECT))

    l16 = dp.addLink(LinkPair(name="l16", node_source=sw1, node_target=sw17, type=LinkType.DIRECT))
    l17 = dp.addLink(LinkPair(name="l17", node_source=sw17, node_target=sw18, type=LinkType.DIRECT))
    l18 = dp.addLink(LinkPair(name="l18", node_source=sw18, node_target=sw19, type=LinkType.DIRECT))
    l19 = dp.addLink(LinkPair(name="l19", node_source=sw19, node_target=sw20, type=LinkType.DIRECT))
    l20 = dp.addLink(LinkPair(name="l20", node_source=sw19, node_target=sw21, type=LinkType.DIRECT))
    l21 = dp.addLink(LinkPair(name="l21", node_source=sw18, node_target=sw22, type=LinkType.DIRECT))
    l22 = dp.addLink(LinkPair(name="l22", node_source=sw22, node_target=sw23, type=LinkType.DIRECT))
    l23 = dp.addLink(LinkPair(name="l23", node_source=sw22, node_target=sw24, type=LinkType.DIRECT))

    l24 = dp.addLink(LinkPair(name="l24", node_source=sw17, node_target=sw25, type=LinkType.DIRECT))
    l25 = dp.addLink(LinkPair(name="l25", node_source=sw25, node_target=sw26, type=LinkType.DIRECT))
    l26 = dp.addLink(LinkPair(name="l26", node_source=sw26, node_target=sw27, type=LinkType.DIRECT))
    l27 = dp.addLink(LinkPair(name="l27", node_source=sw26, node_target=sw28, type=LinkType.DIRECT))
    l28 = dp.addLink(LinkPair(name="l28", node_source=sw25, node_target=sw29, type=LinkType.DIRECT))
    l29 = dp.addLink(LinkPair(name="l29", node_source=sw29, node_target=sw30, type=LinkType.DIRECT))
    l30 = dp.addLink(LinkPair(name="l30", node_source=sw29, node_target=sw31, type=LinkType.DIRECT))


    hl1 = dp.addLink(LinkPair(name="hl1", node_source=h1, node_target=sw4, type=LinkType.HOST))
    hl2 = dp.addLink(LinkPair(name="hl2", node_source=h2, node_target=sw30, type=LinkType.HOST))

    # Adding Controller

    ctl = dp.addNode(Onos(name="ctl1"))
    mgnt = "tcp:{ip}:6653".format(ip=ctl.getIpController())

    sw1.setController(target=mgnt, bridge="br_oper0")
    sw2.setController(target=mgnt, bridge="br_oper0")
    sw3.setController(target=mgnt, bridge="br_oper0")
    sw4.setController(target=mgnt, bridge="br_oper0")
    sw5.setController(target=mgnt, bridge="br_oper0")
    sw6.setController(target=mgnt, bridge="br_oper0")
    sw7.setController(target=mgnt, bridge="br_oper0")
    sw8.setController(target=mgnt, bridge="br_oper0")
    sw9.setController(target=mgnt, bridge="br_oper0")
    sw10.setController(target=mgnt, bridge="br_oper0")
    sw11.setController(target=mgnt, bridge="br_oper0")
    sw12.setController(target=mgnt, bridge="br_oper0")
    sw13.setController(target=mgnt, bridge="br_oper0")
    sw14.setController(target=mgnt, bridge="br_oper0")
    sw15.setController(target=mgnt, bridge="br_oper0")
    sw16.setController(target=mgnt, bridge="br_oper0")
    sw17.setController(target=mgnt, bridge="br_oper0")
    sw18.setController(target=mgnt, bridge="br_oper0")
    sw19.setController(target=mgnt, bridge="br_oper0")
    sw20.setController(target=mgnt, bridge="br_oper0")
    sw21.setController(target=mgnt, bridge="br_oper0")
    sw22.setController(target=mgnt, bridge="br_oper0")
    sw23.setController(target=mgnt, bridge="br_oper0")
    sw24.setController(target=mgnt, bridge="br_oper0")
    sw25.setController(target=mgnt, bridge="br_oper0")
    sw26.setController(target=mgnt, bridge="br_oper0")
    sw27.setController(target=mgnt, bridge="br_oper0")
    sw28.setController(target=mgnt, bridge="br_oper0")
    sw29.setController(target=mgnt, bridge="br_oper0")
    sw30.setController(target=mgnt, bridge="br_oper0")
    sw31.setController(target=mgnt, bridge="br_oper0")


    cli = Cli(dp)
    cli.cmdloop()

    dp.stop()