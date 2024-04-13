# import networkx as nx
# import numpy as np
# import random
# from find_shortest_path import *
#
# # 创建无向图
# G = nx.Graph()
# # 添加节点（节点序号从1到12）
# nodes = range(1, 13)
# G.add_nodes_from(nodes)
#
# # 定义边和节点数
# edges = [(1, 2), (1, 3), (1, 4), (2, 3),  (2, 4), (3, 4), (3, 5), (3, 6),
#          (3, 7), (3, 8), (4, 5), (4, 6), (4, 7), (4, 8), (5, 6), (5, 9),
#          (5, 10), (6, 7), (6, 9), (6, 10), (7, 8), (7, 9), (7, 10), (8, 9),
#          (8, 10), (9, 11), (9, 12), (10, 11), (10, 12), (11, 12)]
# #添加边
# G.add_edges_from(edges)
# find_shortest_path(G,start_node, end_node)
# #——————————————————————————————————————构建带宽矩阵——————————————————————————————————————
# # global bandwidth_matrix1
# # global bandwidth_matrix
#
# #这两行代码设置了 NumPy 和 Python 内置的 random 模块的随机种子
# #使得每次运行这段代码时产生的随机数序列都是相同的，保证了结果的可重复性。
# np.random.seed(3)  # reproducible
# random.seed(3)
#
# bandwidth_matrix = np.diag([1] * 12)
#
# #1——>2、3、4
# bandwidth_matrix[1][0] = 100 * np.random.randint(3, 15)
# bandwidth_matrix[2][0] = 100 * np.random.randint(3, 15)
# bandwidth_matrix[3][0] = 100 * np.random.randint(3, 15)
#
# #2——>3、4
# bandwidth_matrix[2][1] = 100 * np.random.randint(3, 10)
# bandwidth_matrix[3][1] = 100 * np.random.randint(3, 10)
#
# #3——>4、5、6、7、8
# for i in range(3, 8):
#     bandwidth_matrix[i][2] = 100 * np.random.randint(5, 9)
#
# #4——>5、6、7、8
# for i in range(4, 8):
#     bandwidth_matrix[i][3] = 100 * np.random.randint(7, 12)
#
# #5——>6、9、10
# bandwidth_matrix[5][4] = 100 * np.random.randint(9, 16)
# bandwidth_matrix[8][4] = 100 * np.random.randint(9, 16)
# bandwidth_matrix[9][4] = 100 * np.random.randint(9, 16)
#
# #6——>7、9、10
# bandwidth_matrix[6][5] = 100 * np.random.randint(5, 10)
# bandwidth_matrix[8][5] = 100 * np.random.randint(5, 10)
# bandwidth_matrix[9][5] = 100 * np.random.randint(5, 10)
#
# #7——>8、9、10
# bandwidth_matrix[7][6] = 100 * np.random.randint(7, 16)
# bandwidth_matrix[8][6] = 100 * np.random.randint(7, 16)
# bandwidth_matrix[9][6] = 100 * np.random.randint(7, 16)
#
# #8——>9、10
# bandwidth_matrix[8][7] = 100 * np.random.randint(7, 13)
# bandwidth_matrix[9][7] = 100 * np.random.randint(7, 13)
#
# #9——>10、11、12
# for i in range(9, 12):
#     bandwidth_matrix[i][8] = 100 * np.random.randint(7, 12)
#
# #10——>11、12
# bandwidth_matrix[10][9] = 100 * np.random.randint(5, 10)
# bandwidth_matrix[11][9] = 100 * np.random.randint(5, 10)
#
# #11——>12
# bandwidth_matrix[11][10] = 100 * np.random.randint(5, 10)
#
# #对称
# for i in range(0, 12):
#     for j in range(0, 12):
#         bandwidth_matrix[i][j] = bandwidth_matrix[j][i]
#
# task = [1,1,3,4,6000,800,15]
# demand_bandwith = task[5]
# demand_matrix = np.full((12,12), demand_bandwith)
# # 删除不满足带宽需求的边
# for u, v in list(G.edges()):
#     if bandwidth_matrix[u - 1, v - 1] < demand_matrix[u - 1, v - 1]:
#         G.remove_edge(u, v)
# find_shortest_path(G,start_node, end_node)
# # 更新带宽矩阵以反映图的变化
# new_bandwidth_matrix = nx.adjacency_matrix(G).toarray()
#
def remove_path_from_graph(G, path):
    """
    从无向图G中删除给定的路径，并更新图G。

    :param G: 无向图，使用字典的字典表示
    :param path: 要删除的路径，表示为节点的列表
    """
    # 遍历路径中的每个节点，并从邻接表中删除相应的链路
    for i in range(len(path) - 1):
        node1 = path[i]
        node2 = path[i + 1]

        # 从node1的邻居列表中删除node2
        if node2 in G[node1]:
            G[node1].remove(node2)

            # 由于是无向图，也需要从node2的邻居列表中删除node1
        if node1 in G[node2]:
            G[node2].remove(node1)

            # 如果路径中的节点没有其他邻居，则从图中完全删除这些节点
    for node in path:
        if not G[node]:
            del G[node]

        # 示例


G = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

path_to_remove = ['A', 'B', 'E']

print("原始图G:")
print(G)

remove_path_from_graph(G, path_to_remove)

print("删除路径后的图G:")
print(G)


