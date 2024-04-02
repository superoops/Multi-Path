# 开发时间：2024/4/2 下午1:56
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


# 定义函数来查找所有最短路径
def find_all_shortest_paths(graph, source, target):
    # 使用 networkx 的 all_shortest_paths 函数找到所有最短路径
    shortest_paths = nx.all_shortest_paths(graph, source=source, target=target)
    return list(shortest_paths)


# 起点和终点
start_node = 1
end_node = 12

# 找到所有最短路径
all_shortest_paths = find_all_shortest_paths(G, start_node, end_node)
#print(all_shortest_paths)

# 将所有路径转换为列表的列表，以便更容易处理
shortest_paths_list = [list(path) for path in all_shortest_paths]
#print(shortest_paths_list)

# 打印所有最短路径
print("All shortest paths from {} to {}:".format(start_node, end_node))
for path in shortest_paths_list:
    print(path)

# 统计路径的数量
num_paths = len(shortest_paths_list)
print("\nNumber of shortest paths: {}".format(num_paths))
