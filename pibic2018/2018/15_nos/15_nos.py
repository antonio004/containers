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

    # Create Host Nodes

    h1 = dp.addNode(Host(name="h1", ip="10.0.0.1", mask="24"))
    h2 = dp.addNode(Host(name="h2", ip="10.0.0.2", mask="24"))

    # Adding links to dataplane

    l1 = dp.addLink(LinkPair(name="l1", node_source=sw1, node_target=sw2, type=LinkType.DIRECT))
    l2 = dp.addLink(LinkPair(name="l2", node_source=sw2, node_target=sw3, type=LinkType.DIRECT))
    l3 = dp.addLink(LinkPair(name="l3", node_source=sw3, node_target=sw4, type=LinkType.DIRECT))

    l4 = dp.addLink(LinkPair(name="l4", node_source=sw3, node_target=sw5, type=LinkType.DIRECT))
    l5 = dp.addLink(LinkPair(name="l5", node_source=sw2, node_target=sw6, type=LinkType.DIRECT))
    l6 = dp.addLink(LinkPair(name="l6", node_source=sw6, node_target=sw7, type=LinkType.DIRECT))
    l7 = dp.addLink(LinkPair(name="l7", node_source=sw6, node_target=sw8, type=LinkType.DIRECT))

    l8 = dp.addLink(LinkPair(name="l8", node_source=sw1, node_target=sw9, type=LinkType.DIRECT))
    l9 = dp.addLink(LinkPair(name="l9", node_source=sw9, node_target=sw10, type=LinkType.DIRECT))
    l10 = dp.addLink(LinkPair(name="l10", node_source=sw10, node_target=sw11, type=LinkType.DIRECT))
    l11 = dp.addLink(LinkPair(name="l11", node_source=sw10, node_target=sw12, type=LinkType.DIRECT))

    l12 = dp.addLink(LinkPair(name="l12", node_source=sw9, node_target=sw13, type=LinkType.DIRECT))
    l13 = dp.addLink(LinkPair(name="l13", node_source=sw13, node_target=sw14, type=LinkType.DIRECT))
    l14 = dp.addLink(LinkPair(name="l14", node_source=sw13, node_target=sw15, type=LinkType.DIRECT))


    hl1 = dp.addLink(LinkPair(name="hl1", node_source=h1, node_target=sw6, type=LinkType.HOST))
    hl2 = dp.addLink(LinkPair(name="hl2", node_source=h2, node_target=sw14, type=LinkType.HOST))

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

    cli = Cli(dp)
    cli.cmdloop()

    dp.stop()