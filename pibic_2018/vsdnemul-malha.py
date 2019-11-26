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
    aux1=61
    #result = random.sample(range(0,100), 4)
    for i in range(1, aux1):
    	locals()["sw"+str(i)] = dp.addNode(Whitebox("sw"+str(i)))

    # Create Host Nodes

    h1 = dp.addNode(Host(name="h1", ip="10.0.0.1", mask="24"))
    h2 = dp.addNode(Host(name="h2", ip="10.0.0.2", mask="24"))
    h3 = dp.addNode(Host(name="h3", ip="10.0.0.3", mask="24")) 
    h4 = dp.addNode(Host(name="h4", ip="10.0.0.4", mask="24"))
    h5 = dp.addNode(Host(name="h5", ip="10.0.0.5", mask="24"))
    h6 = dp.addNode(Host(name="h6", ip="10.0.0.6", mask="24"))
    h7 = dp.addNode(Host(name="h7", ip="10.0.0.7", mask="24"))
    h8 = dp.addNode(Host(name="h8", ip="10.0.0.8", mask="24"))
    h9 = dp.addNode(Host(name="h9", ip="10.0.0.9", mask="24"))
    h10 = dp.addNode(Host(name="h10", ip="10.0.0.10", mask="24")) 
    h11 = dp.addNode(Host(name="h11", ip="10.0.0.11", mask="24"))
    h12 = dp.addNode(Host(name="h12", ip="10.0.0.12", mask="24"))
    h13 = dp.addNode(Host(name="h13", ip="10.0.0.13", mask="24"))
    h14 = dp.addNode(Host(name="h14", ip="10.0.0.14", mask="24"))
    h15 = dp.addNode(Host(name="h15", ip="10.0.0.15", mask="24"))
    h16 = dp.addNode(Host(name="h16", ip="10.0.0.16", mask="24"))
    #h17 = dp.addNode(Host(name="h17", ip="10.0.0.17", mask="24"))
    #h18 = dp.addNode(Host(name="h18", ip="10.0.0.18", mask="24"))
    #h19 = dp.addNode(Host(name="h19", ip="10.0.0.19", mask="24"))
    #h20 = dp.addNode(Host(name="h20", ip="10.0.0.20", mask="24"))
    #h21 = dp.addNode(Host(name="h21", ip="10.0.0.21", mask="24"))
    #h22 = dp.addNode(Host(name="h22", ip="10.0.0.22", mask="24"))
    #h23 = dp.addNode(Host(name="h23", ip="10.0.0.23", mask="24"))
    #h24 = dp.addNode(Host(name="h24", ip="10.0.0.24", mask="24"))
    #h25 = dp.addNode(Host(name="h25", ip="10.0.0.25", mask="24"))
    #h26 = dp.addNode(Host(name="h26", ip="10.0.0.26", mask="24"))
    #h27 = dp.addNode(Host(name="h27", ip="10.0.0.27", mask="24"))
    #h28 = dp.addNode(Host(name="h28", ip="10.0.0.28", mask="24"))
    #h29 = dp.addNode(Host(name="h29", ip="10.0.0.29", mask="24"))
    #h30 = dp.addNode(Host(name="h30", ip="10.0.0.30", mask="24"))
    #h31 = dp.addNode(Host(name="h31", ip="10.0.0.31", mask="24"))
    #h32 = dp.addNode(Host(name="h32", ip="10.0.0.32", mask="24"))
    #h33 = dp.addNode(Host(name="h33", ip="10.0.0.33", mask="24"))
    #h34 = dp.addNode(Host(name="h34", ip="10.0.0.34", mask="24"))
    #h35 = dp.addNode(Host(name="h35", ip="10.0.0.35", mask="24"))
    #h36 = dp.addNode(Host(name="h36", ip="10.0.0.36", mask="24"))
    #h37 = dp.addNode(Host(name="h37", ip="10.0.0.37", mask="24"))
    #h38 = dp.addNode(Host(name="h38", ip="10.0.0.38", mask="24"))
    #h39 = dp.addNode(Host(name="h39", ip="10.0.0.39", mask="24"))
    #h40 = dp.addNode(Host(name="h40", ip="10.0.0.40", mask="24"))
    #h41 = dp.addNode(Host(name="h41", ip="10.0.0.41", mask="24"))
    #h42 = dp.addNode(Host(name="h42", ip="10.0.0.42", mask="24"))
    #h43 = dp.addNode(Host(name="h43", ip="10.0.0.43", mask="24"))
    #h44 = dp.addNode(Host(name="h44", ip="10.0.0.44", mask="24"))
    #h45 = dp.addNode(Host(name="h45", ip="10.0.0.45", mask="24"))
    #h46 = dp.addNode(Host(name="h46", ip="10.0.0.46", mask="24"))
    #h47 = dp.addNode(Host(name="h47", ip="10.0.0.47", mask="24"))
    #h48 = dp.addNode(Host(name="h48", ip="10.0.0.48", mask="24"))
    #h49 = dp.addNode(Host(name="h49", ip="10.0.0.49", mask="24"))
    #h50 = dp.addNode(Host(name="h50", ip="10.0.0.50", mask="24"))
    #h51 = dp.addNode(Host(name="h51", ip="10.0.0.51", mask="24"))
    #h52 = dp.addNode(Host(name="h52", ip="10.0.0.52", mask="24"))
    #h53 = dp.addNode(Host(name="h53", ip="10.0.0.53", mask="24"))
    #h54 = dp.addNode(Host(name="h54", ip="10.0.0.54", mask="24"))
    #h55 = dp.addNode(Host(name="h55", ip="10.0.0.55", mask="24"))
    #h56 = dp.addNode(Host(name="h56", ip="10.0.0.56", mask="24"))
    #h57 = dp.addNode(Host(name="h57", ip="10.0.0.57", mask="24"))
    #h58 = dp.addNode(Host(name="h58", ip="10.0.0.58", mask="24"))
    #h59 = dp.addNode(Host(name="h59", ip="10.0.0.59", mask="24"))
    #h60 = dp.addNode(Host(name="h60", ip="10.0.0.60", mask="24"))
    #h61 = dp.addNode(Host(name="h61", ip="10.0.0.61", mask="24"))
    #h62 = dp.addNode(Host(name="h62", ip="10.0.0.62", mask="24"))
    #h63 = dp.addNode(Host(name="h63", ip="10.0.0.63", mask="24"))
    #h64 = dp.addNode(Host(name="h64", ip="10.0.0.64", mask="24"))
    #h65 = dp.addNode(Host(name="h65", ip="10.0.0.65", mask="24"))
    #h66 = dp.addNode(Host(name="h66", ip="10.0.0.66", mask="24"))
    #h67 = dp.addNode(Host(name="h67", ip="10.0.0.67", mask="24"))
    #h68 = dp.addNode(Host(name="h68", ip="10.0.0.68", mask="24"))
    #h69 = dp.addNode(Host(name="h69", ip="10.0.0.69", mask="24"))
    #h70 = dp.addNode(Host(name="h70", ip="10.0.0.70", mask="24"))
    #h71 = dp.addNode(Host(name="h71", ip="10.0.0.71", mask="24"))
    #h72 = dp.addNode(Host(name="h72", ip="10.0.0.72", mask="24"))
    #h73 = dp.addNode(Host(name="h73", ip="10.0.0.73", mask="24"))
    #h74 = dp.addNode(Host(name="h74", ip="10.0.0.74", mask="24"))
    #h75 = dp.addNode(Host(name="h75", ip="10.0.0.75", mask="24"))
    #h76 = dp.addNode(Host(name="h76", ip="10.0.0.76", mask="24"))
    #h77 = dp.addNode(Host(name="h77", ip="10.0.0.77", mask="24"))
    #h78 = dp.addNode(Host(name="h78", ip="10.0.0.78", mask="24"))
    #h79 = dp.addNode(Host(name="h79", ip="10.0.0.79", mask="24"))
    #h80 = dp.addNode(Host(name="h80", ip="10.0.0.80", mask="24"))
    #h81 = dp.addNode(Host(name="h81", ip="10.0.0.81", mask="24"))
    #h82 = dp.addNode(Host(name="h82", ip="10.0.0.82", mask="24"))
    #h83 = dp.addNode(Host(name="h83", ip="10.0.0.83", mask="24"))
    #h84 = dp.addNode(Host(name="h84", ip="10.0.0.84", mask="24"))
    #h85 = dp.addNode(Host(name="h85", ip="10.0.0.85", mask="24"))
    #h86 = dp.addNode(Host(name="h86", ip="10.0.0.86", mask="24"))
    #h87 = dp.addNode(Host(name="h87", ip="10.0.0.87", mask="24"))
    #h88 = dp.addNode(Host(name="h88", ip="10.0.0.88", mask="24"))
    #h89 = dp.addNode(Host(name="h89", ip="10.0.0.89", mask="24"))
    #h90 = dp.addNode(Host(name="h90", ip="10.0.0.90", mask="24"))
    #h91 = dp.addNode(Host(name="h91", ip="10.0.0.91", mask="24"))
    #h92 = dp.addNode(Host(name="h92", ip="10.0.0.92", mask="24"))
    #h93 = dp.addNode(Host(name="h93", ip="10.0.0.93", mask="24"))
    #h94 = dp.addNode(Host(name="h94", ip="10.0.0.94", mask="24"))
    #h95 = dp.addNode(Host(name="h95", ip="10.0.0.95", mask="24"))
    #h96 = dp.addNode(Host(name="h96", ip="10.0.0.96", mask="24"))
    #h97 = dp.addNode(Host(name="h97", ip="10.0.0.97", mask="24"))
    #h98 = dp.addNode(Host(name="h98", ip="10.0.0.98", mask="24"))
    #h99 = dp.addNode(Host(name="h99", ip="10.0.0.99", mask="24"))
    #h100 = dp.addNode(Host(name="h100", ip="10.0.0.100", mask="24"))

    # Adding links to dataplane
    # Adding links to dataplane

    hl1 = dp.addLink(LinkPair(name="hl1", node_source=locals()["sw1"], node_target=locals()["sw1"], type=LinkType.DIRECT)) 
    hl2 = dp.addLink(LinkPair(name="hl2", node_source=locals()["sw1"], node_target=locals()["sw2"], type=LinkType.DIRECT)) 
    hl3 = dp.addLink(LinkPair(name="hl3", node_source=locals()["sw1"], node_target=locals()["sw3"], type=LinkType.DIRECT)) 
    hl4 = dp.addLink(LinkPair(name="hl4", node_source=locals()["sw1"], node_target=locals()["sw4"], type=LinkType.DIRECT)) 
    hl5 = dp.addLink(LinkPair(name="hl5", node_source=locals()["sw1"], node_target=locals()["sw5"], type=LinkType.DIRECT)) 
    hl6 = dp.addLink(LinkPair(name="hl6", node_source=locals()["sw1"], node_target=locals()["sw6"], type=LinkType.DIRECT)) 
    hl7 = dp.addLink(LinkPair(name="hl7", node_source=locals()["sw1"], node_target=locals()["sw7"], type=LinkType.DIRECT)) 
    hl8 = dp.addLink(LinkPair(name="hl8", node_source=locals()["sw1"], node_target=locals()["sw8"], type=LinkType.DIRECT)) 
    hl9 = dp.addLink(LinkPair(name="hl9", node_source=locals()["sw1"], node_target=locals()["sw9"], type=LinkType.DIRECT)) 
    hl10 = dp.addLink(LinkPair(name="hl10", node_source=locals()["sw1"], node_target=locals()["sw10"], type=LinkType.DIRECT))
    hl11 = dp.addLink(LinkPair(name="hl11", node_source=locals()["sw1"], node_target=locals()["sw11"], type=LinkType.DIRECT))
    hl12 = dp.addLink(LinkPair(name="hl12", node_source=locals()["sw1"], node_target=locals()["sw12"], type=LinkType.DIRECT))
    hl13 = dp.addLink(LinkPair(name="hl13", node_source=locals()["sw1"], node_target=locals()["sw13"], type=LinkType.DIRECT))
    hl14 = dp.addLink(LinkPair(name="hl14", node_source=locals()["sw1"], node_target=locals()["sw14"], type=LinkType.DIRECT))
    hl15 = dp.addLink(LinkPair(name="hl15", node_source=locals()["sw1"], node_target=locals()["sw15"], type=LinkType.DIRECT))
    hl16 = dp.addLink(LinkPair(name="hl16", node_source=locals()["sw1"], node_target=locals()["sw16"], type=LinkType.DIRECT))
    hl17 = dp.addLink(LinkPair(name="hl17", node_source=locals()["sw1"], node_target=locals()["sw17"], type=LinkType.DIRECT))
    hl18 = dp.addLink(LinkPair(name="hl18", node_source=locals()["sw1"], node_target=locals()["sw18"], type=LinkType.DIRECT))
    hl19 = dp.addLink(LinkPair(name="hl19", node_source=locals()["sw1"], node_target=locals()["sw19"], type=LinkType.DIRECT))    
    hl20 = dp.addLink(LinkPair(name="hl20", node_source=locals()["sw1"], node_target=locals()["sw20"], type=LinkType.DIRECT))
    hl21 = dp.addLink(LinkPair(name="hl21", node_source=locals()["sw1"], node_target=locals()["sw21"], type=LinkType.DIRECT))
    hl22 = dp.addLink(LinkPair(name="hl22", node_source=locals()["sw1"], node_target=locals()["sw22"], type=LinkType.DIRECT))
    hl23 = dp.addLink(LinkPair(name="hl23", node_source=locals()["sw1"], node_target=locals()["sw23"], type=LinkType.DIRECT))
    hl24 = dp.addLink(LinkPair(name="hl24", node_source=locals()["sw1"], node_target=locals()["sw24"], type=LinkType.DIRECT))
    hl25 = dp.addLink(LinkPair(name="hl25", node_source=locals()["sw1"], node_target=locals()["sw25"], type=LinkType.DIRECT))
    hl26 = dp.addLink(LinkPair(name="hl26", node_source=locals()["sw1"], node_target=locals()["sw26"], type=LinkType.DIRECT))
    hl27 = dp.addLink(LinkPair(name="hl27", node_source=locals()["sw1"], node_target=locals()["sw27"], type=LinkType.DIRECT))
    hl28 = dp.addLink(LinkPair(name="hl28", node_source=locals()["sw1"], node_target=locals()["sw28"], type=LinkType.DIRECT))
    hl29 = dp.addLink(LinkPair(name="hl29", node_source=locals()["sw1"], node_target=locals()["sw29"], type=LinkType.DIRECT))
    hl30 = dp.addLink(LinkPair(name="hl30", node_source=locals()["sw1"], node_target=locals()["sw30"], type=LinkType.DIRECT))
    hl31 = dp.addLink(LinkPair(name="hl31", node_source=locals()["sw1"], node_target=locals()["sw31"], type=LinkType.DIRECT))
    hl32 = dp.addLink(LinkPair(name="hl32", node_source=locals()["sw1"], node_target=locals()["sw32"], type=LinkType.DIRECT))
    hl33 = dp.addLink(LinkPair(name="hl33", node_source=locals()["sw1"], node_target=locals()["sw33"], type=LinkType.DIRECT))
    hl34 = dp.addLink(LinkPair(name="hl34", node_source=locals()["sw1"], node_target=locals()["sw34"], type=LinkType.DIRECT))
    hl35 = dp.addLink(LinkPair(name="hl35", node_source=locals()["sw1"], node_target=locals()["sw35"], type=LinkType.DIRECT))
    hl36 = dp.addLink(LinkPair(name="hl36", node_source=locals()["sw1"], node_target=locals()["sw36"], type=LinkType.DIRECT))
    hl37 = dp.addLink(LinkPair(name="hl37", node_source=locals()["sw1"], node_target=locals()["sw37"], type=LinkType.DIRECT))
    hl38 = dp.addLink(LinkPair(name="hl38", node_source=locals()["sw1"], node_target=locals()["sw38"], type=LinkType.DIRECT))
    hl39 = dp.addLink(LinkPair(name="hl39", node_source=locals()["sw1"], node_target=locals()["sw39"], type=LinkType.DIRECT))
    hl40 = dp.addLink(LinkPair(name="hl40", node_source=locals()["sw1"], node_target=locals()["sw40"], type=LinkType.DIRECT))
    hl41 = dp.addLink(LinkPair(name="hl41", node_source=locals()["sw1"], node_target=locals()["sw41"], type=LinkType.DIRECT))
    hl42 = dp.addLink(LinkPair(name="hl42", node_source=locals()["sw1"], node_target=locals()["sw42"], type=LinkType.DIRECT))
    hl43 = dp.addLink(LinkPair(name="hl43", node_source=locals()["sw1"], node_target=locals()["sw43"], type=LinkType.DIRECT))
    hl44 = dp.addLink(LinkPair(name="hl44", node_source=locals()["sw1"], node_target=locals()["sw44"], type=LinkType.DIRECT))
    hl45 = dp.addLink(LinkPair(name="hl45", node_source=locals()["sw1"], node_target=locals()["sw45"], type=LinkType.DIRECT))
    hl46 = dp.addLink(LinkPair(name="hl46", node_source=locals()["sw1"], node_target=locals()["sw46"], type=LinkType.DIRECT))
    hl47 = dp.addLink(LinkPair(name="hl47", node_source=locals()["sw1"], node_target=locals()["sw47"], type=LinkType.DIRECT))
    hl48 = dp.addLink(LinkPair(name="hl48", node_source=locals()["sw1"], node_target=locals()["sw48"], type=LinkType.DIRECT))
    hl49 = dp.addLink(LinkPair(name="hl49", node_source=locals()["sw1"], node_target=locals()["sw49"], type=LinkType.DIRECT))
    hl50 = dp.addLink(LinkPair(name="hl50", node_source=locals()["sw1"], node_target=locals()["sw50"], type=LinkType.DIRECT))
    hl51 = dp.addLink(LinkPair(name="hl51", node_source=locals()["sw1"], node_target=locals()["sw51"], type=LinkType.DIRECT))
    hl52 = dp.addLink(LinkPair(name="hl52", node_source=locals()["sw1"], node_target=locals()["sw52"], type=LinkType.DIRECT))
    hl53 = dp.addLink(LinkPair(name="hl53", node_source=locals()["sw1"], node_target=locals()["sw53"], type=LinkType.DIRECT))
    hl54 = dp.addLink(LinkPair(name="hl54", node_source=locals()["sw1"], node_target=locals()["sw54"], type=LinkType.DIRECT))
    hl55 = dp.addLink(LinkPair(name="hl55", node_source=locals()["sw1"], node_target=locals()["sw55"], type=LinkType.DIRECT))
    hl56 = dp.addLink(LinkPair(name="hl56", node_source=locals()["sw1"], node_target=locals()["sw56"], type=LinkType.DIRECT))
    hl57 = dp.addLink(LinkPair(name="hl57", node_source=locals()["sw1"], node_target=locals()["sw57"], type=LinkType.DIRECT))
    hl58 = dp.addLink(LinkPair(name="hl58", node_source=locals()["sw1"], node_target=locals()["sw58"], type=LinkType.DIRECT))
    hl59 = dp.addLink(LinkPair(name="hl59", node_source=locals()["sw1"], node_target=locals()["sw59"], type=LinkType.DIRECT))
    hl60 = dp.addLink(LinkPair(name="hl60", node_source=locals()["sw1"], node_target=locals()["sw60"], type=LinkType.DIRECT))




    hl62 = dp.addLink(LinkPair(name="hl62", node_source=locals()["sw2"], node_target=locals()["sw3"], type=LinkType.DIRECT))
    hl63 = dp.addLink(LinkPair(name="hl63", node_source=locals()["sw2"], node_target=locals()["sw4"], type=LinkType.DIRECT))
    hl64 = dp.addLink(LinkPair(name="hl64", node_source=locals()["sw2"], node_target=locals()["sw5"], type=LinkType.DIRECT))
    hl65 = dp.addLink(LinkPair(name="hl65", node_source=locals()["sw2"], node_target=locals()["sw6"], type=LinkType.DIRECT))
    hl66 = dp.addLink(LinkPair(name="hl66", node_source=locals()["sw2"], node_target=locals()["sw7"], type=LinkType.DIRECT))
    hl67 = dp.addLink(LinkPair(name="hl67", node_source=locals()["sw2"], node_target=locals()["sw8"], type=LinkType.DIRECT))
    hl68 = dp.addLink(LinkPair(name="hl68", node_source=locals()["sw2"], node_target=locals()["sw9"], type=LinkType.DIRECT))
    hl69 = dp.addLink(LinkPair(name="hl69", node_source=locals()["sw2"], node_target=locals()["sw10"], type=LinkType.DIRECT))
    hl71 = dp.addLink(LinkPair(name="hl71", node_source=locals()["sw2"], node_target=locals()["sw11"], type=LinkType.DIRECT))
    hl72 = dp.addLink(LinkPair(name="hl72", node_source=locals()["sw2"], node_target=locals()["sw12"], type=LinkType.DIRECT))
    hl73 = dp.addLink(LinkPair(name="hl73", node_source=locals()["sw2"], node_target=locals()["sw13"], type=LinkType.DIRECT))
    hl74 = dp.addLink(LinkPair(name="hl74", node_source=locals()["sw2"], node_target=locals()["sw14"], type=LinkType.DIRECT))
    hl75 = dp.addLink(LinkPair(name="hl75", node_source=locals()["sw2"], node_target=locals()["sw15"], type=LinkType.DIRECT))
    hl76 = dp.addLink(LinkPair(name="hl76", node_source=locals()["sw2"], node_target=locals()["sw16"], type=LinkType.DIRECT))
    hl77 = dp.addLink(LinkPair(name="hl77", node_source=locals()["sw2"], node_target=locals()["sw17"], type=LinkType.DIRECT))
    hl78 = dp.addLink(LinkPair(name="hl78", node_source=locals()["sw2"], node_target=locals()["sw18"], type=LinkType.DIRECT))
    hl79 = dp.addLink(LinkPair(name="hl79", node_source=locals()["sw2"], node_target=locals()["sw19"], type=LinkType.DIRECT))
    hl80 = dp.addLink(LinkPair(name="hl80", node_source=locals()["sw2"], node_target=locals()["sw20"], type=LinkType.DIRECT))
    hl81 = dp.addLink(LinkPair(name="hl81", node_source=locals()["sw2"], node_target=locals()["sw21"], type=LinkType.DIRECT))
    hl82 = dp.addLink(LinkPair(name="hl82", node_source=locals()["sw2"], node_target=locals()["sw22"], type=LinkType.DIRECT))
    hl83 = dp.addLink(LinkPair(name="hl83", node_source=locals()["sw2"], node_target=locals()["sw23"], type=LinkType.DIRECT))
    hl84 = dp.addLink(LinkPair(name="hl84", node_source=locals()["sw2"], node_target=locals()["sw24"], type=LinkType.DIRECT))
    hl85 = dp.addLink(LinkPair(name="hl85", node_source=locals()["sw2"], node_target=locals()["sw25"], type=LinkType.DIRECT))
    hl86 = dp.addLink(LinkPair(name="hl86", node_source=locals()["sw2"], node_target=locals()["sw26"], type=LinkType.DIRECT))
    hl87 = dp.addLink(LinkPair(name="hl87", node_source=locals()["sw2"], node_target=locals()["sw27"], type=LinkType.DIRECT))
    hl88 = dp.addLink(LinkPair(name="hl88", node_source=locals()["sw2"], node_target=locals()["sw28"], type=LinkType.DIRECT))
    hl89 = dp.addLink(LinkPair(name="hl89", node_source=locals()["sw2"], node_target=locals()["sw29"], type=LinkType.DIRECT))
    hl90 = dp.addLink(LinkPair(name="hl90", node_source=locals()["sw2"], node_target=locals()["sw30"], type=LinkType.DIRECT))
    hl91 = dp.addLink(LinkPair(name="hl91", node_source=locals()["sw2"], node_target=locals()["sw31"], type=LinkType.DIRECT))
    hl92 = dp.addLink(LinkPair(name="hl92", node_source=locals()["sw2"], node_target=locals()["sw32"], type=LinkType.DIRECT))
    hl93 = dp.addLink(LinkPair(name="hl93", node_source=locals()["sw2"], node_target=locals()["sw33"], type=LinkType.DIRECT))
    hl94 = dp.addLink(LinkPair(name="hl94", node_source=locals()["sw2"], node_target=locals()["sw34"], type=LinkType.DIRECT))
    hl95 = dp.addLink(LinkPair(name="hl95", node_source=locals()["sw2"], node_target=locals()["sw35"], type=LinkType.DIRECT))
    hl96 = dp.addLink(LinkPair(name="hl96", node_source=locals()["sw2"], node_target=locals()["sw36"], type=LinkType.DIRECT))
    hl97 = dp.addLink(LinkPair(name="hl97", node_source=locals()["sw2"], node_target=locals()["sw37"], type=LinkType.DIRECT))
    hl98 = dp.addLink(LinkPair(name="hl98", node_source=locals()["sw2"], node_target=locals()["sw38"], type=LinkType.DIRECT))
    hl99 = dp.addLink(LinkPair(name="hl99", node_source=locals()["sw2"], node_target=locals()["sw39"], type=LinkType.DIRECT))
    hl100 = dp.addLink(LinkPair(name="hl100", node_source=locals()["sw2"], node_target=locals()["sw40"], type=LinkType.DIRECT))
    hl101 = dp.addLink(LinkPair(name="hl101", node_source=locals()["sw2"], node_target=locals()["sw41"], type=LinkType.DIRECT))
    hl102 = dp.addLink(LinkPair(name="hl102", node_source=locals()["sw2"], node_target=locals()["sw42"], type=LinkType.DIRECT))
    hl103 = dp.addLink(LinkPair(name="hl103", node_source=locals()["sw2"], node_target=locals()["sw43"], type=LinkType.DIRECT))
    hl104 = dp.addLink(LinkPair(name="hl104", node_source=locals()["sw2"], node_target=locals()["sw44"], type=LinkType.DIRECT))
    hl105 = dp.addLink(LinkPair(name="hl105", node_source=locals()["sw2"], node_target=locals()["sw45"], type=LinkType.DIRECT))
    hl106 = dp.addLink(LinkPair(name="hl106", node_source=locals()["sw2"], node_target=locals()["sw46"], type=LinkType.DIRECT))
    hl107 = dp.addLink(LinkPair(name="hl107", node_source=locals()["sw2"], node_target=locals()["sw47"], type=LinkType.DIRECT))
    hl108 = dp.addLink(LinkPair(name="hl108", node_source=locals()["sw2"], node_target=locals()["sw48"], type=LinkType.DIRECT))
    hl109 = dp.addLink(LinkPair(name="hl109", node_source=locals()["sw2"], node_target=locals()["sw49"], type=LinkType.DIRECT))
    hl110 = dp.addLink(LinkPair(name="hl110", node_source=locals()["sw2"], node_target=locals()["sw50"], type=LinkType.DIRECT))
    hl111 = dp.addLink(LinkPair(name="hl111", node_source=locals()["sw2"], node_target=locals()["sw51"], type=LinkType.DIRECT))
    hl112 = dp.addLink(LinkPair(name="hl112", node_source=locals()["sw2"], node_target=locals()["sw52"], type=LinkType.DIRECT))
    hl113 = dp.addLink(LinkPair(name="hl113", node_source=locals()["sw2"], node_target=locals()["sw53"], type=LinkType.DIRECT))
    hl114 = dp.addLink(LinkPair(name="hl114", node_source=locals()["sw2"], node_target=locals()["sw54"], type=LinkType.DIRECT))
    hl115 = dp.addLink(LinkPair(name="hl115", node_source=locals()["sw2"], node_target=locals()["sw55"], type=LinkType.DIRECT))
    hl116 = dp.addLink(LinkPair(name="hl116", node_source=locals()["sw2"], node_target=locals()["sw56"], type=LinkType.DIRECT))
    hl117 = dp.addLink(LinkPair(name="hl117", node_source=locals()["sw2"], node_target=locals()["sw57"], type=LinkType.DIRECT))
    hl118 = dp.addLink(LinkPair(name="hl118", node_source=locals()["sw2"], node_target=locals()["sw58"], type=LinkType.DIRECT))
    hl119 = dp.addLink(LinkPair(name="hl119", node_source=locals()["sw2"], node_target=locals()["sw59"], type=LinkType.DIRECT))
    hl120 = dp.addLink(LinkPair(name="hl120", node_source=locals()["sw2"], node_target=locals()["sw60"], type=LinkType.DIRECT))

    hl121 = dp.addLink(LinkPair(name="hl121", node_source=locals()["sw3"], node_target=locals()["sw4"], type=LinkType.DIRECT))
    hl122 = dp.addLink(LinkPair(name="hl122", node_source=locals()["sw3"], node_target=locals()["sw5"], type=LinkType.DIRECT))
    hl123 = dp.addLink(LinkPair(name="hl123", node_source=locals()["sw3"], node_target=locals()["sw6"], type=LinkType.DIRECT))
    hl124 = dp.addLink(LinkPair(name="hl124", node_source=locals()["sw3"], node_target=locals()["sw7"], type=LinkType.DIRECT))
    hl125 = dp.addLink(LinkPair(name="hl125", node_source=locals()["sw3"], node_target=locals()["sw8"], type=LinkType.DIRECT))
    hl126 = dp.addLink(LinkPair(name="hl126", node_source=locals()["sw3"], node_target=locals()["sw9"], type=LinkType.DIRECT))
    hl127 = dp.addLink(LinkPair(name="hl127", node_source=locals()["sw3"], node_target=locals()["sw10"], type=LinkType.DIRECT))
    hl128 = dp.addLink(LinkPair(name="hl128", node_source=locals()["sw3"], node_target=locals()["sw11"], type=LinkType.DIRECT))
    hl129 = dp.addLink(LinkPair(name="hl129", node_source=locals()["sw3"], node_target=locals()["sw12"], type=LinkType.DIRECT))
    hl130 = dp.addLink(LinkPair(name="hl130", node_source=locals()["sw3"], node_target=locals()["sw13"], type=LinkType.DIRECT))
    hl130 = dp.addLink(LinkPair(name="hl130", node_source=locals()["sw3"], node_target=locals()["sw13"], type=LinkType.DIRECT))
    hl130 = dp.addLink(LinkPair(name="hl130", node_source=locals()["sw3"], node_target=locals()["sw13"], type=LinkType.DIRECT))
    hl130 = dp.addLink(LinkPair(name="hl130", node_source=locals()["sw3"], node_target=locals()["sw13"], type=LinkType.DIRECT))
    hl130 = dp.addLink(LinkPair(name="hl130", node_source=locals()["sw3"], node_target=locals()["sw13"], type=LinkType.DIRECT))
    hl130 = dp.addLink(LinkPair(name="hl130", node_source=locals()["sw3"], node_target=locals()["sw13"], type=LinkType.DIRECT))
    hl130 = dp.addLink(LinkPair(name="hl130", node_source=locals()["sw3"], node_target=locals()["sw13"], type=LinkType.DIRECT))
    hl130 = dp.addLink(LinkPair(name="hl130", node_source=locals()["sw3"], node_target=locals()["sw13"], type=LinkType.DIRECT))
    hl130 = dp.addLink(LinkPair(name="hl130", node_source=locals()["sw3"], node_target=locals()["sw13"], type=LinkType.DIRECT))
    hl130 = dp.addLink(LinkPair(name="hl130", node_source=locals()["sw3"], node_target=locals()["sw13"], type=LinkType.DIRECT))
    hl130 = dp.addLink(LinkPair(name="hl130", node_source=locals()["sw3"], node_target=locals()["sw13"], type=LinkType.DIRECT))





    hl01 = dp.addLink(LinkPair(name="hl01", node_source=h1, node_target=sw1, type=LinkType.HOST))
    hl02 = dp.addLink(LinkPair(name="hl02", node_source=h2, node_target=sw10, type=LinkType.HOST))
    hl03 = dp.addLink(LinkPair(name="hl03", node_source=h3, node_target=sw15, type=LinkType.HOST))
    hl04 = dp.addLink(LinkPair(name="hl04", node_source=h4, node_target=sw20, type=LinkType.HOST))
    hl05 = dp.addLink(LinkPair(name="hl05", node_source=h5, node_target=sw25, type=LinkType.HOST))
    hl06 = dp.addLink(LinkPair(name="hl06", node_source=h6, node_target=sw30, type=LinkType.HOST))
    hl07 = dp.addLink(LinkPair(name="hl07", node_source=h7, node_target=sw35, type=LinkType.HOST))
    hl08 = dp.addLink(LinkPair(name="hl08", node_source=h8, node_target=sw40, type=LinkType.HOST))
    hl09 = dp.addLink(LinkPair(name="hl09", node_source=h9, node_target=sw45, type=LinkType.HOST))
    hl10 = dp.addLink(LinkPair(name="hl10", node_source=h10, node_target=sw50, type=LinkType.HOST))
    hl11 = dp.addLink(LinkPair(name="hl11", node_source=h11, node_target=sw55, type=LinkType.HOST))
    hl12 = dp.addLink(LinkPair(name="hl12", node_source=h12, node_target=sw60, type=LinkType.HOST))
    hl13 = dp.addLink(LinkPair(name="hl13", node_source=h13, node_target=sw17, type=LinkType.HOST))
    hl14 = dp.addLink(LinkPair(name="hl14", node_source=h14, node_target=sw27, type=LinkType.HOST))
    hl15 = dp.addLink(LinkPair(name="hl15", node_source=h15, node_target=sw37, type=LinkType.HOST))
    hl16 = dp.addLink(LinkPair(name="hl16", node_source=h16, node_target=sw51, type=LinkType.HOST))

    # Adding Controller

    ctl = dp.addNode(Onos(name="ctl1"))

    mgnt = "tcp:{ip}:6653".format(ip=ctl.getIpController())

    for i in range(1, aux1):
    	locals()["sw"+str(i)].setController(target=mgnt, bridge="br_oper0")

    cli = Cli(dp)
    cli.cmdloop()

    dp.stop()