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


def run(cmd):
    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout, stderr = proc.communicate()
    return proc.returncode, stdout, stderr


def runOnShells(shell_list, filename):
    for shell in shell_list:
        print(colored(shell, "yellow"))
        print(colored("=" * 10, "yellow"))
        output_info = run(["/bin/" + shell, filename])
        print("Exit code:", output_info[0])
        print("Stdout:", output_info[1].decode("utf-8"))
        print("Stderr:", output_info[2].decode("utf-8"))
        print(colored("=" * 10, "yellow"))


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
    runOnShells(installedShells, os.getcwd() + "/" + sys.argv[1])
