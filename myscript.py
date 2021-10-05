import numpy as np
from skeltongraph import SkeltonGraph

features = np.load("joint_feature_for_22_and_30.npy")
ans = np.load(
    '/home/noguchitomoya/Desktop/Test-env/GCN_Regression_with_CAM/misasagikai_3Djoints_data/joint_only_data/Ts_label_01.npy')
arr_with_22 = np.zeros(16 * 25).reshape((16, 25))
arr_with_30 = np.zeros(16 * 25).reshape((16, 25))
index_of_22 = 0
index_of_30 = 0
for i in range(32):
    if ans[i] == 22:  # スコアが22のとき
        arr_with_22[index_of_22] = features[i]
        index_of_22 += 1
    else:  # スコアが30のとき
        arr_with_30[index_of_30] = features[i]
        index_of_30 += 1

testgraph = SkeltonGraph(arr_with_30[0])
testgraph.show_skelton()
mean_of_22 = np.mean(arr_with_22, axis=0)
mean_of_30 = np.mean(arr_with_30, axis=0)
graph_of_22 = SkeltonGraph(mean_of_22)
graph_of_22.show_skelton()
graph_of_30 = SkeltonGraph(mean_of_30)
graph_of_30.show_skelton()

print(2)
