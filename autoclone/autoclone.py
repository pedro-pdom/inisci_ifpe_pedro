import os
import pandas as pd

forkset = pd.read_csv('datasetfork.txt', sep = '\t', header = None)
forkset.columns = ['url','owner_login', 'project_name', 'dominant_domain', 'fork']

cloneurl = forkset.url
name = forkset.project_name 

counter = 0

for x, i in zip(cloneurl, name):
  # os.system('git clone {} D:\gitrepo\{}'.format(x,i)) #the actual cloning line
  print('git clone {} D:\gitrepo\{}'.format(x,i)) # output testing
  counter+=1  
  print("This is the #{} the loop runs!".format(counter))