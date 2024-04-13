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

# 起点和终点
start_node = 1
end_node = 12

def find_top5_shortest_path(G, start_node, end_node):
    # 使用networkx找出所有简单路径
    all_paths = list(nx.all_simple_paths(G, source=start_node, target=end_node))

    # 根据路径长度排序
    sorted_paths = sorted(all_paths, key=lambda path: len(path) - 1)

    # 获取前5条最短的路径（如果不足5条，则选择所有）
    top_5_shortest_paths = sorted_paths[:5]

    # 如果找到的路径数量少于5条，则只返回找到的路径
    paths_set = all_paths[:5] if len(all_paths) >= 5 else all_paths

    # for index, path in enumerate(top_5_shortest_paths, start=1):
    #     print(f"Path {index}: {path}, Length: {len(path) - 1}")

    num_paths = len(paths_set)
    #print("\nNumber of shortest paths: {}".format(num_paths))

    return top_5_shortest_paths

#find_top5_shortest_path(G,start_node, end_node)

def find_shortest_path(G, start_node, end_node):
    # 找到所有最短路径
    all_shortest_paths = nx.all_shortest_paths(G, start_node, end_node)
    # print(all_shortest_paths)

    # 将所有路径转换为列表的列表，以便更容易处理
    shortest_paths_list = [list(path) for path in all_shortest_paths]
    # print(shortest_paths_list)

    shortest_path_len = len(shortest_paths_list[0])-1
    #print(f"最短路径长度为：{shortest_path_len}")

    # 打印所有最短路径
    # print("All shortest paths from {} to {}:".format(start_node, end_node))
    # for path in shortest_paths_list:
    #     print(path)

    # 统计路径的数量
    num_paths = len(shortest_paths_list)
    #print("\n最短路径数量为: {}".format(num_paths))

    return shortest_paths_list, shortest_path_len

#find_shortest_path(G,start_node, end_node)
