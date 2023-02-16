import os
import numpy as np
path = os.chdir('/Users/alexandrasabrio/Desktop/FLOT/flot/datasets/flownet3d/kitti_rm_ground1')
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



n = 150
k = 1
generate1=np.zeros((k,3))
generate2=np.zeros((k,3))
generate3=np.zeros((k,3))
for x in range(n):
    for c in range(k):
        for i in np.arange((-1), 1, .001):
            for j in np.arange((-1), 1, .001):
                # for future use: generate1[c] = (np.random.uniform(low=(-1), high=1),np.random.uniform(low=(-1), high=1),0)
                generate1[c] = (i,j,0)
                generate2[c] = (i,j,0)
                generate3[c] = (i,j,0)
    np.savez('000'+str(x)+'.npz', generate1, generate2, generate3)
#call val_test.py on simulation.npz
        
