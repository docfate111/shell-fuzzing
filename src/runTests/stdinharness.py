import os
from termcolor import colored
import sys
import subprocess
import time
import signal


class TimeoutException(Exception):  # Custom exception class
    pass


def timeout_handler(signum, frame):  # Custom signal handler
    raise TimeoutException


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
    results = {}
    shell = shell_list[0]
    print(colored(shell, "yellow"))
    print(colored("=" * 10, "yellow"))
    output_info = run(["/bin/" + shell, filename])
    print("Exit code:", output_info[0])
    print("Stdout:", output_info[1].decode("utf-8"))
    print("Stderr:", output_info[2].decode("utf-8"))
    print(colored("=" * 10, "yellow"))
    results["Exit code"] = output_info[0]
    results["Stdout"] = output_info[1].decode("utf-8")
    results["Stderr"] = output_info[2].decode("utf-8")
    for shell in shell_list[1:]:
        print(colored(shell, "yellow"))
        print(colored("=" * 10, "yellow"))
        output_info = run(["/bin/" + shell, filename])
        print("Exit code:", output_info[0])
        print("Stdout:", output_info[1].decode("utf-8"))
        print("Stderr:", output_info[2].decode("utf-8"))
        print(colored("=" * 10, "yellow"))
        # if (
        #         output_info[0] != results["Exit code"]
        #         or output_info[1] != results["Stdout"]
        #         or output_info[2] != results["Stderr"]
        #     ):
        #         exit(1)


def getinput(f):
    for line in stdin_fileno:
        f.write(line)


if __name__ == "__main__":
    # https://github.com/mykter/afl-training/tree/master/harness#a-minimal-stdin-test-harness
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
    stdin_fileno = sys.stdin
    if os.path.exists("filetorun"):
        os.remove("filetorun")
    # Change the behavior of SIGALRM
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(5)
    # This try/except loop ensures that
    #   you'll catch TimeoutException when it's sent.
    f = open("filetorun", "w")
    try:
        getinput(f)
    except TimeoutException:
        f.close()
        runOnShells(installedShells, "filetorun")
