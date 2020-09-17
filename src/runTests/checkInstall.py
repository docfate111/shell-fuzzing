import os
from termcolor import colored


def which(program):
    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file
    return "Not installed"


def checkShell(program):
    if "/bin" in which(program):
        print(colored(program + " is installed", "green"))
    else:
        print(colored(program + " is not installed", "red"))


if __name__ == "__main__":
    shells = [
        "dash",
        "yash",
        "ksh",
        "mksh",
        "bosh",
        "zsh",
        "fish",
        "bash3",
        "bash4",
        "bash5",
        "heirloom-sh",
        "osh",
        "bash",
        "tcsh",
    ]
    for i in shells:
        checkShell(i)
