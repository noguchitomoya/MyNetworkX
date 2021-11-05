import matplotlib.pyplot as plt
import networkx as nx
from getRGB import RGB
import numpy as np
from PIL import Image, ImageDraw
import matplotlib.animation as animation
import cv2


def min_max_normalization(x):
    min = x.min()
    max = x.max()
    result = (x - min) / (max - min)
    return result


def save_gif(frame, output_path):
    images = []
    for i in range(frame):
        filename = './DataDir/{:03}.png'.format(i)
        img = Image.open(filename)
        images.append(img)
    images[0].save(output_path+".gif", save_all=True, append_images=images[1:], loop=0, duration=80)

    height, width, layers = cv2.imread('./DataDir/{:03}.png'.format(1)).shape
    size = (width, height)

    codec = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(output_path+".mp4", codec, 4.0, size)

    for i in range(frame):
        img = cv2.imread('./DataDir/{:03}.png'.format(i))
        video.write(img)
    video.release()


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
        node_list = []
        for i in range(25):
            node_list.append(str(i))  # ノードの文字列が、0~24の番号
            # node_list.append(str(i)+": "+str(self.joint_feature[i])[:4])#ノードの文字列が、重要度の値（見づらいかも？）
        # node0 = "0.442"
        # node1 = "1"
        # node2 = "2"
        # node3 = "3"
        # node4 = "4"
        # node5 = "5"
        # node6 = "6"
        # node7 = "7"
        # node8 = "8"
        # node9 = "9"
        # node10 = "10"
        # node11 = "11"
        # node12 = "12"
        # node13 = "13"
        # node14 = "14"
        # node15 = "15"
        # node16 = "16"
        # node17 = "17"
        # node18 = "18"
        # node19 = "19"
        # node20 = "20"
        # node21 = "21"
        # node22 = "22"
        # node23 = "23"
        # node24 = "24"
        # node_list = [node0, node1, node2, node3, node4, node5, node6, node7, node8, node9, node10, node11,
        #              node12, node13, node14,
        #              node15, node16, node17, node18, node19, node20, node21, node22, node23, node24]
        # set color to nodes
        # for i in node_list:
        #     self.G.add_nodes_from([(i, {"color": self.rgb.color_element_0_to_1[node_list.index(i)]})])
        cmap = plt.get_cmap('viridis')  # カラーマップの種類（https://tech-market.org/matplotlib-cmap/）
        for node in range(len(node_list)):
            col = cmap(self.joint_feature[node])
            color = list((col[0], col[1], col[2]))
            # color.reverse()
            # print(color)
            self.G.add_nodes_from([(node_list[node], {"color": color})])
            # self.G.add_nodes_from([(node_list[i], {"color": self.rgb.color_element_0_to_1[i]})])

        # init edges
        self.G.add_edges_from([
            (node_list[0], node_list[1]),
            (node_list[0], node_list[12]),
            (node_list[0], node_list[16]),
            (node_list[12], node_list[13]),
            (node_list[13], node_list[14]),
            (node_list[14], node_list[15]),
            (node_list[16], node_list[17]),
            (node_list[17], node_list[18]),
            (node_list[18], node_list[19]),
            (node_list[1], node_list[20]),
            (node_list[2], node_list[20]),
            (node_list[2], node_list[3]),
            (node_list[20], node_list[8]),
            (node_list[8], node_list[9]),
            (node_list[9], node_list[10]),
            (node_list[10], node_list[11]),
            (node_list[11], node_list[23]),
            (node_list[10], node_list[24]),
            (node_list[20], node_list[4]),
            (node_list[4], node_list[5]),
            (node_list[5], node_list[6]),
            (node_list[6], node_list[7]),
            (node_list[7], node_list[21]),
            (node_list[6], node_list[22]),
            # (node0, node1),
            # (node0, node12),
            # (node0, node16),
            # (node12, node13),
            # (node13, node14),
            # (node14, node15),
            # (node16, node17),
            # (node17, node18),
            # (node18, node19),
            # (node1, node20),
            # (node2, node20),
            # (node2, node3),
            # (node20, node8),
            # (node8, node9),
            # (node9, node10),
            # (node10, node11),
            # (node11, node23),
            # (node10, node24),
            # (node20, node4),
            # (node4, node5),
            # (node5, node6),
            # (node6, node7),
            # (node7, node21),
            # (node6, node22)

        ])
        # init Coordinate
        self.pos = {
            # node0: (490, 440),
            # node1: (490, 545),
            # node2: (490, 790),
            # node3: (490, 875),
            # node4: (380, 710),
            # node5: (300, 630),
            # node6: (215, 545),
            # node7: (80, 490),
            # node8: (600, 710),
            # node9: (680, 630),
            # node10: (765, 545),
            # node11: (900, 490),
            # node12: (380, 380),
            # node13: (350, 245),
            # node14: (350, 80),
            # node15: (300, 25),
            # node16: (600, 380),
            # node17: (630, 245),
            # node18: (630, 80),
            # node19: (680, 25),
            # node20: (490, 710),
            # node21: (25, 410),
            # node22: (160, 465),
            # node23: (955, 410),
            # node24: (820, 465)
            node_list[0]: (490, 440),
            node_list[1]: (490, 545),
            node_list[2]: (490, 790),
            node_list[3]: (490, 875),
            node_list[4]: (380, 710),
            node_list[5]: (300, 630),
            node_list[6]: (215, 545),
            node_list[7]: (80, 490),
            node_list[8]: (600, 710),
            node_list[9]: (680, 630),
            node_list[10]: (765, 545),
            node_list[11]: (900, 490),
            node_list[12]: (380, 380),
            node_list[13]: (350, 245),
            node_list[14]: (350, 80),
            node_list[15]: (300, 25),
            node_list[16]: (600, 380),
            node_list[17]: (630, 245),
            node_list[18]: (630, 80),
            node_list[19]: (680, 25),
            node_list[20]: (490, 710),
            node_list[21]: (25, 410),
            node_list[22]: (160, 465),
            node_list[23]: (955, 410),
            node_list[24]: (820, 465)

        }
        nx.draw(self.G, self.pos, with_labels=True)
        self.node_color = [node["color"] for node in self.G.nodes.values()]

    def show_skelton(self):
        nx.draw(self.G, self.pos, node_color=self.node_color, with_labels=True)
        plt.show()
        # plt.savefig('figure_30.png')

    def save_skelton(self, i):
        nx.draw(self.G, self.pos, node_color=self.node_color, with_labels=True)
        plt.savefig("./DataDir/{:03d}.png".format(i))



print("start")
all_cam=np.load("./DataDir/cam_batch_32.npy")
frame = 60
for batch in range(31,32):
    print("batch is ----------------", batch)
    cam = all_cam[batch]
    cam = min_max_normalization(cam)


    for i in range(frame):
        print("batch "+str(batch)+"and frame " +str(i))
        feature = cam[i]
        s = SkeltonGraph(feature)
        s.save_skelton(i)
        del s

    save_gif(frame, "./DataDir/sample_{:03d}".format(batch))

print("end")
