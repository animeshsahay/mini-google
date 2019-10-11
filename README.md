# COMPSCI532_Project1

This repository is for Project 1. Each students are required to develop a mockup of the core functionality of a Web search engine. For more details, you may refer to the project website https://marcoserafini.github.io/teaching/systems-for-data-science/fall19/project1.html

In this repository, there are 1977 documents. Each of these documents are crawled from the internet, and named as the document id. The file id_URL_pairs.txt is the mapping of document id and its URL. Each line represent one document. Your search engine are required to return the URL of the document. 

For group information, please refer to the form here (https://docs.google.com/spreadsheets/d/1FZshWm0o7_WcKcdyc9sAkdbSnUWrlALn74COMBAkWzA/edit?usp=sharing). Please create a group in GitHub Classroom with the corresponding group name shown in the form above. 

A query test plan will be provided for you to check the correctness of your program soon. 

For submission, please include the inverted index, and all the code needed to run your program. 

# Organisation of Project 
There are four major parts of the repository -
1. HDFS -
Our input file is uploaded on HDFS cluster in a directory named "/data".
2. Spark -
The InvertedIndex.scala file in /Project532 directory contains the source code for building inverted index using scala.
This takes input the input file from HDFS and creates an output file in the "/out" directory. Our indexes have been presented in a file named "Inverted_Index.txt".
Appropriate jar file named "Project532_2.11-1.0.jar" is attached to facilitate this running.
3. RockDB storage and Query -
The inverted index is stored in RockDB as a <Key, Value> pair using the file_read.py file in the repository.
The DB we created is named "inverted_index.db" and this is also uploaded as part of the code.
Querying is done on this DB using query.py file and it is currently tested with testcases provided using a text file named "queries.txt" and output is presented in "results.txt".
4. HTTP Server connection for Dynamic Querying -
In order to aid dynamic querying and testing on our search engine we have created a SimpleHttpServer that takes search query as a "Query Parameter" and returns the results.

Note : We are using scala, python3 and rocksdb installed using python3 for this project.

# Running the Engine
1. Please ensure the doc files are stored in HDFS in the "/data" directory.
2. Run Spark job for inverted indexing using the JAR file. As a reference, we used spark-submit to run our code as given below -
```
spark-submit --class InvertedIndex --master local --deploy-mode client project532_2.11-1.0.jar
```
3. View the output in HDFS in the "/out" directory.
4. Run the "file_read.py" file which loads inverted indices from the file "inverted_index.txt" into a database called "inverted_index.db".
5. Query through file by updating the "query.txt" with your query strings, each entered in a new line. The results will be loaded on to the file named "results.txt".
6. If you wish to run the HTTP Server, do so using the "http_server.py" file. This opens the port 8000 for HTTP requests. As a next step, make a http call using get and your query in this format -
```
$ http http://localhost:8000?query=string
```
If your query has more than one string, please input it as follows -
```
$ http http://localhost:8000?query=string1%20string2
```
