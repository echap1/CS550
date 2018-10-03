from termcolor import colored

def bold(s):
    return colored(s, attrs=["bold"])

def underline(s):
    return colored(s, attrs=["underline"])

def reverse(s):
    return colored(s, attrs=["reverse"])

def dark(s):
    return colored(s, attrs=["dark"])


def red(s):
    return colored(s, "red")

def green(s):
    return colored(s, "green")

def blue(s):
    return colored(s, "blue")

def magenta(s):
    return colored(s, "magenta")

def grey(s):
    return colored(s, "grey")

def cyan(s):
    return colored(s, "cyan")