import os
import numpy as np
#import pandas as pd
path = os.chdir('/Users/alexandrasabrio/Desktop/FLOT/flot/datasets/flownet3d/kitti_rm_ground')
##direct = 'kitti_rm_ground'
##folder = sorted(os.listdir(direct))
##
##for file in folder:
##    a = np.loadtxt(file) #allow_pickle=True)
##    key = list(a.keys())
##    for i in key:
##        length = len(a[i])
##        b = np.delete(a[i],np.s_[3:length],0)
##        np.savez(b)


#just generate 1 single cell arrays and copy it 150 times to get it working 
n = 150
k = 1
pos1=np.zeros((k,3))
pos2=np.zeros((k,3))
gt=np.zeros((k,3))
for x in range(n):
    for c in range(k):
        for i in np.arange((-1), 1, .001):
            for j in np.arange((-1), 1, .001):
                # for future use: generate1[c] = (np.random.uniform(low=(-1), high=1),np.random.uniform(low=(-1), high=1),0)
                pos1[c] = (i,j,0)
                pos2[c] = (i,j,0)
                gt[c] = (i,j,0)
                
    #x = np.array([[pos1],[pos2],[gt]])
    #panda_df = pd.DataFrame(data = x, 
                        #columns = ["pos1", "pos", "gt"])
    #a = to_numpy(panda_df)
                
    np.savez('000'+str(x)+'.npz', gt=gt, pos2=pos2, pos1=pos1)
#call val_test.py on simulation.npz
#pd.writecv or something to get it back to numpy

