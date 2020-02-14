# Generating random programs

- [ ] Finish words
- [ ] Statements
  + [ ] Simple commands (assignments, commands, redirects)
  + [ ] Process control (`|`, `&`, `(...)`)
  + [ ] Logic (`&&`, `||`, `!`, `;`)
  + [ ] Control (`if`, `while`, `until`, `for`, `case`)
  + [ ] Function definition
  
- [ ] Bias towards well known variables (`ENV`, `PATH`, etc.)
- [ ] Bias towards well known shell builtins
- [ ] Option to not generate calls to real programs (need to watch out for `eval` and `source`/`.`!)
- [ ] Options to avoid weird behaviors
  + [ ] Implementation defined (e.g., checking pipe termination)
  + [ ] [Unspecified behavior](https://github.com/mgree/smoosh/blob/master/unspec.md) (e.g., unset `HOME` for `~`) (see 
  + [ ] [Undefined behavior](https://github.com/mgree/smoosh/blob/master/undef.md) (e.g., `exit 300`)

# Linking up with afl-fuzz

- [ ] Sandboxing
- [ ] Use random programs as a test corpus
- [ ] Use [smoosh tests](https://github.com/mgree/smoosh/blob/master/tests) as a corpus
- [ ] Compare shells on different programs
  + [ ] Build VM that can hold all of the shells

# Things to look at

- [Fuzzing in bash](http://lcamtuf.blogspot.com/2014/10/bash-bug-how-we-finally-cracked.html)
