import os  #操作系统模块接口，和文件目录相关
import importlib #import 的实现，第一个目的是在 Python 源代码中提供 import 语句的实现（并且因此而扩展 __import__() 函数）。 这提供了一个可移植到任何 Python 解释器的 import 实现。 相比使用 Python 以外的编程语言实现方式，这一实现更加易于理解。第二个目的是实现 import 的部分被公开在这个包中，使得用户更容易创建他们自己的自定义对象 (通常被称为 importer) 来参与到导入过程中。
import inspect #inspect模块用于收集python对象的信息，可以获取类或函数的参数的信息，源码，解析堆栈，对对象进行类型检查等等
import re #正则表达式
import sys 

'''
const_func_name = 'name'
const_func_score = 'score'
const_func_max_run_time_ratio = 'max_run_time_ratio'
const_func_test_case_file_name = 'test_case_file_name'
'''

def get_all_lines(file_name): #读文件
    with open(file_name, mode='r', encoding='utf-8') as f: 
        return f.readlines()


def get_func_info(file_name): #获取函数名及分数和各自的测试用例
    all_func_info = []
    all_lines = get_all_lines(file_name)
    for line in all_lines:
        tokens = re.split('\s+', line.strip()) #strip()去除首尾空格，按照空格分割字符串
        sz = len(tokens)
        if sz == 4: #tokens[0]函数名；tokens[1]分数；tokens[2]总分；tokens[3]测试文件
            all_func_info.append((tokens[0], float(tokens[1]), float(tokens[2]), tokens[3])) # + '.test_cases.txt'})
        else:
            print("error line: %s in %s (%d tokens)" % (line, file_name, sz), file=sys.stderr) #sys.stderr返回错误信息
    return all_func_info

def get_name_info(sut_no,file_name):  #新增 读取学生信息文件 获取名字
    #all_stu_info = []
    stu_name = ""
    all_stu_lines = get_all_lines(file_name)
    for line in all_stu_lines:
         stuInfo = re.split(',', line.strip())
         zd = len(stuInfo)
         if zd == 2:
             #all_stu_info.append((stuInfo[0],stuInfo[1]))
             if sut_no == stuInfo[0]:
                    stu_name = stuInfo[1]
         else:
             print("error line: %s in %s (%d tokens)" % (line, file_name, zd), file=sys.stderr)
    
    return stu_name

def remove_py_suffix(py_file_name): #去掉文件的.py后缀
    return re.sub('\.py$', '', py_file_name) if py_file_name.endswith('.py') else py_file_name


def get_student_py_list(dir_name): #返回没有.py后缀的学生文件列表
    py_list_wo_suffix = []  # no .py suffix
    all_files = os.listdir(dir_name) #返回指定路径下的文件和文件夹列表。
    for file_name in all_files:
        if file_name.count(' ') > 0 or file_name.count('\t') > 0: #文件名不能包含空格
            print('file name contains space: #%s#' % file_name)
            exit(-1)
        if os.path.isfile(os.path.join(dir_name, file_name)):#join把目录和文件名合成一个路径，然后判断路径是否为文件
            if file_name.lower().endswith('.py'): #判断后缀是否为.py
                if file_name[-2:].lower() != file_name[-2:]:  # .PY .Py .pY -> .py
                    file_name_new = file_name[:-2] + file_name[-2:].lower()
                    os.rename(os.path.join(dir_name, file_name), os.path.join(dir_name, file_name_new))
                    file_name = file_name_new
            py_list_wo_suffix.append(remove_py_suffix(file_name))
    return py_list_wo_suffix


def get_funcs_in_one_module(module_name, verbose): 
    try:
        this_module = importlib.import_module(module_name)#动态导入模块对象
        return {tup[0]:tup[1] for tup in inspect.getmembers(this_module, inspect.isfunction)}#返回一个包含对象的所有成员的(name, value)列表，是一个函数才返回？
    except Exception as e: #发生异常执行这一块代码
        if verbose > 1:
            print('import module %s error: %s %s' % (module_name, type(e).__name__, e), file=sys.stderr) #返回错误信息
        return None


def print_score_summary(py_name, stu_name, total_score, func_names, func_scores):
    assert len(func_scores) == len(func_names) #检查长度是否相等
    print('%15s %s %5.1f -> ' % (py_name, stu_name, total_score), end='', file=sys.stderr) #输出总分数
    for name, score in zip(func_names, func_scores): #zip()打包为元祖的列表
        print('%15s %5.1f\t' % (name, score), end='', file=sys.stderr) #输出每一个函数得分
    print(flush=True, file=sys.stderr) #flush = True时它会立即把内容刷新

#输出信息
def print_func_score_verbose_1(py_name, stu_name, func_name, score, correct_case_cnt, total_case_cnt, verbose):
    if verbose > 0:
        print('Total score of %s  %s for func %s: %.1f = %.1f*(%.1f/%.1f)' %
              (py_name, stu_name, func_name, score*correct_case_cnt/total_case_cnt, score, correct_case_cnt, total_case_cnt),
              flush=True, file=sys.stderr)


def print_msg_verbose_2(py_name,func_name, i_input, msg, verbose):
    if verbose > 1:
        print('student %s function %s: input %d: %s' % (py_name, func_name, i_input, msg), flush=True, file=sys.stderr)


def print_a_thing_verbose_1(msg, verbose):
    if verbose > 0:
        print(msg, flush=True, file=sys.stderr)

