
# coding: utf-8

# # Generate network

# In[1]:
import networkx as nx

# import pandas as pd
import numpy as np
import scipy.io as scio
import hdf5storage # get code on https://pypi.python.org/pypi/hdf5storage/0.1.3

import random

# import matplotlib.pyplot as plt
# import seaborn as sns


# In[2]:
# ER = nx.random_graphs.erdos_renyi_graph(2000, 0.0015)   # n, p


# In[3]:
WS = nx.random_graphs.watts_strogatz_graph(2000, 10, 0.3)
# n - The number of nodes
# k - Each node is joined with its `k` nearest neighbors in a ring topology.
# p - The probability of rewiring each edge


# In[4]:
BA = nx.random_graphs.barabasi_albert_graph(2000, 6)
# n - Number of nodes
# m - Number of edges to attach from a new node to existing nodes


# In[5]:
BA_2000_6 = nx.to_numpy_matrix(BA)
WS_2000_10_03 = nx.to_numpy_matrix(WS)
# ER_2000_02 = nx.to_numpy_matrix(ER)

# In[6]:


def AddRandomEdge(networkMatrix, edgesToAdd):
    N = networkMatrix.shape[0]
    for _ in range(edgesToAdd):
        p1 = random.randint(0, N-1)
        p2 = random.randint(0, N-1)
        while(networkMatrix[p1, p2] == 1):
            p1 = random.randint(0, N-1)
            p2 = random.randint(0, N-1)
        networkMatrix[p1, p2] = 1
        networkMatrix[p2, p1] = 1
    return networkMatrix


# 写入mat
def WriteMatlab(data_np, VarName, FileName):
    matcontent = {}
    matcontent[VarName] = data_np
    hdf5storage.write(matcontent, filename=FileName, matlab_compatible=True)


# In[8]:
# np.savetxt('../data/BA_2000_3.csv', BA_2000_3, fmt = '%d', delimiter = ',')
# np.savetxt('../data/WS_2000_4_03.csv', WS_2000_4_03, fmt = '%d', delimiter = ',')
# # np.savetxt('../data/ER_2000_0003.csv', ER_2000_02, fmt = '%d', delimiter = ',')

scio.savemat('../data/BA_2000_6.mat', {'A': BA_2000_6})
scio.savemat('../data/WS_2000_10_03.mat', {'A': WS_2000_10_03})
# scio.savemat('../data/ER_2000_0003.mat', {'A': BA_2000_3})

# WriteMatlab(BA_2000_3,'BA_2000_3','../data/BA_2000_3_new.mat')
# WriteMatlab(BA_2000_3,'WS_2000_4_03','../data/WS_2000_4_03_new.mat')
# # WriteMatlab(BA_2000_3,'ER_2000_0003','../data/ER_2000_0003_new.mat')


# In[7]:
BA_2000_6_add_400_edges = AddRandomEdge(BA_2000_6, 400)
WS_2000_10_03_add_400_edges = AddRandomEdge(WS_2000_10_03, 400)
# ER_2000_02_add_400_edges = AddRandomEdge(ER_2000_02, 400)

# In[9]:
scio.savemat('../data/BA_2000_6_add_400_edges.mat', {'B': BA_2000_6_add_400_edges})
scio.savemat('../data/WS_2000_10_03_add_400_edges.mat', {'B': WS_2000_10_03_add_400_edges})
# scio.savemat('./data/ER_2000_02_add_400_edges.mat', {'B': ER_2000_02_add_400_edges})


# #读出mats
 
# matcontent = hdf5storage.loadmat('leopard_1.mat')
# InputImage1 = matcontent['leopard_1']

# c = scio.loadmat('./matlab.mat')
# print (type(c))
# print (c)

# d = scio.loadmat('./BA_2000_3.mat')
# print (type(d))
# print (d)