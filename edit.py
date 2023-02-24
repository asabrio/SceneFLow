import os
import numpy as np
import subprocess
#import pandas as pd
path = os.chdir('C:\\Users\\a.sabrio\\Desktop\\FLOT\\flot\\datasets\\flownet3d\\kitti_rm_ground')
##direct = 'kitti_rm_ground'
folder = sorted(os.listdir(path))

'''this is for shuffling an array'''
files = [f for f in os.listdir(path) if f.endswith(".npz")]

# for file in files:
#     a=np.load(file)
#     pos2 = a['pos2'].copy()
#     np.random.shuffle(pos2)
#     new_a = {'gt': a['gt'], 'pos2':pos2, 'pos1':a['pos1']}
#     new_file = os.path.splitext(file)[0] + '.npz'
#     np.savez(new_file, **new_a)

    
#this is for adding/subtracting epsilon
# for file in folder:
#     epsilon = .001  # np.random.normal(loc=0.0, scale=1.0, size=None)
#     with np.load(file) as data:
#         arr0 = data['gt']
#         arr1 = data['pos2']
#         arr2 = data['pos1']
#         arr1 += epsilon
#     np.savez(file, gt=arr0, pos2=arr1, pos1=arr2)


#now making a modified array and passing into val_test.py for each value of epsilon


# Define the function to modify the array
def modify_array(arr, epsilon):
    modified_arr = arr.copy()  # make a copy of the array to modify
    modified_arr[:, 1] += epsilon  # add epsilon to the 2nd column
    # Perform any other desired modifications here
    return modified_arr

# Set the path to the folder containing the .npz files
path = 'C:\\Users\\a.sabrio\\Desktop\\FLOT\\flot\\datasets\\flownet3d\\kitti_rm_ground'
script_path = 'C:\\Users\\a.sabrio\\Desktop\\FLOT\\flot\\scripts\\val_test.py'
# Set the range of epsilon values to test
epsilons = np.arange((-1), 1, .001)

largest_result = None
largest_epsilon = None 

# Loop through all the .npz files in the folder
for file in os.listdir(path):
   # if not filename.endswith('.npz'):
       # continue
    filepath = os.path.join(path, file)
    with np.load(filepath) as data:
        gt = data['gt']
        pos2 = data['pos2']
        pos1 = data['pos1']
        for epsilon in epsilons:
            # Modify the pos2 array using the modify_array function
            modified_pos2 = modify_array(pos2, epsilon)
            # Convert the modified_pos2 array to a byte string
            modified_pos2_bytes = modified_pos2.tobytes()
            # Execute the external script with the modified arrays as input
            result = subprocess.run(['python', script_path], input=modified_pos2_bytes, capture_output=True)
            if result.returncode == 0:
                result_value = result.stdout.decode().strip()
                if result_value:
                    result_float = float(result_value)
                    if result_float > best_result:
                        best_result = result_float
                        best_epsilon = epsilon
           # result_value = float(result.stdout.decode().strip())
            #if largest_result is None or result_value > largest_result:
               # largest_result = result_value
             #   largest_epsilon = epsilon
    # Save the original arrays back to the .npz file
    np.savez(filepath, gt=gt, pos2=pos2, pos1=pos1)
print('Largest epsilon:', best_epsilon)
print('Largest EPE:', best_result)


        
    
    
    
    
    
    
    
    # a = np.load(file) #allow_pickle=True)
    # key = list(a.keys())
    # for i in key:
    #     if key=='pos2':
    #         for i in a[key]:
    #             a[key]=a[key]+epsilon
                
    #             np.savez(a)


#just generate 1 single cell arrays and copy it 150 times to get it working 
# n = 150
# k = 10
# pos1=np.zeros((k,3))
# pos2=np.zeros((k,3))
# gt=np.zeros((k,3))
# for x in range(n):
#     for c in range(k):
#         epsilon = np.random.normal(loc=0.0, scale=1.0, size=None)
#         for i in np.arange((-1), 1, .001):
#             for j in np.arange((-1), 1, .001):
#                 # for future use: generate1[c] = (np.random.uniform(low=(-1), high=1),np.random.uniform(low=(-1), high=1),0)
#                 pos1[c] = (epsilon+.001,epsilon,0)
#                 pos2[c] = (epsilon+.001,epsilon,0)
#                 gt[c] = (epsilon+.001,epsilon,0)
                
#     #x = np.array([[pos1],[pos2],[gt]])
#     #panda_df = pd.DataFrame(data = x, 
#                         #columns = ["pos1", "pos", "gt"])
#     #a = to_numpy(panda_df)
                
#     np.savez('000'+str(x)+'.npz', gt=gt, pos2=pos2, pos1=pos1)
# #call val_test.py on simulation.npz
# #pd.writecv or something to get it back to numpy
