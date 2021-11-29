import math

class Node():
    def __init__(self, parent, board, win_cnt, cis_cnt, value):
        self.parent = parent  # 双亲节点
        self.children = list()  # 子节点   应该是一个list

        self.case = board  # 每个节点储存一个棋盘状态

        self.win_cnt = 0  # 该节点的获胜次数
        self.vis_cnt = 0  # 该节点的访问次数
        self.value = 0 # 胜率，初始化为0
        self.ucb = float('inf')  # 新结点的ucb无穷大

    def cal_ucb(self, N):
        '''
        :param N: 总访问次数
        :return: UCB值
        '''

        const = 2
        return self.value/self.vis_cnt + math.sqrt(const*np.log(N) / self.vis_cnt)

    def cal_value(self):
        '''
        计算胜率： 当前结点获胜次数 / 当前结点的访问次数
        :return: 返回value值
        '''
        return self.win_cnt/self.vis_cnt



