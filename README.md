# Hadoop

Hadoop Commands

1. Version:
Shows the version of hadoop installed.
$ hadoop version
Output:
Hadoop 3.3.1

2. Mkdir:
This command takes the <path> as an argument and creates the directory.
$ hdfs dfs -mkdir /user/dataflair/dir1
Output:
2021-07-26 20:41:45,413 WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable

3. ls:
This command displays the contents of the directory specified by <path>. It shows the name, permissions, owner, group, size and modification date of each entry.
$ hdfs dfs -ls /user/dataflair
Output:
2021-07-26 20:46:55,687 WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Found 3 items
drwxr-xr-x   - ubunta supergroup          0 2021-07-26 20:41 /user/dataflair/dir1
drwxr-xr-x   - ubunta supergroup          0 2021-07-26 19:16 /user/dataflair/dir2
drwxr-xr-x   - ubunta supergroup          0 2021-07-26 19:17 /user/dataflair/ranjith

4. put:
 This command copies the file in the local filesystem to the file in DFS.
$ hdfs dfs -put /home/ubunta/sample.txt /user/dataflair/dir1
 
5. copyFrom Local:
This command is similar to put command. But the source should refer to local file.
$ hdfs dfs -copyFromLocal sample.txt /user/dataflair/dir1
 
6. Get:
This Hadoop shell command copies the file in HDFS identified by <src> to file in local file system identified by <localdest>.
$ hdfs dfs -get /user/dataflair/dir1 /home/ubunta
 
7. copyToLocal:
It is similar to get command. Only the difference is that in this the destination of copied file should refer to a local file.
$ hdfs dfs -copyToLocal /user/dataflair/dir1

8. Cat:
This Hadoop Shell Command displays the contents of file on console or stdout.
$ hdfs dfs -cat /user/dataflair/dir1/sample.txt
9. Mv:
This Hadoop shell command moves the file from the specified source to destination within HDFS. 
$ hdfs dfs -mv /user/dataflair/dir1/sample.txt /user/dataflair/dir2
10. Cp:
This Hadoop shell command copies the file or directory from given source to destination within HDFS.
$ hdfs dfs -cp /user/dataflair/dir2/sample.txt /user/dataflair/dir1
11.rm:
The rm command removes the file present in the specified path.
$ hdfs dfs -rm -r /test




