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
    sw32 = dp.addNode(Whitebox("sw32"))
    sw33 = dp.addNode(Whitebox("sw33"))
    sw34 = dp.addNode(Whitebox("sw34"))
    sw35 = dp.addNode(Whitebox("sw35"))
    sw36 = dp.addNode(Whitebox("sw36"))
    sw37 = dp.addNode(Whitebox("sw37"))
    sw38 = dp.addNode(Whitebox("sw38"))
    sw39 = dp.addNode(Whitebox("sw39"))
    sw40 = dp.addNode(Whitebox("sw40"))
    sw41 = dp.addNode(Whitebox("sw41"))
    sw42 = dp.addNode(Whitebox("sw42"))
    sw43 = dp.addNode(Whitebox("sw43"))
    sw44 = dp.addNode(Whitebox("sw44"))
    sw45 = dp.addNode(Whitebox("sw45"))
    sw46 = dp.addNode(Whitebox("sw46"))
    sw47 = dp.addNode(Whitebox("sw47"))
    sw48 = dp.addNode(Whitebox("sw48"))
    sw49 = dp.addNode(Whitebox("sw49"))
    sw50 = dp.addNode(Whitebox("sw50"))
    sw51 = dp.addNode(Whitebox("sw51"))
    sw52 = dp.addNode(Whitebox("sw52"))
    sw53 = dp.addNode(Whitebox("sw53"))
    sw54 = dp.addNode(Whitebox("sw54"))
    sw55 = dp.addNode(Whitebox("sw55"))
    sw56 = dp.addNode(Whitebox("sw56"))
    sw57 = dp.addNode(Whitebox("sw57"))
    sw58 = dp.addNode(Whitebox("sw58"))
    sw59 = dp.addNode(Whitebox("sw59"))
    sw60 = dp.addNode(Whitebox("sw60"))
    sw61 = dp.addNode(Whitebox("sw61"))
    sw62 = dp.addNode(Whitebox("sw62"))
    sw63 = dp.addNode(Whitebox("sw63"))
    sw64 = dp.addNode(Whitebox("sw64"))
    # Create Host Nodes

    h1 = dp.addNode(Host(name="h1", ip="10.0.0.1", mask="24"))
    h2 = dp.addNode(Host(name="h2", ip="10.0.0.2", mask="24"))

    # Adding links to dataplane

    l1 = dp.addLink(LinkPair(name="l1", node_source=sw1, node_target=sw2, type=LinkType.DIRECT))
    l2 = dp.addLink(LinkPair(name="l2", node_source=sw1, node_target=sw33, type=LinkType.DIRECT))
    l3 = dp.addLink(LinkPair(name="l3", node_source=sw2, node_target=sw3, type=LinkType.DIRECT))
    l4 = dp.addLink(LinkPair(name="l4", node_source=sw2, node_target=sw18, type=LinkType.DIRECT))
    l5 = dp.addLink(LinkPair(name="l5", node_source=sw3, node_target=sw4, type=LinkType.DIRECT))
    
    l6 = dp.addLink(LinkPair(name="l6", node_source=sw3, node_target=sw11, type=LinkType.DIRECT))
    l7 = dp.addLink(LinkPair(name="l7", node_source=sw4, node_target=sw5, type=LinkType.DIRECT))
    l8 = dp.addLink(LinkPair(name="l8", node_source=sw4, node_target=sw8, type=LinkType.DIRECT))
    
    l9 = dp.addLink(LinkPair(name="l9", node_source=sw5, node_target=sw6, type=LinkType.DIRECT))
    l10 = dp.addLink(LinkPair(name="l10", node_source=sw5, node_target=sw7, type=LinkType.DIRECT))
    l11 = dp.addLink(LinkPair(name="l11", node_source=sw8, node_target=sw9, type=LinkType.DIRECT))
    l12 = dp.addLink(LinkPair(name="l12", node_source=sw8, node_target=sw10, type=LinkType.DIRECT))
    l13 = dp.addLink(LinkPair(name="l13", node_source=sw11, node_target=sw12, type=LinkType.DIRECT))
    l14 = dp.addLink(LinkPair(name="l14", node_source=sw11, node_target=sw15, type=LinkType.DIRECT))
    l15 = dp.addLink(LinkPair(name="l15", node_source=sw12, node_target=sw13, type=LinkType.DIRECT))

    l16 = dp.addLink(LinkPair(name="l16", node_source=sw12, node_target=sw14, type=LinkType.DIRECT))
    l17 = dp.addLink(LinkPair(name="l17", node_source=sw15, node_target=sw16, type=LinkType.DIRECT))
    l18 = dp.addLink(LinkPair(name="l18", node_source=sw15, node_target=sw17, type=LinkType.DIRECT))
    l19 = dp.addLink(LinkPair(name="l19", node_source=sw18, node_target=sw19, type=LinkType.DIRECT))
    l20 = dp.addLink(LinkPair(name="l20", node_source=sw18, node_target=sw26, type=LinkType.DIRECT))
    l21 = dp.addLink(LinkPair(name="l21", node_source=sw19, node_target=sw20, type=LinkType.DIRECT))
    l22 = dp.addLink(LinkPair(name="l22", node_source=sw19, node_target=sw23, type=LinkType.DIRECT))
    l23 = dp.addLink(LinkPair(name="l23", node_source=sw20, node_target=sw21, type=LinkType.DIRECT))

    l24 = dp.addLink(LinkPair(name="l24", node_source=sw20, node_target=sw22, type=LinkType.DIRECT))
    l25 = dp.addLink(LinkPair(name="l25", node_source=sw23, node_target=sw24, type=LinkType.DIRECT))
    l26 = dp.addLink(LinkPair(name="l26", node_source=sw23, node_target=sw25, type=LinkType.DIRECT))
    l27 = dp.addLink(LinkPair(name="l27", node_source=sw26, node_target=sw27, type=LinkType.DIRECT))
    l28 = dp.addLink(LinkPair(name="l28", node_source=sw26, node_target=sw30, type=LinkType.DIRECT))
    l29 = dp.addLink(LinkPair(name="l29", node_source=sw27, node_target=sw28, type=LinkType.DIRECT))
    l30 = dp.addLink(LinkPair(name="l30", node_source=sw27, node_target=sw29, type=LinkType.DIRECT))
    
    l31 = dp.addLink(LinkPair(name="l31", node_source=sw30, node_target=sw31, type=LinkType.DIRECT))
    l32 = dp.addLink(LinkPair(name="l32", node_source=sw30, node_target=sw32, type=LinkType.DIRECT))
    l33 = dp.addLink(LinkPair(name="l33", node_source=sw33, node_target=sw34, type=LinkType.DIRECT))
    l34 = dp.addLink(LinkPair(name="l34", node_source=sw33, node_target=sw49, type=LinkType.DIRECT))
    l35 = dp.addLink(LinkPair(name="l35", node_source=sw34, node_target=sw35, type=LinkType.DIRECT))
    l36 = dp.addLink(LinkPair(name="l36", node_source=sw34, node_target=sw42, type=LinkType.DIRECT))
    l37 = dp.addLink(LinkPair(name="l37", node_source=sw35, node_target=sw36, type=LinkType.DIRECT))
    l38 = dp.addLink(LinkPair(name="l38", node_source=sw35, node_target=sw39, type=LinkType.DIRECT))
    l39 = dp.addLink(LinkPair(name="l39", node_source=sw36, node_target=sw37, type=LinkType.DIRECT))
    l40 = dp.addLink(LinkPair(name="l40", node_source=sw36, node_target=sw38, type=LinkType.DIRECT))
    l41 = dp.addLink(LinkPair(name="l41", node_source=sw39, node_target=sw40, type=LinkType.DIRECT))
    l42 = dp.addLink(LinkPair(name="l42", node_source=sw39, node_target=sw41, type=LinkType.DIRECT))
    l43 = dp.addLink(LinkPair(name="l43", node_source=sw42, node_target=sw43, type=LinkType.DIRECT))
    l44 = dp.addLink(LinkPair(name="l44", node_source=sw42, node_target=sw46, type=LinkType.DIRECT))
    l45 = dp.addLink(LinkPair(name="l45", node_source=sw43, node_target=sw44, type=LinkType.DIRECT))
    l46 = dp.addLink(LinkPair(name="l46", node_source=sw43, node_target=sw45, type=LinkType.DIRECT))
    l47 = dp.addLink(LinkPair(name="l47", node_source=sw46, node_target=sw47, type=LinkType.DIRECT))
    l48 = dp.addLink(LinkPair(name="l48", node_source=sw46, node_target=sw48, type=LinkType.DIRECT))
    l49 = dp.addLink(LinkPair(name="l49", node_source=sw49, node_target=sw50, type=LinkType.DIRECT))
    l50 = dp.addLink(LinkPair(name="l50", node_source=sw49, node_target=sw57, type=LinkType.DIRECT))
    l51 = dp.addLink(LinkPair(name="l51", node_source=sw50, node_target=sw51, type=LinkType.DIRECT))
    l52 = dp.addLink(LinkPair(name="l52", node_source=sw50, node_target=sw54, type=LinkType.DIRECT))
    l53 = dp.addLink(LinkPair(name="l53", node_source=sw51, node_target=sw52, type=LinkType.DIRECT))
    l54 = dp.addLink(LinkPair(name="l54", node_source=sw51, node_target=sw53, type=LinkType.DIRECT))
    l55 = dp.addLink(LinkPair(name="l55", node_source=sw54, node_target=sw55, type=LinkType.DIRECT))
    l56 = dp.addLink(LinkPair(name="l56", node_source=sw54, node_target=sw56, type=LinkType.DIRECT))
    l57 = dp.addLink(LinkPair(name="l57", node_source=sw57, node_target=sw58, type=LinkType.DIRECT))
    l58 = dp.addLink(LinkPair(name="l58", node_source=sw57, node_target=sw61, type=LinkType.DIRECT))
    l59 = dp.addLink(LinkPair(name="l59", node_source=sw58, node_target=sw59, type=LinkType.DIRECT))
    l60 = dp.addLink(LinkPair(name="l60", node_source=sw58, node_target=sw60, type=LinkType.DIRECT))
    l61 = dp.addLink(LinkPair(name="l61", node_source=sw61, node_target=sw62, type=LinkType.DIRECT))
    l62 = dp.addLink(LinkPair(name="l62", node_source=sw61, node_target=sw63, type=LinkType.DIRECT))

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
    sw32.setController(target=mgnt, bridge="br_oper0")
    sw33.setController(target=mgnt, bridge="br_oper0")
    sw34.setController(target=mgnt, bridge="br_oper0")
    sw35.setController(target=mgnt, bridge="br_oper0")
    sw36.setController(target=mgnt, bridge="br_oper0")
    sw37.setController(target=mgnt, bridge="br_oper0")
    sw38.setController(target=mgnt, bridge="br_oper0")
    sw39.setController(target=mgnt, bridge="br_oper0")
    sw40.setController(target=mgnt, bridge="br_oper0")
    sw41.setController(target=mgnt, bridge="br_oper0")
    sw42.setController(target=mgnt, bridge="br_oper0")
    sw43.setController(target=mgnt, bridge="br_oper0")
    sw44.setController(target=mgnt, bridge="br_oper0")
    sw45.setController(target=mgnt, bridge="br_oper0")
    sw46.setController(target=mgnt, bridge="br_oper0")
    sw47.setController(target=mgnt, bridge="br_oper0")
    sw48.setController(target=mgnt, bridge="br_oper0")
    sw49.setController(target=mgnt, bridge="br_oper0")
    sw50.setController(target=mgnt, bridge="br_oper0")
    sw51.setController(target=mgnt, bridge="br_oper0")
    sw52.setController(target=mgnt, bridge="br_oper0")
    sw53.setController(target=mgnt, bridge="br_oper0")
    sw54.setController(target=mgnt, bridge="br_oper0")
    sw55.setController(target=mgnt, bridge="br_oper0")
    sw56.setController(target=mgnt, bridge="br_oper0")
    sw57.setController(target=mgnt, bridge="br_oper0")
    sw58.setController(target=mgnt, bridge="br_oper0")
    sw59.setController(target=mgnt, bridge="br_oper0")
    sw60.setController(target=mgnt, bridge="br_oper0")
    sw61.setController(target=mgnt, bridge="br_oper0")
    sw62.setController(target=mgnt, bridge="br_oper0")
    sw63.setController(target=mgnt, bridge="br_oper0")
    sw64.setController(target=mgnt, bridge="br_oper0")



    cli = Cli(dp)
    cli.cmdloop()
