# 开发时间：2024/4/2 上午10:48
import numpy as np
import random
import networkx as nx

# 创建无向图
G = nx.Graph()
# 添加节点（节点序号从1到12）
nodes = range(1, 13)
G.add_nodes_from(nodes)

# 定义边和节点数
edges = [(1, 2), (1, 3), (1, 4), (2, 3),  (2, 4), (3, 4), (3, 5), (3, 6),
         (3, 7), (3, 8), (4, 5), (4, 6), (4, 7), (4, 8), (5, 6), (5, 9),
         (5, 10), (6, 7), (6, 9), (6, 10), (7, 8), (7, 9), (7, 10), (8, 9),
         (8, 10), (9, 11), (9, 12), (10, 11), (10, 12), (11, 12)]
#添加边
G.add_edges_from(edges)

#——————————————————————————————————————网络拓扑构建置——————————————————————————————————————
# 初始化节点数量和算力节点数量

node_num = 12
server_num = 5

#定义节点
Nodes = np.zeros((3,node_num))
Nodes[0,:] = np.arange(1,13)

node_level = np.array([1,1,2,2,3,3,3,3,4,4,5,5])
Nodes[1,:] = node_level

computing_power = np.array([200,0,0,300,800,0,0,0,0,1000,300,0])
Nodes[2,:] = computing_power
print(Nodes)

#——————————————————————————————————————构建带宽矩阵——————————————————————————————————————
# global bandwidth_matrix1
# global bandwidth_matrix

#这两行代码设置了 NumPy 和 Python 内置的 random 模块的随机种子
#使得每次运行这段代码时产生的随机数序列都是相同的，保证了结果的可重复性。
np.random.seed(3)  # reproducible
random.seed(3)

bandwidth_matrix = np.diag([1] * 12)

#1——>2、3、4
bandwidth_matrix[1][0] = 100 * np.random.randint(3, 15)
bandwidth_matrix[2][0] = 100 * np.random.randint(3, 15)
bandwidth_matrix[3][0] = 100 * np.random.randint(3, 15)

#2——>3、4
bandwidth_matrix[2][1] = 100 * np.random.randint(3, 10)
bandwidth_matrix[3][1] = 100 * np.random.randint(3, 10)

#3——>4、5、6、7、8
for i in range(3, 8):
    bandwidth_matrix[i][2] = 100 * np.random.randint(5, 9)

#4——>5、6、7、8
for i in range(4, 8):
    bandwidth_matrix[i][3] = 100 * np.random.randint(7, 12)

#5——>6、9、10
bandwidth_matrix[5][4] = 100 * np.random.randint(9, 16)
bandwidth_matrix[8][4] = 100 * np.random.randint(9, 16)
bandwidth_matrix[9][4] = 100 * np.random.randint(9, 16)

#6——>7、9、10
bandwidth_matrix[6][5] = 100 * np.random.randint(5, 10)
bandwidth_matrix[8][5] = 100 * np.random.randint(5, 10)
bandwidth_matrix[9][5] = 100 * np.random.randint(5, 10)

#7——>8、9、10
bandwidth_matrix[7][6] = 100 * np.random.randint(7, 16)
bandwidth_matrix[8][6] = 100 * np.random.randint(7, 16)
bandwidth_matrix[9][6] = 100 * np.random.randint(7, 16)

#8——>9、10
bandwidth_matrix[8][7] = 100 * np.random.randint(7, 13)
bandwidth_matrix[9][7] = 100 * np.random.randint(7, 13)

#9——>10、11、12
for i in range(9, 12):
    bandwidth_matrix[i][8] = 100 * np.random.randint(7, 12)

#10——>11、12
bandwidth_matrix[10][9] = 100 * np.random.randint(5, 10)
bandwidth_matrix[11][9] = 100 * np.random.randint(5, 10)

#11——>12
bandwidth_matrix[11][10] = 100 * np.random.randint(5, 10)

#对称
for i in range(0, 12):
    for j in range(0, 12):
        bandwidth_matrix[i][j] = bandwidth_matrix[j][i]

print(bandwidth_matrix)
#——————————————————————————————————————算力节点放置——————————————————————————————————————
# server_connection = np.zeros(12)
# server_connection[[0,3,4,9,10]] = 1
# print(server_connection)
