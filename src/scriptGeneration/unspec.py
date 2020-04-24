#    Include this later:
'''
Will implement this later:
and the following may need to be quoted under certain circumstances. That is, these characters may be special depending on conditions described elsewhere in this volume of POSIX.1-2017:

*   ?   [   #   ˜   =   %
'''
#NDef("header", "#!/bin/")
#for beginning of programs i.e. #!/bin/zsh
'''Not posix but in shells:
    [[ ]]
    function
    select
  other bashisms(for me to implement later): https://mywiki.wooledge.org/Bashism
'''
'''
NDef("unspecified_behavior_commands", Or(
    "alloc",
    "autoload",
    "bind",
    "bindkey",
    "builtin",
    "bye",
    "caller",
    "cap",
    "chdir",
    "clone",
    "comparguments",
    "compcall",
    "compctl",
    "compdescribe",
    "compfiles",
    "compgen",
    "compgroups",
    "complete",
    "compquote",
    "comptags",
    "comptry",
    "compvalues",
    "declare",
    "dirs",
    "disable",
    "disown",
    "dosh",
    "echotc",
    "echoti",
    "help",
    "history",
    "hist",
    "let",
    "local",
    "login",
    "logout",
    "map",
    "mapfile",
    "popd",
    "print",
    "pushd",
    "readarray",
    "repeat",
    "savehistory",
    "source",
    "shopt",
    "stop",
    "suspend",
    "typeset",
    "whence"
)
)
