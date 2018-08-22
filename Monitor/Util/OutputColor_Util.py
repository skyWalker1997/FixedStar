
class Logger:
    """
    A Display class
    """
    """Display type"""
    DEFAULT = 0
    BOLD= 1
    NON_BOLD = 22
    UNDERLINE = 4
    NON_UNDERLINE = 24
    FLICKER = 5
    NON_FLICKER = 25
    REVERSE = 7
    NON_REVERSE = 27

    """Foreground"""
    F_BLACK = '[30m'
    F_RED = '[31m'
    F_GREEN = '[32m'
    F_YELLOW = '[33m'
    F_BLUE = '[34m'
    F_PINK = '[35m'
    F_CYAN = '[36m'
    F_WHITE = '[37m'


    """BackGround"""
    B_WHITE = '[40m'
    B_RED = '[41m'
    B_GREEN = '[42m'
    B_YELLOW = '[43m'
    B_BLUE = '[44m'
    B_PINK = '[45m'
    B_CYAN = '[46m'
    B_GREY = '[47m'

    """Font"""
    DEEPGREY = '[90m'
    RED = '[91m'
    GREEN = '[92m'
    YELLOW = '[93m'
    BLUE = '[94m'
    PINK = '[95m'
    CYAN = '[96m'
    BLACK = '[97m'
    GREY = '[98m'


    """General"""
    HEADER = '\033[1;98m'
    LOGBLUE = '\033[4;94m'
    OKGREEN = '\033[1;92m'
    WARNING = '\033[4;93m'
    FAIL = '\033[1;93;41m'
    BEGINC= '\033'
    ENDC = '\033[0m'
    TEST = '\033[1;30m'


# print Logger.HEADER + "info" + Logger.ENDC
# print Logger.LOGBLUE + "info" + Logger.ENDC
# print Logger.OKGREEN + "info" + Logger.ENDC
# print Logger.WARNING + "info" + Logger.ENDC
# print Logger.FAIL + "info" + Logger.ENDC