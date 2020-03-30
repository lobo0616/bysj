# -*- coding: utf-8 -*-

import importlib
import inspect
import signal
import time
from configparser import ConfigParser


class Test(object):
    def __init__(self,
                 func_name,
                 gold_function,
                 inputs_file,
                 multiple_of_time):
        self.func_name = func_name
        self.inputs = read_inputs(inputs_file)
        self.multiple_of_time = multiple_of_time
        self.gold_func = gold_function


class Student(object):
    def __init__(self, student_id, funcs):
        self.student_id = student_id
        self.funcs = funcs
        self.score = {func_name: 0 for func_name in funcs}

    def get_total_score(self):
        return sum(s for q, s in self.score.items())

    def __str__(self):
        return self.student_id+':'+str(self.score)


class Scorer(object):
    def __init__(self, tests, students):
        self.tests = tests
        self.students = students

    def score(self):
        for student in self.students:
            print(f'Judging {student.student_id}')
            for func_name in self.tests:
                task = self.tests[func_name]
                for i, input in enumerate(task.inputs):
                    start = time.time()
                    gold_result = task.gold_func(*input)
                    end = time.time()
                    second = end - start
                    try:
                        with timeout(second * task.multiple_of_time):
                            result = student.funcs[func_name](*input)
                    except Exception as e:
                        msg = "{}: {}".format(type(e).__name__, e)
                        print(f"function {func_name:>8}: input {i} {msg}")
                        continue
                    if result == gold_result:
                        print(f'function {func_name:>8}: input {i} passed')
                        student.score[func_name] += 1
                    else:
                        print(f'function {func_name:>8}: input {i} failed')
            print(student.score)
            print('\n')


class timeout(object):
    r"""Context-manager that prevents function execution from timeout.
    Example::
        >>> @timeout(3)
        ... def f(n):
        ...     time.sleep(n)
        >>> f(5)
        >>> with timeout(3):
        ...     time.sleep(5)
    """

    def __init__(self, seconds=1):
        super(timeout, self).__init__()

        self.seconds = seconds

    def __enter__(self):
        signal.signal(signal.SIGALRM, self.handler)
        signal.setitimer(signal.ITIMER_REAL, self.seconds)

    def __exit__(self, type, value, traceback):
        signal.setitimer(signal.ITIMER_REAL, 0)

    def __call__(self, func):
        @functools.wraps(func)
        def decorate_timeout(*args, **kwargs):
            with self:
                return func(*args, **kwargs)
        return decorate_timeout

    def handler(self, signum, frame):
        raise TimeoutError(f"Execution time exceeded {self.seconds:.3}s.")


def get_functions(stu_id, func_names):
    try:
        module = importlib.import_module(stu_id)
    except Exception as e:
        return {func: None for func in func_names}
    funcs = {
        tup[0]: tup[1]
        for tup in inspect.getmembers(module, inspect.isfunction)
    }
    return funcs


def read_inputs(file):
    inputs = []
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            input = eval(line)
            inputs.append(input)
    return inputs


class Config(object):
    def __init__(self, config_file):
        self._config = ConfigParser()
        self._config.read(config_file)

    @property
    def all_tests_config(self):
        return [(v for k, v in self._config.items(section))
                for section in self._config.sections()]

    @property
    def func_names(self):
        return [self._config.get(section, 'function_name')
                for section in self._config.sections()]

    def inputs_file(self, func_name):
        return self._config.get(func_name, 'inputs_file')

    def multiple_of_time(self, func_name):
        return self._config.getint(func_name, 'multiple_of_time')
