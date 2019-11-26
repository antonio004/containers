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

    ctl1 = Onos(name = "control1")

    h1 = Host(name = "host1")
    h2 = Host(name = "host2")

    link1 = HostLinkBridge(node_host = h1, node_target = n5, ip_host = "10.0.0.1/24", mtu = "9000")
    link2 = HostLinkBridge(node_host = h2, node_target = n24, ip_host = "10.0.0.2/24", mtu = "9000")
    

    link3 = DirectLinkBridge(node_source = n1, node_target = n2, mtu = "9000")
    link4 = DirectLinkBridge(node_source = n2, node_target = n3, mtu = "9000")
    link5 = DirectLinkBridge(node_source = n3, node_target = n4, mtu = "9000")
    link6 = DirectLinkBridge(node_source = n4, node_target = n5, mtu = "9000")
    link7 = DirectLinkBridge(node_source = n4, node_target = n6, mtu = "9000")
    link8 = DirectLinkBridge(node_source = n3, node_target = n7, mtu = "9000")
    link9 = DirectLinkBridge(node_source = n7, node_target = n8, mtu = "9000")
    link10 = DirectLinkBridge(node_source = n7, node_target = n9, mtu = "9000")


    link11 = DirectLinkBridge(node_source = n2, node_target = n10, mtu = "9000")
    link12 = DirectLinkBridge(node_source = n10, node_target = n11, mtu = "9000")
    link13 = DirectLinkBridge(node_source = n11, node_target = n12, mtu = "9000")
    link14 = DirectLinkBridge(node_source = n11, node_target = n13, mtu = "9000")
    link15 = DirectLinkBridge(node_source = n10, node_target = n14, mtu = "9000")
    link16 = DirectLinkBridge(node_source = n14, node_target = n15, mtu = "9000")
    link17 = DirectLinkBridge(node_source = n14, node_target = n16, mtu = "9000")
    

    link18 = DirectLinkBridge(node_source = n1, node_target = n17, mtu = "9000")
    link19 = DirectLinkBridge(node_source = n17, node_target = n18, mtu = "9000")
    link20 = DirectLinkBridge(node_source = n18, node_target = n19, mtu = "9000")
    link21 = DirectLinkBridge(node_source = n19, node_target = n20, mtu = "9000")
    link22 = DirectLinkBridge(node_source = n19, node_target = n21, mtu = "9000")
    link23 = DirectLinkBridge(node_source = n18, node_target = n22, mtu = "9000")
    link24 = DirectLinkBridge(node_source = n22, node_target = n23, mtu = "9000")
    link25 = DirectLinkBridge(node_source = n22, node_target = n24, mtu = "9000")
    


    link26 = DirectLinkBridge(node_source = n17, node_target = n25, mtu = "9000")
    link27 = DirectLinkBridge(node_source = n25, node_target = n26, mtu = "9000")
    link28 = DirectLinkBridge(node_source = n26, node_target = n27, mtu = "9000")
    link29 = DirectLinkBridge(node_source = n26, node_target = n28, mtu = "9000")
    link30 = DirectLinkBridge(node_source = n25, node_target = n29, mtu = "9000")
    link31 = DirectLinkBridge(node_source = n29, node_target = n30, mtu = "9000")
    link32 = DirectLinkBridge(node_source = n29, node_target = n31, mtu = "9000")


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



