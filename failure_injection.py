# 开发时间：2024/4/2 下午3:28
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


def inject_link_failure(graph, edge_to_remove):
    if graph.has_edge(*edge_to_remove):
        graph.remove_edge(*edge_to_remove)
        print(f"Link failure injected: {edge_to_remove} has been removed.")
    else:
        print(f"Edge {edge_to_remove} does not exist in the graph.")

    # 重新计算最短路径的函数

def recalculate_shortest_paths(graph, source, target):
    # 使用 networkx 的 all_shortest_paths 函数找到所有最短路径
    # 注意：all_shortest_paths 在某些情况下可能非常慢，因为需要遍历所有可能的路径
    # 如果只关心单条最短路径，可以使用 shortest_path
    all_paths = nx.all_shortest_paths(graph, source=source, target=target)
    return list(all_paths)

# 注入链路故障
faulty_edge = (4, 6)  # 假设 (4, 6) 是故障的链路
inject_link_failure(G, faulty_edge)

# 重新计算并打印最短路径集合
start_node = 1
end_node = 12
shortest_paths_after_failure = recalculate_shortest_paths(G, start_node, end_node)

# 转换所有路径生成器到列表的列表，以便处理
shortest_paths_after_failure_list = [list(path) for path in shortest_paths_after_failure]

# 打印所有最短路径
print("Shortest paths from {} to {} after link failure:".format(start_node, end_node))
for path in shortest_paths_after_failure_list:
    print(path)

# 统计路径的数量
num_paths_after_failure = len(shortest_paths_after_failure_list)
print("\nNumber of shortest paths after link failure: {}".format(num_paths_after_failure))