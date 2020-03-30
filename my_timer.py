
import signal
import time


class MyTimer(object):
    r"""Context-manager that prevents function execution from timeout. #上下文管理器，防止函数执行超时
    Example::
        >>> @MyTimer(3)
        ... def f(n):
        ...     time.sleep(n)
        >>> f(5)
        >>> with MyTimer(3):
        ...     time.sleep(5)
    """

    def __init__(self, seconds=1):
        super(MyTimer, self).__init__()
        self.seconds = seconds

    def __enter__(self): #当这个类被with关键字执行时，就自动调用这个方法。有返回值则调用给 as 声明的变量
        signal.signal(signal.SIGALRM, self.handler)
        signal.setitimer(signal.ITIMER_REAL, self.seconds)

    def __exit__(self, type, value, traceback):
        signal.setitimer(signal.ITIMER_REAL, 0)

    def __call__(self, func):
        @functools.wraps(func) #装饰器 添加新功能 记录函数执行时间？
        def decorate_timeout(*args, **kwargs):
            with self:
                return func(*args, **kwargs)
                '''
                try:
                    ret = func(*args, **kwargs)
                    return ret
                except Exception as e:
                    raise(e)
                '''
        return decorate_timeout

    def handler(self, signum, frame):
        raise TimeoutError("Execution time exceeded %.10f seconds." % self.seconds)

