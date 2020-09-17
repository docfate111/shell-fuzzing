import os
from termcolor import colored
import sys
import subprocess


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


checkShell = lambda program: "/bin" in which(program)


def get_output(cmnd):
    try:
        output = subprocess.check_output(
            cmnd,
            stderr=subprocess.STDOUT,
            shell=True,
            timeout=3,
            universal_newlines=True,
        )
    except subprocess.CalledProcessError as exc:
        print("Status : FAIL", exc.returncode, exc.output)
    else:
        print("Output: \n{}\n".format(output))


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: python3", sys.argv[0], "[script]")
        exit(0)
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
    installedShells = list(filter(checkShell, shells))
