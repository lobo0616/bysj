import sys   #sys.argv 是一个包含命令行参数的列表 sys.path 包含了一个 Python 解释器自动查找所需模块的路径的列表
import argparse #argparse 是python自带的命令行参数解析包，可以用来方便地读取命令行参数
import time 

from utils import *
from my_timer import MyTimer

max_time_for_import_one_py = 3.0  # seconds
min_time_for_run_one_func = 0.1  # seconds, sometimes time_gap_sec*time_ratio (for gold.py) is too small


def evaluate_one_py(py_name, all_func_info, stu_name, gold_funcs, verbose):
    if verbose > 0: 
        print('\nStart evaluating %s %s'%( py_name,stu_name), flush=True, file=sys.stderr)
    try:
        with MyTimer(max_time_for_import_one_py): 
            this_funcs = get_funcs_in_one_module(py_name, verbose) #将学生代码的函数提取出来
    except Exception as e:
        print_a_thing_verbose_1('import module %s timeout: %s %s' % (py_name, type(e).__name__, e), verbose)

    total_score = 0.  
    func_scores = []
    func_names = []
    for (func_name, score, time_ratio, test_case_file_name) in all_func_info: #批阅的函数名 分数 测试用例文件 时间？
        func_names.append(func_name)
        if this_funcs is None: #判断是否有函数
            func_scores.append(0.)
            print_a_thing_verbose_1('module %s does not contain func: %s' % (py_name, func_name), verbose)
            continue
        correct_case_cnt = 0. 
        lines = get_all_lines(test_case_file_name)  #读文件，测试用例文件
        total_case_cnt = len(lines)  #测试用例个数
        gold_func = gold_funcs.get(func_name) #返回gold文件里的特定的函数名(要评分的那些函数）
        assert gold_func is not None #检查函数名
        if this_funcs.get(func_name) is None: 
            lines = [] #如果没有相符合的函数名 测试用例文件也没有相符合的
        for i_input, one_input in enumerate(lines):#enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标 i是下标，one是数据
            one_input_line = one_input.strip() #移除空格换行符
            assert len(one_input_line) > 0 #检查长度
            one_input = eval(one_input_line) #eval() 函数用来执行一个字符串表达式，并返回表达式的值（字符串转为列表）
            one_input_for_sys = eval(one_input_line) 
            start_time = time.time() 
            gold_result = gold_func(*one_input) #将测试用例放入函数里执行？（数组第一个元素？）
            end_time = time.time() 
            time_gap_sec = end_time - start_time #执行时间

            try:
                with MyTimer(max(time_gap_sec * time_ratio, min_time_for_run_one_func)):
                    result = this_funcs[func_name](*one_input_for_sys) #将测试用例放到学生函数里执行？
            except Exception as e:  #发生异常执行这一块
                print_msg_verbose_2(py_name, func_name, i_input, '%s : %s' % (type(e).__name__, e), verbose)
                continue
            if gold_result is None: 
                print(*one_input, gold_result)
            if result == gold_result: #判断学生结果和答案结果是否相等
                correct_case_cnt += 1 #通过的正确的测试用例个数+1
                print_msg_verbose_2(py_name, func_name, i_input, 'passed', verbose) 
            else:
                print_msg_verbose_2(py_name, func_name, i_input, 'failed', verbose)
        this_func_score = score * correct_case_cnt / total_case_cnt #分数就是通过的用例/总用例
        func_scores.append(this_func_score) #函数的得分列表
        total_score += this_func_score #总分数
        print_func_score_verbose_1(py_name, stu_name, func_name, score, correct_case_cnt, total_case_cnt, verbose)
    print_score_summary(py_name,stu_name, total_score, func_names, func_scores) 


if __name__ == '__main__':
    argparser = argparse.ArgumentParser() #创建解析器
    argparser.add_argument('--prog_dir', default='examples/') #添加参数
    argparser.add_argument('--gold_py', default='gold.py')
    argparser.add_argument('--func_info_list', default='func_info_list.txt')
    argparser.add_argument('--verbose', type=int, default=0)
    argparser.add_argument('--student',default='student.csv')  #新增文件 学号和姓名
    args, extra_args = argparser.parse_known_args() #解析参数。
	#当仅获取到基本设置时，如果运行命令中传入了之后才会获取到的其他配置，不会报错；而是将多出来的部分保存起来，留到后面使用
    sys.path.insert(0, args.prog_dir) #新添加的目录会优先于其他目录被import检查
    all_func_info = get_func_info(args.func_info_list) #该函数在utils.py中，获取要评阅的函数名及分数和各自的测试用例
    #all_student_info =get_name_info(args.student) #获取学生学号 姓名 
    py_list = get_student_py_list(args.prog_dir) #该函数在utils.py中，返回没有.py后缀的学生文件列表
    gold_py = remove_py_suffix(args.gold_py.lower()) #该函数在utils.py中，lower()大写转成小写,去掉参考答案文件后缀
    gold_funcs = get_funcs_in_one_module(gold_py, args.verbose) #该函数在utils.py中，返回gold_py的函数
    assert gold_funcs is not None #assert（断言）用于判断一个表达式，在表达式条件为 false 的时候触发异常。
    with open('log.stdout-outputs', 'w') as f:
        sys.stdout = f #sys.stdout的形式就是print的一种默认输出格式，等于print "%VALUE%"
        for one_py in py_list: #学生代码文件夹
            print("学号：", one_py)
            stu_name = get_name_info(one_py,args.student)
            print("姓名：", stu_name)
            evaluate_one_py(one_py, all_func_info, stu_name, gold_funcs, args.verbose)


