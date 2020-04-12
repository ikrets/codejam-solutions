import numpy as np
from collections import namedtuple
import timeit

class Node:
    def __init__(self, left, right, top, bottom, S):
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom
        self.S = S


def build_connections(array):
    nodes = []
    flat_nodes = []

    R = len(array)
    C = len(array[0])

    for i in range(R):
        nodes.append([])
        for j in range(C):
            node = Node(None, None, None, None, array[i][j])
            nodes[i].append(node)
            flat_nodes.append(node)

    for i in range(R):
        for j in range(C):
            if j > 0:
                nodes[i][j].left = nodes[i][j - 1]
            if j < C - 1:
                nodes[i][j].right = nodes[i][j + 1]
            if i > 0:
                nodes[i][j].top = nodes[i - 1][j]
            if i < R - 1:
                nodes[i][j].bottom = nodes[i + 1][j]

    return flat_nodes

def filter_participants(nodes):
    removed = set()
    changed = set()
    S_removed = 0

    for node in nodes:
        present_nodes = [n for n in [node.left, node.right, node.top, node.bottom] if n]
        if not present_nodes:
            continue

        avg_neighbor_S = sum(n.S for n in present_nodes) / len(present_nodes)

        if node.S < avg_neighbor_S:
            removed.add(node)
            S_removed += node.S


    for n in removed:
        if n.top:
            changed.add(n.top)
            n.top.bottom = n.bottom
            if n.bottom:
                n.bottom.top = n.top
                changed.add(n.bottom)
        if n.bottom:
            changed.add(n.bottom)
            n.bottom.top = n.top
            if n.top:
                n.top.bottom = n.bottom
                changed.add(n.top)
        if n.left:
            changed.add(n.left)
            n.left.right = n.right
            if n.right:
                n.right.left = n.left
                changed.add(n.right)
        if n.right:
            changed.add(n.right)
            n.right.left = n.left
            if n.left:
                n.left.right = n.right
                changed.add(n.left)

    
    return S_removed, changed - removed
            
def solve(array):
    participants = build_connections(array)
    interest = sum(n.S for n in participants)
    total_interest = 0

    changed = participants

    while True:
        S_removed, changed = filter_participants(changed)
        total_interest += interest

        if S_removed == 0:
            return total_interest

        interest -= S_removed

T = int(input())

for t in range(T):
    R, C = [int(n) for n in input().split(' ')]
    array = []
    for r in range(R):
        array.append([int(S) for S in input().split(' ')])

    total_interest = solve(array)
    print('Case #{}: {}'.format(t + 1, total_interest))
