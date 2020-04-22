POSIX shell fuzzer

-----------------

A grammar-based fuzzer for the POSIX language implementation that runs random shell scripts and tests for undefined behavior.

Running ./setup.sh does everything

The default number of scripts is 15 for now


Currently there are 2 bugs in gramfuzz that need to be fixed until we are able to run the scripts generated in the directory smooshfuzz/src/testscripts

Next steps: fix syntax errors given by generating script and build harness for running different shells quickly
