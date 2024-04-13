import numpy as np
import random
import pandas as pd
import math
#——————————————————————————————————————网络拓扑构建置——————————————————————————————————————
# 初始化节点数量和算力节点数量
node_num = 12
server_node_num = 5

# global bandwidth_matrix1
# global bandwidth_matrix

#这两行代码设置了 NumPy 和 Python 内置的 random 模块的随机种子
#使得每次运行这段代码时产生的随机数序列都是相同的，保证了结果的可重复性。
# np.random.seed(3)  # reproducible
# random.seed(3)

#——————————————————————————————————————计算任务生成——————————————————————————————————————
class NetworkTask:
    def __init__(self, task_id, priority, source, destination, task_size, bandwidth, delay_req):
        self.task_id = task_id
        self.priority = priority
        self.source = source
        self.destination = destination
        self.task_size = task_size
        self.bandwidth = bandwidth
        self.delay_req = delay_req

priorities = [3, 2, 1]
nodes = [1, 2, 3, 4, 5,6,7,8,9,10,11,12]
server_nodes = [1,4,5,10,11]
tasks = []

task_num = 10

for k in range(task_num):
    task_id = k + 1
    priority = random.choice(priorities)
    source = random.choice(nodes)
    if source == 1 or source == 2:
        destination = 1
    elif source == 3 or source == 4:
        destination = 4
    elif source == 5 or source == 6:
        destination = 5
    elif source == 7 or source == 8:
        destination = 8
    elif source == 9 or source == 10:
        destination = 10
    else:
        destination = 11
    # while destination == source:
    #     destination = random.choice(nodes)
    task_size = random.choice([i for i in range(500, 6001, 500)])
    bandwidth = random.choice([i for i in range(50, 500, 50)])
    delay_req = task_size // bandwidth
    task = NetworkTask(task_id,priority, source, destination, task_size, bandwidth, delay_req)
    tasks.append(task)



# for task in tasks:
#     print(f"任务编号:{task.task_id}, 优先级：{task.priority}，源节点：{task.source}，目的节点：{task.destination}，"
#           f"任务大小：{task.task_size}，带宽需求：{task.bandwidth}，时延要求：{task.delay_req}")

# 提取每个任务的属性并转换为矩阵（DataFrame）
data = []
for task in tasks:
    data.append({
        'task_id': task.task_id,
        'priority': task.priority,
        'source': task.source,
        'destination': task.destination,
        'task_size': task.task_size,
        'bandwidth': task.bandwidth,
        'delay_req': task.delay_req
    })

# 创建DataFrame
task_df = pd.DataFrame(data)
print(task_df)
task_metrix = task_df.values
#print(task_metrix[0])

# 显示矩阵
#print(task_metrix)