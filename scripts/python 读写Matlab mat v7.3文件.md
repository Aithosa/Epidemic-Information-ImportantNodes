## python 读写Matlab mat v7.3文件

*本文链接：https://blog.csdn.net/u013701860/article/details/86189047*

主要使用了hdf5storage这个模块

比h5py更好用，而且h5py还存在读入数据维度跟matlab不一致的问题

```Python
import hdf5storage # get code on https://pypi.python.org/pypi/hdf5storage/0.1.3
import numpy as np
 
 
# 写入mat
def WriteMatlab(data_np, VarName, FileName):
    matcontent = {}
    matcontent[VarName] = data_np
    hdf5storage.write(matcontent, filename=FileName, matlab_compatible=True)
 
data_np=np.ones([3,3], dtype=np.float32)
WriteMatlab(data_np,'data_np','data_np.mat')
 
 
#读出mat
matcontent = hdf5storage.loadmat('leopard_1.mat')
InputImage1 = matcontent['leopard_1']
```



## python中处理.mat文件
 

### 背景

在实际使用python的时候，发现很多数据都是使用`.mat`的形式保存，所以，如何使用python读写`.mat`文件成为了许多python使用者必备的技能。

v7.3版本的`.mat`文件与普通版本的.mat文件读写方法不一样，将分开来介绍

### 普通.mat文件

主要借助sicpy.io中提供的两个函数`loadmat`和`savemat`.

```Python
import scipy.io as sio
import numpy as np

#load
data = sio.loadmat('data.mat')

#save
array_x = np.array([1,2,3,4])
array_y = np.array([5,6,7,8])
sio.savemat('save.mat', {'arrayX': array_x, 'arrayY': array_y})
```

### v7.3版本.mat文件

v7.3版本的`.mat`文件是matlab中保存大文件的格式，使用上面的方式是无法读取的，这个时候需要使用h5py

安装h5py:http://blog.csdn.net/GYGuo95/article/details/79537594

```Python
# 读取
import h5py

data = h5py.File('data.mat')
```