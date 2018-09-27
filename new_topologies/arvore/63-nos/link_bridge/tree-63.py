#!/usr/bin/env python3
from vsdnemu.api.dataplane.dataplaneapi import Dataplane
from vsdnemu.api.log.logapi import get_logger
from vsdnemu.api.node.nodeapi import NodeType
from vsdnemu.frontend.cli import Prompt
from vsdnemu.link.veth_link import HostLinkVeth, DirectLinkVeth
from vsdnemu.link.bridge_link import HostLinkBridge, DirectLinkBridge
from vsdnemu.node.host_node import Host
from vsdnemu.node.onos_node import Onos
from vsdnemu.node.whitebox_node import WhiteBox

logger = get_logger("topology.script")


def Topology():

    n1 = WhiteBox(name = "node1")
    n2 = WhiteBox(name = "node2")
    n3 = WhiteBox(name = "node3")
    n4 = WhiteBox(name = "node4")
    n5 = WhiteBox(name = "node5")
    n6 = WhiteBox(name = "node6")
    n7 = WhiteBox(name = "node7")
    n8 = WhiteBox(name = "node8")
    n9 = WhiteBox(name = "node9")
    n10 = WhiteBox(name = "node10")
    n11 = WhiteBox(name = "node11")
    n12 = WhiteBox(name = "node12")
    n13 = WhiteBox(name = "node13")
    n14 = WhiteBox(name = "node14")
    n15 = WhiteBox(name = "node15")
    n16 = WhiteBox(name = "node16")
    n17 = WhiteBox(name = "node17")
    n18 = WhiteBox(name = "node18")
    n19 = WhiteBox(name = "node19")
    n20 = WhiteBox(name = "node20")
    n21 = WhiteBox(name = "node21")
    n22 = WhiteBox(name = "node22")
    n23 = WhiteBox(name = "node23")
    n24 = WhiteBox(name = "node24")
    n25 = WhiteBox(name = "node25")
    n26 = WhiteBox(name = "node26")
    n27 = WhiteBox(name = "node27")
    n28 = WhiteBox(name = "node28")
    n29 = WhiteBox(name = "node29")
    n30 = WhiteBox(name = "node30")
    n31 = WhiteBox(name = "node31")
    n32 = WhiteBox(name = "node32")
    n33 = WhiteBox(name = "node33")
    n34 = WhiteBox(name = "node34")
    n35 = WhiteBox(name = "node35")
    n36 = WhiteBox(name = "node36")
    n37 = WhiteBox(name = "node37")
    n38 = WhiteBox(name = "node38")
    n39 = WhiteBox(name = "node39")
    n40 = WhiteBox(name = "node40")
    n41 = WhiteBox(name = "node41")
    n42 = WhiteBox(name = "node42")
    n43 = WhiteBox(name = "node43")
    n44 = WhiteBox(name = "node44")
    n45 = WhiteBox(name = "node45")
    n46 = WhiteBox(name = "node46")
    n47 = WhiteBox(name = "node47")
    n48 = WhiteBox(name = "node48")
    n49 = WhiteBox(name = "node49")
    n50 = WhiteBox(name = "node50")
    n51 = WhiteBox(name = "node51")
    n52 = WhiteBox(name = "node52")
    n53 = WhiteBox(name = "node53")
    n54 = WhiteBox(name = "node54")
    n55 = WhiteBox(name = "node55")
    n56 = WhiteBox(name = "node56")
    n57 = WhiteBox(name = "node57")
    n58 = WhiteBox(name = "node58")
    n59 = WhiteBox(name = "node59")
    n60 = WhiteBox(name = "node60")
    n61 = WhiteBox(name = "node61")
    n62 = WhiteBox(name = "node62")
    n63 = WhiteBox(name = "node63")

    ctl1 = Onos(name = "control1")

    h1 = Host(name = "host1")
    h2 = Host(name = "host2")

    link1 = HostLinkBridge(node_host = h1, node_target = n5, ip_host = "10.0.0.1/24", mtu = "9000")
    link2 = HostLinkBridge(node_host = h2, node_target = n24, ip_host = "10.0.0.2/24", mtu = "9000")
    

    link3 = DirectLinkBridge(node_source = n1, node_target = n2, mtu = "9000")
    link4 = DirectLinkBridge(node_source = n2, node_target = n3, mtu = "9000")
    link5 = DirectLinkBridge(node_source = n3, node_target = n4, mtu = "9000")
    link6 = DirectLinkBridge(node_source = n4, node_target = n5, mtu = "9000")
    link7 = DirectLinkBridge(node_source = n5, node_target = n6, mtu = "9000")
    link8 = DirectLinkBridge(node_source = n5, node_target = n7, mtu = "9000")
    link9 = DirectLinkBridge(node_source = n4, node_target = n8, mtu = "9000")
    link10 = DirectLinkBridge(node_source = n8, node_target = n9, mtu = "9000")
    link11 = DirectLinkBridge(node_source = n8, node_target = n10, mtu = "9000")
    

    link12 = DirectLinkBridge(node_source = n3, node_target = n11, mtu = "9000")
    link13 = DirectLinkBridge(node_source = n11, node_target = n12, mtu = "9000")
    link14 = DirectLinkBridge(node_source = n12, node_target = n13, mtu = "9000")
    link15 = DirectLinkBridge(node_source = n12, node_target = n14, mtu = "9000")
    link16 = DirectLinkBridge(node_source = n11, node_target = n15, mtu = "9000")
    link17 = DirectLinkBridge(node_source = n15, node_target = n16, mtu = "9000")
    link18 = DirectLinkBridge(node_source = n15, node_target = n17, mtu = "9000")
    

    link19 = DirectLinkBridge(node_source = n2, node_target = n18, mtu = "9000")
    link20 = DirectLinkBridge(node_source = n18, node_target = n19, mtu = "9000")
    link21 = DirectLinkBridge(node_source = n19, node_target = n20, mtu = "9000")
    link22 = DirectLinkBridge(node_source = n19, node_target = n21, mtu = "9000")
    link23 = DirectLinkBridge(node_source = n18, node_target = n22, mtu = "9000")
    link24 = DirectLinkBridge(node_source = n22, node_target = n23, mtu = "9000")
    link25 = DirectLinkBridge(node_source = n22, node_target = n24, mtu = "9000")
    


    link26 = DirectLinkBridge(node_source = n1, node_target = n25, mtu = "9000")
    link27 = DirectLinkBridge(node_source = n25, node_target = n26, mtu = "9000")
    link28 = DirectLinkBridge(node_source = n26, node_target = n27, mtu = "9000")
    link29 = DirectLinkBridge(node_source = n27, node_target = n28, mtu = "9000")
    link30 = DirectLinkBridge(node_source = n28, node_target = n29, mtu = "9000")
    link31 = DirectLinkBridge(node_source = n28, node_target = n30, mtu = "9000")
    link32 = DirectLinkBridge(node_source = n27, node_target = n31, mtu = "9000")
    link33 = DirectLinkBridge(node_source = n31, node_target = n32, mtu = "9000")
    link34 = DirectLinkBridge(node_source = n31, node_target = n33, mtu = "9000")


    link35 = DirectLinkBridge(node_source = n26, node_target = n34, mtu = "9000")
    link36 = DirectLinkBridge(node_source = n34, node_target = n35, mtu = "9000")
    link37 = DirectLinkBridge(node_source = n35, node_target = n36, mtu = "9000")
    link38 = DirectLinkBridge(node_source = n35, node_target = n37, mtu = "9000")
    link39 = DirectLinkBridge(node_source = n34, node_target = n38, mtu = "9000")
    link40 = DirectLinkBridge(node_source = n38, node_target = n39, mtu = "9000")
    link41 = DirectLinkBridge(node_source = n38, node_target = n40, mtu = "9000")


    link42 = DirectLinkBridge(node_source = n25, node_target = n41, mtu = "9000")
    link43 = DirectLinkBridge(node_source = n41, node_target = n42, mtu = "9000")
    link44 = DirectLinkBridge(node_source = n42, node_target = n43, mtu = "9000")
    link45 = DirectLinkBridge(node_source = n43, node_target = n44, mtu = "9000")
    link46 = DirectLinkBridge(node_source = n43, node_target = n45, mtu = "9000")
    link47 = DirectLinkBridge(node_source = n42, node_target = n46, mtu = "9000")
    link48 = DirectLinkBridge(node_source = n46, node_target = n47, mtu = "9000")
    link49 = DirectLinkBridge(node_source = n46, node_target = n48, mtu = "9000")


    link50 = DirectLinkBridge(node_source = n41, node_target = n49, mtu = "9000")
    link51 = DirectLinkBridge(node_source = n49, node_target = n50, mtu = "9000")
    link52 = DirectLinkBridge(node_source = n50, node_target = n51, mtu = "9000")
    link53 = DirectLinkBridge(node_source = n50, node_target = n52, mtu = "9000")
    link54 = DirectLinkBridge(node_source = n49, node_target = n53, mtu = "9000")
    link55 = DirectLinkBridge(node_source = n53, node_target = n54, mtu = "9000")
    link56 = DirectLinkBridge(node_source = n53, node_target = n55, mtu = "9000")

    link57 = DirectLinkBridge(node_source = n20, node_target = n56, mtu = "9000")
    link58 = DirectLinkBridge(node_source = n20, node_target = n57, mtu = "9000")
    link59 = DirectLinkBridge(node_source = n21, node_target = n58, mtu = "9000")
    link60 = DirectLinkBridge(node_source = n21, node_target = n59, mtu = "9000")
    link61 = DirectLinkBridge(node_source = n23, node_target = n60, mtu = "9000")
    link62 = DirectLinkBridge(node_source = n23, node_target = n61, mtu = "9000")
    link63 = DirectLinkBridge(node_source = n24, node_target = n62, mtu = "9000")
    link64 = DirectLinkBridge(node_source = n24, node_target = n63, mtu = "9000")







    data = Dataplane()
    data.add_link(link1)
    data.add_link(link2)
    data.add_link(link3)
    data.add_link(link4)
    data.add_link(link5)
    data.add_link(link6)
    data.add_link(link7)
    data.add_link(link8)
    data.add_link(link9)
    data.add_link(link10)
    data.add_link(link11)
    data.add_link(link12)
    data.add_link(link13)
    data.add_link(link14)
    data.add_link(link15)
    data.add_link(link16)
    data.add_link(link17)
    data.add_link(link18)
    data.add_link(link19)
    data.add_link(link20)
    data.add_link(link21)
    data.add_link(link22)
    data.add_link(link23)
    data.add_link(link24)
    data.add_link(link25)
    data.add_link(link26)
    data.add_link(link27)
    data.add_link(link28)
    data.add_link(link29)
    data.add_link(link30)
    data.add_link(link31)
    data.add_link(link32)
    data.add_link(link33)
    data.add_link(link34)
    data.add_link(link35)
    data.add_link(link36)
    data.add_link(link37)
    data.add_link(link38)
    data.add_link(link39)
    data.add_link(link40)
    data.add_link(link41)
    data.add_link(link42)
    data.add_link(link43)
    data.add_link(link44)
    data.add_link(link45)
    data.add_link(link46)
    data.add_link(link47)
    data.add_link(link48)
    data.add_link(link48)
    data.add_link(link50)
    data.add_link(link51)
    data.add_link(link52)
    data.add_link(link53)
    data.add_link(link54)
    data.add_link(link55)
    data.add_link(link56)
    data.add_link(link57)
    data.add_link(link58)
    data.add_link(link59)
    data.add_link(link60)
    data.add_link(link61)
    data.add_link(link62)
    data.add_link(link63)
    data.add_link(link64)


    data.add_node(n1)
    data.add_node(n2)
    data.add_node(n3)
    data.add_node(n4)
    data.add_node(n5)
    data.add_node(n6)
    data.add_node(n7)
    data.add_node(n8)
    data.add_node(n9)
    data.add_node(n10)
    data.add_node(n11)
    data.add_node(n12)
    data.add_node(n13)
    data.add_node(n14)
    data.add_node(n15)
    data.add_node(n16)
    data.add_node(n17)
    data.add_node(n18)
    data.add_node(n19)
    data.add_node(n20)
    data.add_node(n21)
    data.add_node(n22)
    data.add_node(n23)
    data.add_node(n24)
    data.add_node(n25)
    data.add_node(n26)
    data.add_node(n27)
    data.add_node(n28)
    data.add_node(n29)
    data.add_node(n30)
    data.add_node(n31)
    data.add_node(n32)
    data.add_node(n33)
    data.add_node(n34)
    data.add_node(n35)
    data.add_node(n36)
    data.add_node(n37)
    data.add_node(n38)
    data.add_node(n39)
    data.add_node(n40)
    data.add_node(n41)
    data.add_node(n42)
    data.add_node(n43)
    data.add_node(n44)
    data.add_node(n45)
    data.add_node(n46)
    data.add_node(n47)
    data.add_node(n48)
    data.add_node(n49)
    data.add_node(n50)
    data.add_node(n51)
    data.add_node(n52)
    data.add_node(n53)
    data.add_node(n54)
    data.add_node(n55)
    data.add_node(n56)
    data.add_node(n57)
    data.add_node(n58)
    data.add_node(n59)
    data.add_node(n60)
    data.add_node(n61)
    data.add_node(n62)
    data.add_node(n63)



    data.add_node(h1)
    data.add_node(h2)
    data.add_node(ctl1)
    
    return data


