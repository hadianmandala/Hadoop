# Hadoop Wordcount 
You can execute WordCount.java in your hadoop,
Before execute WordCount.java, make sure you have add extra classpath that will compile .java file to .class and finally become jar file<br>
Add this extra line into your .bashrc<br>
`export HADOOP_CLASSPATH=$JAVA_HOME/lib/tools.jar`<br>

* Run `.java` file in your hadoop<br>
`hadoop com.sun.tools.javac.Main WordCount.java`

* Compile your WordCount class<br>
`jar cf wc.jar WordCount*.class`

* Run your wc.jar<br>
`hadoop jar wc.jar WordCount /wordcount/input /wordcount/output`<br>
Make sure folder `/wordcount/output` doesn't exist so the output file can create the wordcount result into `/wordcount/output` folder
