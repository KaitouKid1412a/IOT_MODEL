from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.node import RemoteController

class CustomTopo (Topo):

    def build(self):

        S1 = self.addSwitch('s1')

        H1 = self.addHost('h1')
        H2 = self.addHost('h2')

        self.addLink(S1, H1)
        self.addLink(S1, H2)


topo = CustomTopo()
net = Mininet(topo, controller=lambda name: RemoteController(name, ip='127.0.0.1', protocol='tcp', port = 6633), autoSetMacs=True)
net.start()
CLI(net)
net.stop()