def Controlplane(dataplane):
    def exist_ctl():
        for k, n in dataplane.get_nodes().items():
            if n.type == NodeType.CONTROLLER:
                return n
        return None

    def connect_ctl(control_ip):
        if ctl is not None:
            for k, n in dataplane.get_nodes().items():
                if n.type == NodeType.SWITCH:
                    n.set_controller(ip = control_ip)

    ctl = exist_ctl()
    connect_ctl(control_ip = ctl.control_ip)
    logger.info("Controller IP: http://{ip}:8181/onos/ui/login.html".format(ip = ctl.control_ip))



"""
def Controller():

    def exist_ctl():
        for k, node in _nodes.get_nodes().items():
            if isinstance(node, Onos):
                return node

    def set_controller(ctl_ip):
        if ctl is not None:
            for k, node in _nodes.get_nodes().items():
                if isinstance(node, WhiteBox):
                    node.set_controller(ip = ctl_ip)
        else:
            log.warn("No controller setting")

    ctl = exist_ctl()
    set_controller(ctl_ip = ctl.control_ip)

    log.info("Controller IP: http://{ip}:8181/onos/ui/login.html".format(ip=ctl.control_ip))
"""

if __name__ == '__main__':
    logger.info("Creating Topology")

    data = Topology()

    data.commit()

    logger.info("Topology initialized")

    Controlplane(dataplane = data)

    logger.info("Control plane initialized")

    cmd = Prompt(dataplane = data)
    cmd.cmdloop()



