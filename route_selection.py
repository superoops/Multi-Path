# 开发时间：2024/4/2 下午3:46
#from task_generation import task_metrix
import random
import networkx as nx
import numpy as np
from find_shortest_path import *

task_1 = [1,1,3,4,6000,400,15]
#——————————————————————————————————————网络拓扑构建置——————————————————————————————————————
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
#print(Nodes)


#计算综合指数，选择最优目标节点
def choose_computing_node(G, task, computing_power):
    task_size = task[4]
    start_node = task[2]
    end_node = task[3]
    # 找到所有大于等于业务算力需求的算力节点及其算力
    indices_enough_power = np.array([])#算力节点集合索引
    values_enough_power = np.array([])#算力节点的算力值
    for i in range(12):
        if computing_power[i] >= task_size / 50:
            indices_enough_power = np.append(indices_enough_power, i+1)
            values_enough_power = np.append(values_enough_power,computing_power[i])
    print(indices_enough_power)
    print(values_enough_power)

    num_server = len(indices_enough_power)

    if num_server == 0:
        print("算力不足，该任务无法被调度")
    else:
        score = np.zeros((1, num_server))  # 综合指数初始化全0
        find_shortest_path(G, start_node, end_node)
        find_top5_shortest_path(G, start_node, end_node)

        for i in range(num_server):
            shortest_paths_list, shortest_path_len = find_shortest_path(G, start_node, indices_enough_power[i])  # 获取所有最短路径,以及最短路径长度
        num_hop = shortest_path_len
        score[0, i] = values_enough_power[i] / num_hop  # 综合指数与剩余算力成正比，与最短路径跳数成反比，具体的计算方法后面再修改

    max_index = np.argmax(score)
    end_node = indices_enough_power[max_index]  # 更新目的节点

    return end_node


def route_selection(G, task,bandwidth_matrix, computing_power):

    start_node = task[2]
    end_node = choose_computing_node(G, task, computing_power)
    route = []

    if task[1] == 3:
        paths_set = find_top5_shortest_path(G, start_node, end_node)
        main_path = paths_set[0]
        backup_path = paths_set[1]
        route = [main_path, backup_path]
    elif task[1] == 1:
        paths_set = find_top5_shortest_path(G, start_node, end_node)
        main_path = paths_set[0]
        backup_path = []
        route = [main_path, backup_path]
    elif task[1] == 2:
        route = find_path_for_prio2(G, task,bandwidth_matrix, computing_power)

    return route

def find_path_for_prio2(G, task):

    global bandwidth_matrix
    global computing_power
    task_size = task[4]
    start_node = task[2]
    demand_power = task_size / 50
    # 检查链路剩余带宽是否符合要求
    original_bandwidth = bandwidth_matrix
    demand_bandwidth = task[5]
    demand_matrix = np.full((12,12), demand_bandwidth)
    # 删除不满足带宽需求的边,更新G
    for u, v in list(G.edges()):
        if original_bandwidth[u - 1, v - 1] < demand_matrix[u - 1, v - 1]:
            G.remove_edge(u, v)
    main_end_node = choose_computing_node(G, task, computing_power)
    top5_shortest_path_mian = find_top5_shortest_path(G, start_node, main_end_node)
    main_path = top5_shortest_path_mian[0]

    # 选择主路径后，更新算力节点剩余算力
    computing_power[main_end_node-1] = computing_power[main_end_node-1] - demand_power

    # 选择主路径后，更新带宽矩阵
    path_len = len(main_path)
    for i in range(path_len-1):
        # 获取当前节点和下一个节点的索引
        current_node = main_path[i]
        next_node = main_path[i + 1]
        # 更新带宽矩阵中对应链路的带宽值
        # 注意：由于是无向图，所以两个方向都需要更新
        bandwidth_matrix[current_node, next_node] -= demand_matrix
        bandwidth_matrix[next_node, current_node] -= demand_matrix

    # 删除主路径，更新图G
    for u, v in zip(main_path[:-1], main_path[1:]):
        G.remove_edge(u, v)

    # 选择备份路径目标节点
    backup_end_node = choose_computing_node(G, task, computing_power)
    top5_shortest_path_backup = find_top5_shortest_path(G, start_node, backup_end_node)
    backup_path = top5_shortest_path_backup[0]

    # 更新带宽矩阵
    # 待补充

    path = [main_path, backup_path]

    return path



End_Node = choose_computing_node(G,task_1, computing_power)
print(f"最优的目标节点为：{End_Node}")




