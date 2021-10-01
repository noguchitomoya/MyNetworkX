import matplotlib.pyplot as plt
import networkx as nx
from getRGB import RGB
import numpy as np


class SkeltonGraph:
    def __init__(self, joint_feature):
        self.joint_feature = joint_feature
        self.rgb = RGB(joint_feature)
        self.G = nx.Graph()
        self.pos = None
        self.node_color = None
        self.init_graph()

    def init_graph(self):
        # init node
        node0 = "0"
        node1 = "1"
        node2 = "2"
        node3 = "3"
        node4 = "4"
        node5 = "5"
        node6 = "6"
        node7 = "7"
        node8 = "8"
        node9 = "9"
        node10 = "10"
        node11 = "11"
        node12 = "12"
        node13 = "13"
        node14 = "14"
        node15 = "15"
        node16 = "16"
        node17 = "17"
        node18 = "18"
        node19 = "19"
        node20 = "20"
        node21 = "21"
        node22 = "22"
        node23 = "23"
        node24 = "24"
        node_list = [node0, node1, node2, node3, node4, node5, node6, node7, node8, node9, node10, node11,
                     node12, node13, node14,
                     node15, node16, node17, node18, node19, node20, node21, node22, node23, node24]
        # set color to nodes
        for i in node_list:
            self.G.add_nodes_from([(i, {"color": self.rgb.color_element_0_to_1[node_list.index(i)]})])

        # init edges
        self.G.add_edges_from([
            (node0, node1),
            (node0, node12),
            (node0, node16),
            (node12, node13),
            (node13, node14),
            (node14, node15),
            (node16, node17),
            (node17, node18),
            (node18, node19),
            (node1, node20),
            (node2, node20),
            (node2, node3),
            (node20, node8),
            (node8, node9),
            (node9, node10),
            (node10, node11),
            (node11, node23),
            (node10, node24),
            (node20, node4),
            (node4, node5),
            (node5, node6),
            (node6, node7),
            (node7, node21),
            (node6, node22)

        ])
        # init Coordinate
        self.pos = {
            node0: (490, 440),
            node1: (490, 545),
            node2: (490, 790),
            node3: (490, 875),
            node4: (380, 710),
            node5: (300, 630),
            node6: (215, 545),
            node7: (80, 490),
            node8: (600, 710),
            node9: (680, 630),
            node10: (765, 545),
            node11: (900, 490),
            node12: (380, 380),
            node13: (350, 245),
            node14: (350, 80),
            node15: (300, 25),
            node16: (600, 380),
            node17: (630, 245),
            node18: (630, 80),
            node19: (680, 25),
            node20: (490, 710),
            node21: (25, 410),
            node22: (160, 465),
            node23: (955, 410),
            node24: (820, 465)

        }

        self.node_color = [node["color"] for node in self.G.nodes.values()]

    def show_skelton(self):
        nx.draw(self.G, self.pos, node_color=self.node_color, with_labels=True)
        plt.show()


feature = np.load("joint_feature[31].npy")
s = SkeltonGraph(feature)
s.show_skelton()
