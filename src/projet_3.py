from lib.molp_log import Logger

log = Logger('OCR3', verbose=True)

def try_except(function,log=log):

    def wrapper(*args, **kwargs):
        try:
            result = function(*args, **kwargs)
        except Exception as _e:
            log.error('',args,_e,func_name=function.__name__)
            result = None
        finally:         
            return result
 
    return wrapper


def temp():
    pass

@try_except
def divide(a,b):
    return (a/b)

print(divide(10,0))


print(log.log_var)