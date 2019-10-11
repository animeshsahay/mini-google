# Queries the RocksDB with inverted index and outputs the URLs of the corresponding docIDs.
import rocksdb

db = rocksdb.DB("inverted_index.db", rocksdb.Options())

doc_dict = {}
with open('id_URL_pairs.txt') as fp:
	line = fp.readline()
	while line:
		pairs = line.strip("\n").split(",")
		doc_dict[pairs[0]] = pairs[1]
		line = fp.readline()

rp = open("results.txt", "w")
with open('query.txt') as fp:
	line = fp.readline()
	while line:
		line = line.strip("\n")
		rp.write("\nQueried term = " + line + "\n")
		qstrs = line.lower().split(" ")
		final_docs = []
		for qstr in qstrs:
			docs = db.get(bytes(qstr,'utf-8')).decode("utf8").split(",")
			final_docs.extend(docs)
		final_docs = list(dict.fromkeys(final_docs))
		rp.write("Results:\n")
		for doc in final_docs:
			rp.write(doc_dict[doc] + "\n")
		line = fp.readline()
