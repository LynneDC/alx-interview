#!/usr/bin/python3


def canUnlockAll(boxes):
    visited = set()

    def dfs(box_index):
        visited.add(box_index)

        for key in boxes[box_index]:
            if key < len(boxes) and key not in visited:
                dfs(key)
    dfs(0)
    return len(visited) == len(boxes)
