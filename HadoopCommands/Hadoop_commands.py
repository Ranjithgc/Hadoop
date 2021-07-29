"""
@Author: Ranjith G C
@Date: 2021-07-28
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-28 
@Title : Program Aim is to work with Hadoop commands.
"""

import subprocess

def run_cmd(args_list):
        """
        Description:
                run linux commands.
        Parameter: 
                it takes args_list as parameter.
        Return:
                it returns s_return, s_output, s_err.
        """
        print('Running system command: {0}'.format(' '.join(args_list)))
        proc = subprocess.Popen(args_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        s_output, s_err = proc.communicate()
        s_return =  proc.returncode
        return s_return, s_output, s_err 

if __name__ == "__main__":
    #Run Hadoop mkdir command in python
    mkdir = run_cmd(['hdfs', 'dfs', '-mkdir', '-p', '/data/test/ranjith'])
    
    #Run Hadoop ls command in Python
    ls = run_cmd(['hdfs', 'dfs', '-ls', '/data/test'])

    #Run Hadoop put command in Python
    put = run_cmd(['hdfs', 'dfs', '-put', '/home/ubunta/Desktop/Hadoop_Python/sample.txt', '/data/test/ranjith'])

    #Run Hadoop copyFromLocal command in Python
    copyFromLocal = run_cmd(['hdfs', 'dfs', '-copyFromLocal', 'sample1.txt', '/data/test/ranjith'])

    #Run Hadoop get command in Python
    get = run_cmd(['hdfs', 'dfs', '-get', '/data/test/ranjith/sample1.txt', '/home/ubunta'])
                      
    #Run Hadoop copyToLocal command in Python
    copyToLocal = run_cmd(['hdfs', 'dfs', '-copyToLocal', '/data/test/ranjith/sample.txt'])

    #Run Hadoop mv command in python
    mv = run_cmd(['hdfs', 'dfs', '-mv', '/data/test/ranjith/sample1.txt', '/user/data/abc'])

    #Run Hadoop cp command in python
    cp = run_cmd(['hdfs', 'dfs', '-cp', '/user/data/abc/sample1.txt', '/data/test/ranjith'])

    #Run Hadoop moveFromLocal command in python
    moveFromLocal = run_cmd(['hdfs', 'dfs', '-moveFromLocal', 'sample2.txt', '/data/test/ranjith'])

    #Run Hadoop rm command in python
    # rm command used to remove directories
    rm = run_cmd(['hdfs', 'dfs', '-rm', '-r', '/test'])










                       







