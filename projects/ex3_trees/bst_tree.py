#!/usr/bin/python3
"""script that implements Binary Search Tree and Adelson-Velsky-Landis Tree

[TBD]
"""

import random
import time
import gc

from matplotlib import pyplot as plt

class BST:
    '''Binary Search Tree Structure'''
    def __init__(self, key = None, val = None):
        self.right = None
        self.left = None
        self.key = key
        self.val = val
        self.size = 1

    def __str__(self):
        print("TBD")
    
    def insert(self, key, val = None):
        if not self.key:
            self.key = key
            self.value = val
            return
        
        if self.key == key:
            return

        if key < self.key:
            if self.left:
                self.left.insert(key, val)
                return
            self.left = BST(key = key, val = val)
            self.size = self.size + 1
            return
        
        if self.right:
            self.right.insert(key, val)
            return
        self.right = BST(key, val)
        self.size = self.size + 1
        return

    def search(self, key):
        '''Searches for the key. If key exists, 
           then it returns key and value, otherwise 
           returns False.'''
        if key == self.key:
            return (self.key, self.key)

        if key < self.key:
            if self.left == None:
                return False
            return self.left.search(key)

        if self.right == None:
            return False
        return self.right.search(key)

    def delete(self, key):
        if self == None:
            return self

        if key < self.key:
            if self.left:
                self.left = self.left.delete(key)
            return self

        if key > self.key:
            if self.right:
                self.right = self.right.delete(key)
            return self

        if self.right == None:
            return self.left
        
        if self.left == None:
            return self.right

        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.key = min_larger_node.key
        self.right = self.right.delete(min_larger_node.key)
        return self

    def print(self, level = 0):
        if self:
            if self.right:
                self.right.print(level + 1)
            print(' ' * 4 * level + '->', self.key)
            if self.left:
                self.left.print(level + 1)

def list_generator(min_val, max_val, n):
    # print(f'Min: {min_val}, Max: {max_val}, N: {n}')
    return random.sample(range(min_val, max_val + 1), n)

if __name__ == "__main__":
    
    number_of_nodes = range(1000, 10001, 1000)

    min_val = 1
    max_val = 1000

    creating_time = []
    searching_time = []
    deleting_time = []

    gc_old = gc.isenabled() # garbage collector state
    gc.disable() # disable garbage collector before measuring execution times

    for i in number_of_nodes:
        tree = BST()

        # keys_list = list_generator(min_val, max_val, i)
        keys_list = list_generator(min_val, i, i)
        start = time.process_time()
        for j in keys_list:
            tree.insert(j)
        stop = time.process_time()
        creating_time.append(stop-start)
        print(f'Czas tworzenia {i} elementów drzewa: {creating_time[-1]}')

        start = time.process_time()
        for j in keys_list:
            tree.search(j)
        stop = time.process_time()
        searching_time.append(stop-start)
        print(f'Czas wyszukiwania {i} elementów drzewa: {searching_time[-1]}')

        start = time.process_time()
        for j in keys_list:
            tree.delete(j)
        stop = time.process_time()
        deleting_time.append(stop-start)
        print(f'Czas usuwania {i} elementów drzewa: {deleting_time[-1]}')

    if gc_old: gc.enable() # restore garbage collector initial state
