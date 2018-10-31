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
    n64 = WhiteBox(name = "node64")
    n65 = WhiteBox(name = "node65")
    n66 = WhiteBox(name = "node66")
    n67 = WhiteBox(name = "node67")
    n68 = WhiteBox(name = "node68")
    n69 = WhiteBox(name = "node69")
    n70 = WhiteBox(name = "node70")
    n71 = WhiteBox(name = "node71")
    n72 = WhiteBox(name = "node72")
    n73 = WhiteBox(name = "node73")
    n74 = WhiteBox(name = "node74")
    n75 = WhiteBox(name = "node75")
    n76 = WhiteBox(name = "node76")
    n77 = WhiteBox(name = "node77")
    n78 = WhiteBox(name = "node78")
    n79 = WhiteBox(name = "node79")
    n80 = WhiteBox(name = "node80")
    n81 = WhiteBox(name = "node81")
    n82 = WhiteBox(name = "node82")
    n83 = WhiteBox(name = "node83")
    n84 = WhiteBox(name = "node84")
    n85 = WhiteBox(name = "node85")
    n86 = WhiteBox(name = "node86")
    n87 = WhiteBox(name = "node87")
    n88 = WhiteBox(name = "node88")
    n89 = WhiteBox(name = "node89")
    n90 = WhiteBox(name = "node90")
    n91 = WhiteBox(name = "node91")
    n92 = WhiteBox(name = "node92")
    n93 = WhiteBox(name = "node93")
    n94 = WhiteBox(name = "node94")
    n95 = WhiteBox(name = "node95")
    n96 = WhiteBox(name = "node96")
    n97 = WhiteBox(name = "node97")
    n98 = WhiteBox(name = "node98")
    n99 = WhiteBox(name = "node99")
    n100 = WhiteBox(name = "node100")
    n101 = WhiteBox(name = "node101")
    n102 = WhiteBox(name = "node102")
    n103 = WhiteBox(name = "node103")
    n104 = WhiteBox(name = "node104")
    n105 = WhiteBox(name = "node105")
    n106 = WhiteBox(name = "node106")
    n107 = WhiteBox(name = "node107")
    n108 = WhiteBox(name = "node108")
    n109 = WhiteBox(name = "node109")
    n110 = WhiteBox(name = "node110")
    n111 = WhiteBox(name = "node111")
    n112 = WhiteBox(name = "node112")
    n113 = WhiteBox(name = "node113")
    n114 = WhiteBox(name = "node114")
    n115 = WhiteBox(name = "node115")
    n116 = WhiteBox(name = "node116")
    n117 = WhiteBox(name = "node117")
    n118 = WhiteBox(name = "node118")
    n119 = WhiteBox(name = "node119")
    n120 = WhiteBox(name = "node120")
    n121 = WhiteBox(name = "node121")
    n122 = WhiteBox(name = "node122")
    n123 = WhiteBox(name = "node123")
    n124 = WhiteBox(name = "node124")
    n125 = WhiteBox(name = "node125")
    n126 = WhiteBox(name = "node126")
    n127 = WhiteBox(name = "node127")




    ctl1 = Onos(name = "control1")

    h1 = Host(name = "host1")
    h2 = Host(name = "host2")

    link1 = HostLinkVeth(node_host = h1, node_target = n5, ip_host = "10.0.0.1/24", mtu = "9000")
    link2 = HostLinkVeth(node_host = h2, node_target = n24, ip_host = "10.0.0.2/24", mtu = "9000")
    

    link3 = DirectLinkBridge(node_source = n1, node_target = n2, mtu = "9000")
    link4 = DirectLinkBridge(node_source = n1, node_target = n65, mtu = "9000")
    link5 = DirectLinkBridge(node_source = n2, node_target = n3, mtu = "9000")
    link6 = DirectLinkBridge(node_source = n2, node_target = n34, mtu = "9000")
    link7 = DirectLinkBridge(node_source = n3, node_target = n4, mtu = "9000")
    link8 = DirectLinkBridge(node_source = n3, node_target = n19, mtu = "9000")
    link9 = DirectLinkBridge(node_source = n4, node_target = n5, mtu = "9000")
    link10 = DirectLinkBridge(node_source = n4, node_target = n12, mtu = "9000")
    link11 = DirectLinkBridge(node_source = n5, node_target = n6, mtu = "9000")
    link12 = DirectLinkBridge(node_source = n5, node_target = n9, mtu = "9000")
    link13 = DirectLinkBridge(node_source = n6, node_target = n7, mtu = "9000")
    link14 = DirectLinkBridge(node_source = n6, node_target = n8, mtu = "9000")
    link15 = DirectLinkBridge(node_source = n9, node_target = n10, mtu = "9000")
    link16 = DirectLinkBridge(node_source = n9, node_target = n11, mtu = "9000")
    link17 = DirectLinkBridge(node_source = n12, node_target = n13, mtu = "9000")
    link18 = DirectLinkBridge(node_source = n12, node_target = n16, mtu = "9000")
    link19 = DirectLinkBridge(node_source = n13, node_target = n14, mtu = "9000")
    link20 = DirectLinkBridge(node_source = n13, node_target = n15, mtu = "9000")
    link21 = DirectLinkBridge(node_source = n16, node_target = n17, mtu = "9000")
    link22 = DirectLinkBridge(node_source = n16, node_target = n18, mtu = "9000")
    link23 = DirectLinkBridge(node_source = n19, node_target = n20, mtu = "9000")
    link24 = DirectLinkBridge(node_source = n19, node_target = n27, mtu = "9000")
    link25 = DirectLinkBridge(node_source = n20, node_target = n21, mtu = "9000")
    link26 = DirectLinkBridge(node_source = n20, node_target = n24, mtu = "9000")
    link27 = DirectLinkBridge(node_source = n21, node_target = n22, mtu = "9000")
    link28 = DirectLinkBridge(node_source = n21, node_target = n23, mtu = "9000")
    link29 = DirectLinkBridge(node_source = n24, node_target = n25, mtu = "9000")
    link30 = DirectLinkBridge(node_source = n24, node_target = n26, mtu = "9000")
    link31 = DirectLinkBridge(node_source = n27, node_target = n28, mtu = "9000")
    link32 = DirectLinkBridge(node_source = n27, node_target = n31, mtu = "9000")
    link33 = DirectLinkBridge(node_source = n28, node_target = n29, mtu = "9000")
    link34 = DirectLinkBridge(node_source = n28, node_target = n30, mtu = "9000")
    link35 = DirectLinkBridge(node_source = n31, node_target = n32, mtu = "9000")
    link36 = DirectLinkBridge(node_source = n31, node_target = n33, mtu = "9000")
    link37 = DirectLinkBridge(node_source = n34, node_target = n35, mtu = "9000")
    link38 = DirectLinkBridge(node_source = n34, node_target = n50, mtu = "9000")
    link39 = DirectLinkBridge(node_source = n35, node_target = n36, mtu = "9000")
    link40 = DirectLinkBridge(node_source = n35, node_target = n43, mtu = "9000")
    link41 = DirectLinkBridge(node_source = n36, node_target = n37, mtu = "9000")
    link42 = DirectLinkBridge(node_source = n36, node_target = n40, mtu = "9000")
    link43 = DirectLinkBridge(node_source = n37, node_target = n38, mtu = "9000")
    link44 = DirectLinkBridge(node_source = n37, node_target = n39, mtu = "9000")
    link45 = DirectLinkBridge(node_source = n40, node_target = n41, mtu = "9000")
    link46 = DirectLinkBridge(node_source = n40, node_target = n42, mtu = "9000")
    link47 = DirectLinkBridge(node_source = n43, node_target = n44, mtu = "9000")
    link48 = DirectLinkBridge(node_source = n43, node_target = n47, mtu = "9000")
    link49 = DirectLinkBridge(node_source = n44, node_target = n45, mtu = "9000")
    link50 = DirectLinkBridge(node_source = n44, node_target = n46, mtu = "9000")
    link51 = DirectLinkBridge(node_source = n47, node_target = n48, mtu = "9000")
    link52 = DirectLinkBridge(node_source = n47, node_target = n49, mtu = "9000")
    link53 = DirectLinkBridge(node_source = n50, node_target = n51, mtu = "9000")
    link54 = DirectLinkBridge(node_source = n50, node_target = n58, mtu = "9000")
    link55 = DirectLinkBridge(node_source = n51, node_target = n52, mtu = "9000")
    link56 = DirectLinkBridge(node_source = n51, node_target = n55, mtu = "9000")
    link57 = DirectLinkBridge(node_source = n52, node_target = n53, mtu = "9000")
    link58 = DirectLinkBridge(node_source = n52, node_target = n54, mtu = "9000")
    link59 = DirectLinkBridge(node_source = n55, node_target = n56, mtu = "9000")
    link60 = DirectLinkBridge(node_source = n55, node_target = n57, mtu = "9000")
    link61 = DirectLinkBridge(node_source = n58, node_target = n59, mtu = "9000")
    link62 = DirectLinkBridge(node_source = n58, node_target = n62, mtu = "9000")
    link63 = DirectLinkBridge(node_source = n59, node_target = n60, mtu = "9000")
    link64 = DirectLinkBridge(node_source = n59, node_target = n61, mtu = "9000")
    link65 = DirectLinkBridge(node_source = n62, node_target = n63, mtu = "9000")
    link66 = DirectLinkBridge(node_source = n62, node_target = n64, mtu = "9000")
    link67 = DirectLinkBridge(node_source = n65, node_target = n66, mtu = "9000")
    link68 = DirectLinkBridge(node_source = n65, node_target = n97, mtu = "9000")
    link69 = DirectLinkBridge(node_source = n66, node_target = n67, mtu = "9000")
    link70 = DirectLinkBridge(node_source = n66, node_target = n82, mtu = "9000")
    link71 = DirectLinkBridge(node_source = n67, node_target = n68, mtu = "9000")
    link72 = DirectLinkBridge(node_source = n67, node_target = n75, mtu = "9000")
    link73 = DirectLinkBridge(node_source = n68, node_target = n69, mtu = "9000")
    link74 = DirectLinkBridge(node_source = n68, node_target = n72, mtu = "9000")
    link75 = DirectLinkBridge(node_source = n69, node_target = n70, mtu = "9000")
    link76 = DirectLinkBridge(node_source = n69, node_target = n71, mtu = "9000")
    link77 = DirectLinkBridge(node_source = n72, node_target = n73, mtu = "9000")
    link78 = DirectLinkBridge(node_source = n75, node_target = n76, mtu = "9000")
    link79 = DirectLinkBridge(node_source = n75, node_target = n79, mtu = "9000")
    link80 = DirectLinkBridge(node_source = n76, node_target = n77, mtu = "9000")
    link81 = DirectLinkBridge(node_source = n76, node_target = n78, mtu = "9000")
    link82 = DirectLinkBridge(node_source = n79, node_target = n80, mtu = "9000")
    link83 = DirectLinkBridge(node_source = n79, node_target = n81, mtu = "9000")
    link84 = DirectLinkBridge(node_source = n82, node_target = n83, mtu = "9000")
    link85 = DirectLinkBridge(node_source = n82, node_target = n90, mtu = "9000")
    link86 = DirectLinkBridge(node_source = n83, node_target = n84, mtu = "9000")
    link87 = DirectLinkBridge(node_source = n83, node_target = n87, mtu = "9000")
    link88 = DirectLinkBridge(node_source = n84, node_target = n85, mtu = "9000")
    link89 = DirectLinkBridge(node_source = n84, node_target = n86, mtu = "9000")
    link90 = DirectLinkBridge(node_source = n87, node_target = n88, mtu = "9000")
    link91 = DirectLinkBridge(node_source = n87, node_target = n89, mtu = "9000")
    link92 = DirectLinkBridge(node_source = n90, node_target = n91, mtu = "9000")
    link93 = DirectLinkBridge(node_source = n90, node_target = n94, mtu = "9000")
    link94 = DirectLinkBridge(node_source = n91, node_target = n92, mtu = "9000")
    link95 = DirectLinkBridge(node_source = n91, node_target = n93, mtu = "9000")
    link96 = DirectLinkBridge(node_source = n94, node_target = n95, mtu = "9000")
    link97 = DirectLinkBridge(node_source = n94, node_target = n96, mtu = "9000")
    link98 = DirectLinkBridge(node_source = n97, node_target = n98, mtu = "9000")
    link99 = DirectLinkBridge(node_source = n72, node_target = n74, mtu = "9000")
    link100 = DirectLinkBridge(node_source = n98, node_target = n99, mtu = "9000")
    link101 = DirectLinkBridge(node_source = n98, node_target = n106, mtu = "9000")
    link102 = DirectLinkBridge(node_source = n99, node_target = n100, mtu = "9000")
    link103 = DirectLinkBridge(node_source = n99, node_target = n103, mtu = "9000")
    link104 = DirectLinkBridge(node_source = n100, node_target = n101, mtu = "9000")
    link105 = DirectLinkBridge(node_source = n100, node_target = n102, mtu = "9000")
    link106 = DirectLinkBridge(node_source = n103, node_target = n104, mtu = "9000")
    link107 = DirectLinkBridge(node_source = n103, node_target = n105, mtu = "9000")
    link108 = DirectLinkBridge(node_source = n106, node_target = n107, mtu = "9000")
    link109 = DirectLinkBridge(node_source = n106, node_target = n110, mtu = "9000")
    link110 = DirectLinkBridge(node_source = n107, node_target = n108, mtu = "9000")
    link111 = DirectLinkBridge(node_source = n107, node_target = n109, mtu = "9000")
    link112 = DirectLinkBridge(node_source = n110, node_target = n111, mtu = "9000")
    link113 = DirectLinkBridge(node_source = n110, node_target = n112, mtu = "9000")
    link114 = DirectLinkBridge(node_source = n113, node_target = n114, mtu = "9000")
    link115 = DirectLinkBridge(node_source = n113, node_target = n121, mtu = "9000")
    link116 = DirectLinkBridge(node_source = n114, node_target = n115, mtu = "9000")
    link117 = DirectLinkBridge(node_source = n114, node_target = n118, mtu = "9000")
    link118 = DirectLinkBridge(node_source = n115, node_target = n116, mtu = "9000")
    link119 = DirectLinkBridge(node_source = n115, node_target = n117, mtu = "9000")
    link120 = DirectLinkBridge(node_source = n118, node_target = n119, mtu = "9000")
    link121 = DirectLinkBridge(node_source = n118, node_target = n120, mtu = "9000")
    link122 = DirectLinkBridge(node_source = n121, node_target = n122, mtu = "9000")
    link123 = DirectLinkBridge(node_source = n121, node_target = n125, mtu = "9000")
    link124 = DirectLinkBridge(node_source = n122, node_target = n123, mtu = "9000")
    link125 = DirectLinkBridge(node_source = n122, node_target = n124, mtu = "9000")
    link126 = DirectLinkBridge(node_source = n125, node_target = n126, mtu = "9000")
    link127 = DirectLinkBridge(node_source = n125, node_target = n127, mtu = "9000")
    link128 = DirectLinkBridge(node_source = n97, node_target = n113, mtu = "9000")

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
    data.add_link(link65)
    data.add_link(link66)
    data.add_link(link67)
    data.add_link(link68)
    data.add_link(link69)
    data.add_link(link70)
    data.add_link(link71)
    data.add_link(link72)
    data.add_link(link73)
    data.add_link(link74)
    data.add_link(link75)
    data.add_link(link76)
    data.add_link(link77)
    data.add_link(link78)
    data.add_link(link79)
    data.add_link(link80)
    data.add_link(link81)
    data.add_link(link82)
    data.add_link(link83)
    data.add_link(link84)
    data.add_link(link85)
    data.add_link(link86)
    data.add_link(link87)
    data.add_link(link88)
    data.add_link(link89)
    data.add_link(link90)
    data.add_link(link91)
    data.add_link(link92)
    data.add_link(link93)
    data.add_link(link94)
    data.add_link(link95)
    data.add_link(link96)
    data.add_link(link97)
    data.add_link(link98)
    data.add_link(link99)
    data.add_link(link100)
    data.add_link(link101)
    data.add_link(link102)
    data.add_link(link103)
    data.add_link(link104)
    data.add_link(link105)
    data.add_link(link106)
    data.add_link(link107)
    data.add_link(link108)
    data.add_link(link109)
    data.add_link(link110)
    data.add_link(link111)
    data.add_link(link112)
    data.add_link(link113)
    data.add_link(link114)
    data.add_link(link115)
    data.add_link(link116)
    data.add_link(link117)
    data.add_link(link118)
    data.add_link(link119)
    data.add_link(link120)
    data.add_link(link121)
    data.add_link(link122)
    data.add_link(link123)
    data.add_link(link124)
    data.add_link(link125)
    data.add_link(link126)
    data.add_link(link127)
    data.add_link(link128)



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
    data.add_node(n64)
    data.add_node(n65)
    data.add_node(n66)
    data.add_node(n67)
    data.add_node(n68)
    data.add_node(n69)
    data.add_node(n70)
    data.add_node(n71)
    data.add_node(n72)
    data.add_node(n73)
    data.add_node(n74)
    data.add_node(n75)
    data.add_node(n76)
    data.add_node(n77)
    data.add_node(n78)
    data.add_node(n79)
    data.add_node(n80)
    data.add_node(n81)
    data.add_node(n82)
    data.add_node(n83)
    data.add_node(n84)
    data.add_node(n85)
    data.add_node(n86)
    data.add_node(n87)
    data.add_node(n88)
    data.add_node(n89)
    data.add_node(n90)
    data.add_node(n91)
    data.add_node(n92)
    data.add_node(n93)
    data.add_node(n94)
    data.add_node(n95)
    data.add_node(n96)
    data.add_node(n97)
    data.add_node(n98)
    data.add_node(n99)
    data.add_node(n100)
    data.add_node(n101)
    data.add_node(n102)
    data.add_node(n103)
    data.add_node(n104)
    data.add_node(n105)
    data.add_node(n106)
    data.add_node(n107)
    data.add_node(n108)
    data.add_node(n109)
    data.add_node(n110)
    data.add_node(n111)
    data.add_node(n112)
    data.add_node(n113)
    data.add_node(n114)
    data.add_node(n115)
    data.add_node(n116)
    data.add_node(n117)
    data.add_node(n118)
    data.add_node(n119)
    data.add_node(n120)
    data.add_node(n121)
    data.add_node(n122)
    data.add_node(n123)
    data.add_node(n124)
    data.add_node(n125)
    data.add_node(n126)
    data.add_node(n127)

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


