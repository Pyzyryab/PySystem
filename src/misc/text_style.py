class TextStyle:
    '''
    Base class. All children classes are basically decorators.
    Each action (color or format) is ONE decorator (instead one fn that receives all availiable options
    by parameter, and then produces a result as option.)
    The idea behind this option represented as a funtion, is just to call the decorator, and in order to KNOW what
    options are availiable the autocomplete (usually Ctrl + space) will show you those options,
    availiable options inmediatly, reducing the error-prone way to pass something as parameter.
    Not always less is better.
    '''
    ENDC = '\033[0m'

    @staticmethod
    def action(function):
        def wrapper():
            fn = function()
            if isinstance(fn, str):
                return f'TextActionChoice{fn}{TextStyle.ENDC}'
            else:
                return fn
        return wrapper


class TextFormat(TextStyle):
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @staticmethod
    def bold_format(function):
        def wrapper():
            print('bold format got called')
            fn = function()
            if isinstance(fn, str):
                return f'{TextFormat.BOLD}{fn}{TextStyle.ENDC}'
            else:
                return fn
        return wrapper

    @staticmethod
    def underline_format(function):
        def wrapper():
            fn = function()
            if isinstance(fn, str):
                return f'{TextFormat.BOLD}{fn}{TextStyle.ENDC}'
            else:
                return fn
        return wrapper

class TextColor(TextStyle):
    PURPLE_COLOR = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    RED_FAIL = '\033[91m'

    @staticmethod
    def purple(function):
        def wrapper():
            fn = function()
            if isinstance(fn, str):
                return f'{TextColor.PURPLE_COLOR}{fn}{TextStyle.ENDC}'
            else:
                return fn
        return wrapper

    @staticmethod
    def blue(function):
        def wrapper():
            fn = function()
            if isinstance(fn, str):
                return f'{TextColor.BLUE}{fn}{TextStyle.ENDC}'
            else:
                return fn
        return wrapper

    @staticmethod
    def cyan(function):
        def wrapper():
            fn = function()
            if isinstance(fn, str):
                return f'{TextColor.CYAN}{fn}{TextStyle.ENDC}'
            else:
                return fn
        return wrapper
    
    @staticmethod
    def green(function):
        def wrapper():
            fn = function()
            if isinstance(fn, str):
                return f'{TextColor.GREEN}{fn}{TextStyle.ENDC}'
            else:
                return fn
        return wrapper

    @staticmethod
    def warning(function):
        def wrapper():
            fn = function()
            if isinstance(fn, str):
                return f'{TextColor.WARNING}{fn}{TextStyle.ENDC}'
            else:
                return fn
        return wrapper

    @staticmethod
    def red_fail(function):
        def wrapper():
            fn = function()
            if isinstance(fn, str):
                return f'{TextColor.RED_FAIL}{fn}{TextStyle.ENDC}'
            else:
                return fn
        return wrapper