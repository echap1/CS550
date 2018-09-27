import sys
import numpy as np

num_list = [int(x) for x in str(sys.argv[1])]
val_list = np.array(num_list[::-1]) * 2 ** np.array(range(len(num_list)))

print(sum(val_list))