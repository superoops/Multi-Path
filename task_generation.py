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
#np.random.seed(3)  # reproducible
#random.seed(3)

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

for k in range(10):
    task_id = k + 1
    priority = random.choice(priorities)
    source = random.choice(nodes)
    destination = random.choice(server_nodes)
    while destination == source:
        destination = random.choice(nodes)
    task_size = random.choice([i for i in range(500, 2001, 500)])
    bandwidth = random.choice([i for i in range(300, 500, 50)])
    delay_req = random.randint(10, 1000) * task_size // 2000
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

# 显示DataFrame
#print(task_metrix)