POSIX shell fuzzer

-----------------

A grammar-based fuzzer for the POSIX language implementation that runs random shell scripts and tests for undefined behavior.
NOTE: the script assumes your OS is using the yum package manager but it shouldn't be hard to modify the script based for your distro
Running 
``` 
./provision.sh
``` 
sets everything up
```
./run.sh
```
runs the harness
 .travis.yml (optional)
    just runs provision.sh and then make
  provision.sh
    installs global dependencies, e.g., afl-fuzz, gramfuzz/test-generation deps
  run.sh
    the command that runs afl-fuzz
  /shells
    Makefile
      has a target for each shell we care about
      goes into that shell's directory and does the whole build process
      each shell has `-dep` target, i.e., `bash3-dep` `smoosh-dep`
        the `-dep` target should run `yum` or whatever else to get dependencies
    /bash3
      /src
      ...
      bash
    /bash4
      /src
      ...
      bash
    /bash5
      /src
      ...
      bash
    /fish
      ...
      fish
    ...
  /seeds - directory with randomly generated POSIX programs go here
  /output - this directory is afl-fuzz's -o directory
shells - file with a list of all of the shells we want to run:
  ~/shells/bash3/bash
  ~/shells/bash4/bash
  ~/shells/bash5/bash
  ~/shells/fish/bash
  ~/shells/dash/bash
  ~/shells/smoosh/bash
  ...
