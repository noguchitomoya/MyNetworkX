# ↑jupter notebookで使用する場合のマジックコマンド
import matplotlib.pyplot as plt
import networkx as nx

# Graphオブジェクトの作成
G = nx.Graph()

# nodeデータの追加
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

# G.add_nodes_from(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18","19", "20","21", "22", "23", "24"])
G.add_nodes_from(
    [node0, node1, node2, node3, node4, node5, node6, node7, node8, node9, node10, node11, node12, node13, node14,
     node15, node16, node17, node18, node19, node20, node21, node22, node23, node24])
# edgeデータの追加
G.add_edges_from([
    (node0, node1),
    (node0, node12)
])

pos = {
    node0: (490,460),
    node1: (490, 355),
    node2: (490, 110),
    node3: (490, 25),
    node4: (0, 0),
    node5: (5, 5),
    node6: (0, 0),
    node7: (5, 5),
    node8: (0, 0),
    node9: (5, 5),
    node10: (0, 0),
    node11: (5, 5),
    node12: (380, 520),
    node13: (350, 655),
    node14: (350, 820),
    node15: (300, 875),
    node16: (600, 520),
    node17: (630, 655),
    node18: (630, 820),
    node19: (680, 875),
    node20: (490, 190),
    node21: (5, 5),
    node22: (0, 0),
    node23: (5, 5),
    node24: (5, 5)


}
# ネットワークの可視化
nx.draw(G, pos )
plt.show()
