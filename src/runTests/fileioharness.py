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


def runOnShells(shell_list, filename, exitOndiff):
    results = {}
    shell = shell_list[0]
    print(colored(shell, "yellow"))
    print(colored("=" * 10, "yellow"))
    output_info = run(["/usr/local/bin/" + shell, filename])
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
        output_info = run(["usr/local/bin/" + shell, filename])
        print("Exit code:", output_info[0])
        print("Stdout:", output_info[1].decode("utf-8"))
        print("Stderr:", output_info[2].decode("utf-8"))
        print(colored("=" * 10, "yellow"))
        if exitOndiff:
            if (
                output_info[0] != results["Exit code"]
                or output_info[1] != results["Stdout"]
                or output_info[2] != results["Stderr"]
            ):
                exit(1)


if __name__ == "__main__":
    # https://github.com/mykter/afl-training/tree/master/harness#writing-a-file-input-test-harness
    if len(sys.argv) == 1:
        print("Usage: python3", sys.argv[0], "[script] [exit on difference]")
        print("Takes a file and runs all installed shells on it")
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
    exitOndiff = False
    if len(sys.argv) > 2:
        exitOndiff = True
    runOnShells(installedShells, os.getcwd() + "/" + sys.argv[1], exitOndiff)
