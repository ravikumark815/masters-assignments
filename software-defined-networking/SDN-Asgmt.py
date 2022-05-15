"""
Software Defined Networking (SSZG580)
Assignment 1
Student Name: K Ravi Kumar Reddy
Student ID: 2020MT13010
"""

from mininet.net import Mininet
from mininet.node import Host, OVSSwitch, Controller, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import setLogLevel, info
from mininet.topolib import TreeTopo

def SDN_Asgmt():
    net = Mininet(topo=None, build=False, ipBase='10.0.0.0/8', controller=RemoteController)

    info("\n> Adding Controller\n")
    c0 = net.addController(name='c0', controller=RemoteController, ip="10.0.0.200/8", port=6633)
    
    info("\n>> Adding Switches\n")
    s1_switch = net.addSwitch('s1', cls=OVSSwitch, stp=1)
    s2_switch = net.addSwitch('s2', cls=OVSSwitch, stp=1)
    s3_switch = net.addSwitch('s3', cls=OVSSwitch, stp=1)

    info("\n>> Adding Hosts\n")
    h1_node = net.addHost('h1', cls=Host, ip='10.0.0.2/8', defaultRoute='h1-eth0')
    h2_node = net.addHost('h2', cls=Host, ip='10.0.0.3/8', defaultRoute='h2-eth0')
    
    info("\n>> Adding Links\n")
    net.addLink(h1_node, s1_switch, cls=TCLink)
    net.addLink(s1_switch, s3_switch, cls=TCLink)
    net.addLink(s3_switch, h2_node, cls=TCLink)
    net.addLink(s1_switch, s2_switch, cls=TCLink)
    net.addLink(s2_switch, s3_switch, cls=TCLink)

    net.build()
    c0.start()

    s1_switch.start([c0])
    s2_switch.start([c0])
    s3_switch.start([c0])
    
    net.start()
    
    CLI(net)

if __name__ == '__main__':
    print ("--------------------------------------")
    print ("SDN Assignment 1 | BITS WILP Program")
    print ("--------------------------------------")
    print ("Student Name: K Ravi Kumar Reddy")
    print ("Student ID: 2020MT13010")
    print ("--------------------------------------\n")
    setLogLevel('info')
    SDN_Asgmt()