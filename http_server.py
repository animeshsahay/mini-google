from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse as up
import rocksdb

db = rocksdb.DB("inverted_index.db", rocksdb.Options())
doc_dict = {}
with open('id_URL_pairs.txt') as fp:
	line = fp.readline()
	while line:
		pairs = line.strip("\n").split(",")
		doc_dict[pairs[0]] = pairs[1]
		line = fp.readline()
			
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

	def do_GET(self):
		self.send_response(200)
		self.end_headers()
		query = up.parse_qs(self.path[2:])
		qstrs = query["query"][0]
		self.wfile.write(bytes("\nQueried term = " + qstrs + "\n",'utf-8'))
		qstrs = qstrs.lower().split(" ")
		final_docs = []
		for qstr in qstrs:
			docs = db.get(bytes(qstr,'utf-8')).decode("utf8").split(",")
			final_docs.extend(docs)
		final_docs = list(dict.fromkeys(final_docs))
		self.wfile.write(bytes("Results:\n",'utf-8'))
		for doc in final_docs:
			self.wfile.write(bytes(doc_dict[doc] + "\n",'utf-8'))


httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()
