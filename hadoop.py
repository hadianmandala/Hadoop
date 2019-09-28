# Install hdfs package via pip


import pandas as pd
from hdfs import InsecureClient
import os

# ===== Connect to HDFS =====
#client_hdfs = InsecureClient('hdfs_adress:web_port')
client_hdfs = InsecureClient('http://hadoop01.org:50070')

# ===== Read File in HDFS =====
with client_hdfs.read('hdfs_path_file', encoding = 'utf-8') as reader:
    df = pd.read_csv(reader,index_col=0)
print (df)

# ==== Creating a simple Pandas DataFrame =====
liste_hello = ['hello1','hello2']
liste_world = ['world1','world2']
df = pd.DataFrame(data = {'hello' : liste_hello, 'world': liste_world})
 
# ==== Writing Dataframe to HDFS =====
with client_hdfs.write('/user/hdfs/wiki/helloworld.csv', encoding = 'utf-8') as writer:
    df.to_csv(writer)
    
# ====== Reading files ======
with client_hdfs.read('/user/hdfs/wiki/helloworld.csv', encoding = 'utf-8') as reader:
    df = pd.read_csv(reader,index_col=0)
    
# ==== Getting Content Summary ====
client_hdfs.content('hdfs_path')

# ==== Remove a directory or File in HDFS ====
client_hdfs.delete('hdfs_path', recursive=False, skip_trash=True)

# ==== Create a Directory ====
client_hdfs.makedirs('hdfs_path', permission=None)

# ==== Upload FIle into HDFS ====
client_hdfs.upload('hdfs_path', 'local_path', n_threads=1, temp_dir=None, chunk_size=65536, progress=None, cleanup=True, overwrite=True)

# Source : https://hdfscli.readthedocs.io/en/latest/api.html#module-hdfs.client
