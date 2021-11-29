# 蒙特卡洛搜索树
# 娄新宇
# 最后一次修改：2021.11.29


import Node
import time
import random

class MCTS(self):
    def __init__(self,board):
        self.root = Node(parent = None, board = board)

    def MCTS_search(self):
        start = time.time()
        while time.time() - start < 5:  # 5s内做出决策
            leaf = selection(root)
            simulation = roll_out(leaf)  # 直到终态，返回终态节点
            back_proppagation(leaf, simulation)  # 从终态节点向上回溯
        return best_children


    def roll_out(self, node):
        if node.case.is_terminal():
            # 如果此节点为终态，返回此节点
            return node
        # simulation
        # 杏姐


    def selection(self, node):
        '''
        :param node: 输入当前所在的节点
        :return: 返回叶子结点
        '''
        if node.children == []:
            # True: It's a leaf node
            return node
        # 当前结点不是叶子结点，选择UCB最大的子节点继续向下寻找
        ch_ucb = [i.cal_ucb(self.root.vis_cnt) for i in node.children]
        #max_node = []   # 考虑到可能出现多个UCB最大的结点
        max_pos_u = [i for i in range(len(ch_ucb)) if ch_ucb[i] == max(ch_ucb)]
        return self.selection(node.children[random.randint(0, len(max_pos_u)-1)])


    def back_propagation(self, node):
        '''
        :param node: 输入当前结点
        :function: 向上回溯，更新双亲结点的value和访问次数
        无返回值
        '''
        node.win_cnt += 1
        node.vis_cnt += 1
        node.value = node.cal_value()
        if node.parent:
            back_propagation(node.parent)

    def best_children(self, root):
        '''
        :param node: 根节点
        :return: 最好的落子
        '''
        ch_value = [i.value for i in root.children]
        max_pos_v = [i for i in range(len(ch_value)) if ch_value[i] == max(ch_value)]
        # 若有多个最大value，随机返回一个
        return node.children[random.randint(0, len(max_pos_v) - 1)]


