Steps for Executing Word Count Program in Hadoop :

Step 1: 

Create a file with the name word_count_data.txt  and add some data to it.
$ cd lengthwordcount
$ touch matrix1.txt
$ touch matrix2.txt

Step 2: 

Create a mapper.py file that implements the mapper logic. It will read the data from STDIN and will split the lines into words, and will generate an output of each word with its individual count. 
Let’s test our mapper.py locally that it is working fine or not.
Syntax:
cat <text_data_file> | python <mapper_code_python_file>
To Run Command(in my case)
cat *.txt | python mapper.py
Step 3:

Create a reducer.py file that implements the reducer logic. It will read the output of mapper.py from STDIN(standard input) and will aggregate the occurrence of each word and will write the final output to STDOUT. 
To Run Command(in my case):
Now let’s check our reducer code reducer.py with mapper.py is it working properly or not with the help of the below command.
cat *.txt | python mapper.py | sort -k1,1 | python reducer.py

Step 4: 

Now let’s start all our Hadoop daemons with the below command.
$ start-all.sh

Now make a directory word_count_in_python in our HDFS in the root directory that will store our word_count_data.txt file with the below command.
$ hdfs dfs -mkdir /matrix_multiplication

Copy word_count_data.txt to this folder in our HDFS with help of copyFromLocal command.
$  hdfs dfs -copyFromLocal ~/Documents/*.txt /matrix_multiplication

Now our data file has been sent to HDFS successfully. we can check whether it sends or not by using the below command or by manually visiting our HDFS. 
$ hdfs dfs -ls /length    # list down content of /word_count_python directory

Let’s give executable permission to our mapper.py and reducer.py with the help of the below command.
$ chmod 777 mapper.py reducer.py


Step 5: 
Now download the latest hadoop-streaming jar file from this Link. Then place, this Hadoop,-streaming jar file to a place from you can easily access it. In my case, I am placing it to /Documents folder where mapper.py and reducer.py file is present.
$ hadoop jar /home/ubunta/hadoop-3.3.1/share/hadoop/tools/lib/hadoop-streaming-jar-3.3.1 \
> -mapper /home/ubunta/Desktop/Matrix_Multiplication/mapper.py -mapper "python3 mapper.py" \
> -reducer /home/ubunta/Desktop/Matrix_Multiplication/reducer.py -reducer "python3 reducer.py" \
> -input /matrix_multiplication/*.txt \
> -output /matrix_multiplication/output 

Now let’s run our python files with the help of the Hadoop streaming utility as shown below.
$ hdfs dfs -cat /matrix_multiplication/output/part-00000

In the above command in -output, we will specify the location in HDFS where we want our output to be stored. So let’s check our output in output file at location /word_count_in_python/output/part-00000 in my case. We can check results by manually vising the location in HDFS or with the help of cat command as shown below.













