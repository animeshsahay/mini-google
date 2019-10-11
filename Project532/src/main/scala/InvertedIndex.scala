  import org.apache.spark.{ SparkConf, SparkContext }

  object InvertedIndex {
    def main(args: Array[String]) {
      val conf = new SparkConf().setAppName("Mini_Google_18")
        .setMaster("local")
      val sc = new SparkContext(conf)

      sc.wholeTextFiles("/data").flatMap {
        case (docId, content) =>
          content
            .toLowerCase()
            // Split the docs by space and commas
            .split("[ ,]") map {
            // Create a tuple of (word, filePath)
            wordId => (wordId, docId)
          }
      }.map {
        case (wordId, docId) => (wordId, docId.split("/").last.replace(".txt", ""))
      }.reduceByKey {
        // Group all (word, doc) pairs and sum the counts
        case (a, b) => a + "," + b
      }.groupBy {
        // Group by words
        case (wordId, docId) => wordId
      }.map {
        case (wordId, list) => list.mkString(", ")
      }.saveAsTextFile("/out")
    }
  }
