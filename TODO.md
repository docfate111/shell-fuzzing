# Generating random programs

- [X] Finish words
  + [ ] Fixup HEREDOCS ???
- [X] Statements
  + [X] Simple commands (assignments, commands, redirects)
  + [X] Process control (`|`, `&`, `(...)`)
  + [X] Logic (`&&`, `||`, `!`, `;`)
  + [X] Control (`if`, `while`, `until`, `for`, `case`)
  + [X] Function definition 
- [X] WeightedOr-doesn't work with unwrapped strings (i.e. must be NRef(), And(), Or() etc.)  
- [X] Bias towards well known variables (`ENV`, `PATH`, etc.)
- [X] Bias towards well known shell builtins
?? Next steps:
- [ ] Option to not generate calls to real programs (need to watch out for `eval` and `source`/`.`!)
- [ ] Options to avoid weird behaviors
  + [ ] Implementation defined (e.g., checking pipe termination)
  + [ ] [Unspecified behavior](https://github.com/mgree/smoosh/blob/master/unspec.md) (e.g., unset `HOME` for `~`) (see 
  + [ ] [Undefined behavior](https://github.com/mgree/smoosh/blob/master/undef.md) (e.g., `exit 300`)

# Linking up with afl-fuzz

- [ ] Sandboxing
- [X] Use random programs as a test corpus
- [ ] Use [smoosh tests](https://github.com/mgree/smoosh/blob/master/tests) as a corpus
- [X] Compare shells on different programs
  + [X] Build VM that can hold all of the shells

# Things to look at

- [POSIX spec](https://pubs.opengroup.org/onlinepubs/9699919799/)
- [gramfuzz docs](https://d0c-s4vage.github.io/gramfuzz/)
- [Fuzzing in bash](http://lcamtuf.blogspot.com/2014/10/bash-bug-how-we-finally-cracked.html)
- [C-reduce on languages other than C](https://linki.tools/2020/02/creduce-it-s-a-kind-of-magic.html)
