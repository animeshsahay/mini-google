#Creates a DB called inverted_index and adds all the key-value mapping from the inverted_index.txt file
import rocksdb

db = rocksdb.DB("inverted_index.db", rocksdb.Options(create_if_missing=True))

filepath = 'inverted_index.txt'
batch = rocksdb.WriteBatch()
with open(filepath) as fp:
   line = fp.readline()
   strs = ""
   while line:
       line = fp.readline()
       strs = line.strip("\n")
       strs = strs.strip("()")
       strs = strs.split(',',1)
       batch.put(bytes(strs[0],'utf-8'), bytes(strs[-1],'utf-8'))

   print("*************** Writing ***************")
   db.write(batch)

   print("**************** Print content ****************")
   it = db.iteritems()
   it.seek_to_first()

   print(list(it))
