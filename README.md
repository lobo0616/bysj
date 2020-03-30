# Scorer

```python
$ python main.py --prog_dir examples/ --gold_py gold.py --func_info_list func_info_list.txt --verbose 0
prog_dir: the directory path that includes all the .py files
gold_py: the gold-standard .py
func_info_list: the functions to be evaluated
    File format:
        One function a line; 
        Each line has 4 fields, separated by whitespaces.
        For exmaple: 
            sum    50  10  data/two_sum.txt
            Column 0: function name   
            Column 1: total score for this function  
            Column 2: maximum time allowed for running (ratio * time_used_by_the_gold_standard_py)
            Column 3: test case file 
verbose：
    0：输出最少的信息
    1：输出较多信息
    2：输出最多信息
    
    
每一位出题老师需要准备：
    1. func_info_list.txt，每个函数一行
    2. 在gold.py中实现相应的函数的正确答案
    3. 每一个函数对应一个测试用例文件（txt）

测试用例设计：
    每行一个测试用例
    多个参数由逗号隔开
    如果只有一个参数，最后需要加一个逗号

main.py最上面有两个变量，可能需要修改：
    max_time_for_import_one_py = 3.0  
    # seconds，如果超过这个时间，会直接给学生0分：
    # 杜绝最外层的死循环和input()调用
    min_time_for_run_one_func = 0.1  # seconds, 有的时候标准函数运行时间(time_gap_sec)太小了，
    # 即使乘一个倍数(time_ratio，推荐设置为10），即，也还是会产生计时错误，索性定一个最小值：允许学生的一个函数执行的最小时间，
    # 即如果time_gap_sec*time_ratio<0.1s，那么就按0.1

学生代码中print(file=sys.stdout)的东西，我都重定向到log.stdout-output中了

如果要修改输出分数和详细信息的格式，可以看utils.py中的print_score_summary函数

没有解决的问题:
    1. 如果学生的代码中有语法错误（函数内部有的语法错误可以绕过去），
    会导致import 1830401054（学号，以此为例）错误，完全无法判卷
    2. 如果学生代码中有input函数调用，那么会导致import 1830401054超时
    （我可以用输入重定向的方法解决这个问题，但是感觉没有必要，也猜不到学生要干啥）
    

学生写代码时的注意事项我会不断整理到课程主页上：http://hlt.suda.edu.cn/index.php/Python-2018

李正华 (zhli13@suda.edu.cn)
2018.11
    

    

