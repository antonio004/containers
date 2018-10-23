#!/usr/bin/python

#GraphML-Topo-to-VSDNEmul-Network-Generator
#
# This file parses Network Topologies in GraphML format from the Internet Topology Zoo.
# Files have to be in the same directory.
#
# Arguments:
#   -f              [filename of GraphML input file]
#   --file          [filename of GraphML input file]
#   -o              [filename of GraphML output file]
#   --output        [filename of GraphML output file]
#   -lw             [type link of whitebox(DIRECT, HOST, VIRTUAL, WIFI)]
#   --link_whitebox [type link of whitebox(DIRECT, HOST, VIRTUAL, WIFI)]
# Without any input, program will terminate.
# Without specified output, outputfile will have the same name as the input file.
#
#################################################################################



import xml.etree.ElementTree as ET
import sys
import math
import re
from sys import argv

input_file_name = ''
output_file_name = ''
link  = ''
link_type = ''

# first check commandline arguments
for i in range(len(argv)):

    if argv[i] == '-f':
        input_file_name = argv[i+1]
    if argv[i] == '--file':
        input_file_name = argv[i+1]
    if argv[i] == '-o':
        output_file_name = argv[i+1]
    if argv[i] == '--output':
        output_file_name = argv[i+1]
    if argv[i] == '-lw':
        link = argv[i+1]
    if argv[i] == '--link':
        link = argv[i+1]
    if argv[i] == '-tl':
        link_type = argv[i+1]
    if argv[i] == '--link_type':
        link_type = argv[i+1]

def getLink(link):
    if(link) == '':
        link='LinkPair'
    return link

def getLinktype(link_type):
    if (link_type) == '':
        link_type = 'DIRECT'

    return link_type

# terminate when inputfile is missing
if input_file_name == '':
    sys.exit('\n\tNo input file was specified as argument....!')

# define string fragments for output later on
outputstring_1 = '''#!/usr/bin/python

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
'''

outputstring_2a='''
    # add nodes, switches first...
'''
outputstring_2b='''
    # ... and now hosts
'''

outputstring_3a='''
    # add edges between switch and corresponding host
'''

outputstring_3b='''
    # add edges between switches
'''

outputstring_4b='''
    # Connecting Switchs on Controller
'''


#WHERE TO PUT RESULTS
outputstring_to_be_exported = ''
outputstring_to_be_exported += outputstring_1

#READ FILE AND DO ALL THE ACTUAL PARSING IN THE NEXT PARTS
xml_tree    = ET.parse(input_file_name)
namespace   = "{http://graphml.graphdrawing.org/xmlns}"
ns          = namespace # just doing shortcutting, namespace is needed often.

#GET ALL ELEMENTS THAT ARE PARENTS OF ELEMENTS NEEDED LATER ON
root_element    = xml_tree.getroot()
graph_element   = root_element.find(ns + 'graph')

# GET ALL ELEMENT SETS NEEDED LATER ON
index_values_set    = root_element.findall(ns + 'key')
node_set            = graph_element.findall(ns + 'node')
edge_set            = graph_element.findall(ns + 'edge')

# SET SOME VARIABLES TO SAVE FOUND DATA FIRST
# memomorize the values' ids to search for in current topology
node_label_name_in_graphml = ''
node_latitude_name_in_graphml = ''
node_longitude_name_in_graphml = ''
# for saving the current values
node_index_value     = ''
node_name_value      = ''
node_longitude_value = ''
node_latitude_value  = ''
# id:value dictionaries
id_node_name_dict   = {}     # to hold all 'id: node_name_value' pairs
id_longitude_dict   = {}     # to hold all 'id: node_longitude_value' pairs
id_latitude_dict    = {}     # to hold all 'id: node_latitude_value' pairs

# FIND OUT WHAT KEYS ARE TO BE USED, SINCE THIS DIFFERS IN DIFFERENT GRAPHML TOPOLOGIES
for i in index_values_set:

    if i.attrib['attr.name'] == 'label' and i.attrib['for'] == 'node':
        node_label_name_in_graphml = i.attrib['id']
    if i.attrib['attr.name'] == 'Longitude':
        node_longitude_name_in_graphml = i.attrib['id']
    if i.attrib['attr.name'] == 'Latitude':
        node_latitude_name_in_graphml = i.attrib['id']

