from datetime import datetime


class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Timer:
    def __init__(self, func_name=""):
        self.func_name = func_name

    def __enter__(self):
        self.start = datetime.now()

    def __exit__(self, *args):
        self.end = datetime.now()
        print("{}{} took {}{}".format(Colors.OKBLUE, self.func_name, self.end - self.start, Colors.ENDC))
