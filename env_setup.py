################################################
# Sets up the Python environment.              #
# Inspired by tornado-boilerplate by bueda,    #
# and tornado-production-skeleton by bdarnell. #
################################################

import os
import site
import sys
    
base_dir = os.path.dirname(os.path.abspath(__file__))  
prev_sys_path = list(sys.path)

# The directories to add to the PYTHONPATH.
dirs = ['handlers']
for dir in dirs:
    dir_path = os.path.join(base_dir, dir)
    for sub_dir in os.listdir(dir_path):
        sub_path = os.path.join(base_dir, dir, sub_dir)
        if os.path.isdir(sub_path):
            site.addsitedir(sub_path)

# addsitedir adds its directories at the end, but we want our local stuff
# to take precedence over system-installed packages.
# See http://code.google.com/p/modwsgi/issues/detail?id=112
new_sys_path = []
for item in list(sys.path):
  if item not in prev_sys_path:
    new_sys_path.append(item)
    sys.path.remove(item)
sys.path[:0] = new_sys_path