# NOW PARSE ELEMENT SETS TO GET THE DATA FOR THE TOPO
# GET NODE_NAME DATA
# GET LONGITUDE DATK
# GET LATITUDE DATA
for n in node_set:

    node_index_value = n.attrib['id']

    #get all data elements residing under all node elements
    data_set = n.findall(ns + 'data')

    #finally get all needed values
    for d in data_set:

        #node name
        if d.attrib['key'] == node_label_name_in_graphml:
            #strip all whitespace from names so they can be used as id's
            node_name_value = re.sub(r'\s+', '', d.text)
        #longitude data
        if d.attrib['key'] == node_longitude_name_in_graphml:
            node_longitude_value = d.text
        #latitude data
        if d.attrib['key'] == node_latitude_name_in_graphml:
            node_latitude_value = d.text

        #save id:data couple
        id_node_name_dict[node_index_value] = node_name_value
        id_longitude_dict[node_index_value] = node_longitude_value
        id_latitude_dict[node_index_value]  = node_latitude_value


# STRING CREATION
# FIRST CREATE THE SWITCHES AND HOSTS
tempstring1 = ''
tempstring2 = ''
tempstring3 = ''

for i in range(0, len(id_node_name_dict)):

    #create switch
    temp1 =  '    '
    temp1 += id_node_name_dict[str(i)]
    temp1 += " = dp.addNode(Whitebox(name='"
    temp1 += id_node_name_dict[str(i)]
    temp1 += "'))\n"

    #create corresponding host
    temp2 =  '    Host_'
    temp2 += id_node_name_dict[str(i)]
    temp2 += " = dp.addNode(Host(name='Host_"
    temp2 += id_node_name_dict[str(i)]
    temp2 += "'"
    temp2 += ", ip='10.0.0."
    temp2 += str(i+1)
    temp2 += "'"
    temp2 += ", mask='24"
    temp2 += "'))\n"
    tempstring1 += temp1
    tempstring2 += temp2

    # link each switch and its host...
    temp3 =  '    '
    temp3 +=  "link_host"
    temp3 += str(i)
    temp3 += " = dp.addLink(LinkPair(name='link_host" #criar funcao para pegar o tipo de link futuramente
    temp3 += str(i)
    temp3 += "'"
    temp3 += ", node_source="
    temp3 += id_node_name_dict[str(i)]
    temp3 += ' , '
    temp3 += "node_target= Host_"
    temp3 += id_node_name_dict[str(i)]
    temp3 += ' , '
    temp3 += "type="
    temp3 += "LinkType.HOST"
    temp3 += "))"
    temp3 += '\n'
    tempstring3 += temp3

outputstring_to_be_exported += outputstring_2a
outputstring_to_be_exported += tempstring1
outputstring_to_be_exported += outputstring_2b
outputstring_to_be_exported += tempstring2
outputstring_to_be_exported += outputstring_3a
outputstring_to_be_exported += tempstring3
outputstring_to_be_exported += outputstring_3b

# SECOND CALCULATE DISTANCES BETWEEN SWITCHES,
#   and link each single host to its corresponding switch

tempstring4 = ''
tempstring5 = ''
z=0
for e in edge_set:

    # GET IDS FOR EASIER HANDLING
    src_id = e.attrib['source']
    dst_id = e.attrib['target']

    # ... and link all corresponding switches with each other
    temp4 =  '    '
    temp4 +=  "link_wh"
    temp4 += str(z)
    temp4 += " = dp.addLink("
    temp4 += getLink(link) 
    temp4 += "(name='link_wh" #criar funcao para pegar o tipo de link futuramente
    temp4 += str(z)
    temp4 += "'"
    temp4 += ", node_source="
    temp4 += id_node_name_dict[src_id]
    temp4 += ' , '
    temp4 += "node_target="
    temp4 += id_node_name_dict[dst_id]
    temp4 += ' , '
    temp4 += "type="
    temp4 += "LinkType."
    temp4 += getLinktype(link_type).upper()
    temp4 += "))"
    temp4 += '\n'
    tempstring4 += temp4
    z +=1

outputstring_to_be_exported += tempstring4

for i in range(0, len(id_node_name_dict)):
    # ... Conecting each switch on Onos controller
    temp5 =  '    '
    temp5 += id_node_name_dict[str(i)]
    temp5 += '.'
    temp5 += "setController(target=mgnt, bridge='br_oper0')"
    temp5 += '\n'
    tempstring5 += temp5

outputstring_to_be_exported += outputstring_4b
outputstring_to_be_exported += tempstring5


outputstring_5a='''
    #showing cli interface
    cli = Cli(dp)
    cli.cmdloop()

    #stop and close all nodes
    dp.stop()
'''
outputstring_to_be_exported += outputstring_5a

# GENERATION FINISHED, WRITE STRING TO FILE
outputfile = ''
if output_file_name == '':
    output_file_name = input_file_name + 'vSDNemul-topology.py'

outputfile = open(output_file_name, 'w')
outputfile.write(outputstring_to_be_exported)
outputfile.close()

print "Topology generation SUCCESSFUL!"
