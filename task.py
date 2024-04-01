import numpy as np
import random
import math
#——————————————————————————————————————网络拓扑构建置——————————————————————————————————————
# 初始化节点数量和算力节点数量
node_num = 12
server_node_num = 5

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
server_connection = np.zeros(12)
server_connection[[0,3,4,9,10]] = 1
print(server_connection)

#——————————————————————————————————————计算任务生成——————————————————————————————————————
class NetworkTask:
    def __init__(self, task_id, priority, source, destination, task_size, bandwidth, delay):
        self.task_id = task_id
        self.priority = priority
        self.source = source
        self.destination = destination
        self.task_size = task_size
        self.bandwidth = bandwidth
        self.delay = delay

priorities = ['高', '中', '低']
nodes = ['A', 'B', 'C', 'D', 'E']
tasks = []
number = 0

for k in range(10):
    task_id = k + 1
    priority = random.choice(priorities)
    source = random.choice(nodes)
    destination = random.choice(nodes)
    while destination == source:
        destination = random.choice(nodes)
    task_size = random.choice([i for i in range(500, 2001, 500)])
    bandwidth = random.randint(50, 200)
    delay = random.randint(10, 1000) * task_size // 2000
    task = NetworkTask(task_id,priority, source, destination, task_size, bandwidth, delay)
    tasks.append(task)


for task in tasks:
    print(f"任务编号:{task.task_id}, 优先级：{task.priority}，源节点：{task.source}，目的节点：{task.destination}，任务大小：{task.task_size}，带宽需求：{task.bandwidth}，时延要求：{task.delay}")

