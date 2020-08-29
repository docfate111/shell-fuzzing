from specified import *
NDef("globalvar",
     Or(
         "ENV",
         "HOME",
         "IFS",
         "LANG",
         "LC_ALL",
         "LC_COLLATE",
         "LC_CTYPE",
         "LC_MESSAGES",
         "LINENO",
         "NLSPATH",
         "PATH",
         "PPID",
         "PS1",
         "PS2",
         "PS4",
         "PWD"
     )
)
#Regular Built-In Utilities
NDef("built-in", Or(
    NRef("alias_command"),
    NRef("bg_command"),
    NRef("cd_command"),
    NRef("command_command"),
    NRef("false_command"),
    NRef("fc_command"),
    NRef("fg_command"),
    NRef("getopts_command"),
    NRef("hash_command"),
    NRef("jobs_command"),
    NRef("kill_command"),
    NRef("newgrp_command"),
    NRef("pwd_command"),
    NRef("read_command"),
    NRef("type_command"),
    NRef("true_command"),
    NRef("ulimit_command"),
    NRef("umask_command"),
    NRef("unalias_command"),
    NRef("wait_command")
)
)
NDef("special-built-in", Or(
    NRef("break_command"),
    NRef("colon_command"),
    NRef("continue_command"),
    NRef("dot_command"),
    NRef("eval_command"),
    NRef("exec_command"),
    NRef("exit_command"),
    NRef("export_command"),
    NRef("readonly_command"),
    NRef("return_command"),
    NRef("set_command"),
    NRef("shift_command"),
    NRef("times_command"),
    NRef("trap_command"),
    NRef("unset_command")
    )
)
NDef("n",  UInt(odds = [(0.9, [1, 2]),
                               (0.1, [3, 9])])
)
NDef("break_command", WeightedOr(
    (And(
        " ",
        NRef("break")
     ), 0.9),
    (And(
        " ",
        NRef("break"),
        " ",
        NRef("n")
    ),
     0.1)
    )
)
NDef("break", "break")
NDef("colon_command",
And(
    " ",
    ":"
    )
)
NDef("continue", "continue")
NDef("continue_command", WeightedOr(
    (And(
        " ",
        NRef("continue")
    ), 0.9),
    (And(
        " ",
        NRef("continue"),
        " ",
        NRef("n")
        ), 0.1)
    )
)
NDef("dot_command", And(
                        " ",
                        ".",
                        " ",
                        NRef("filename")
                        )
)
NDef("eval_command", And(
                        " ",
                        "eval",
                        " ",
                        NRef("command")
                        )
)
NDef("exec_command",  And(
                        " ",
                        "exec",
                        " ",
                        NRef("command")
                        )
)
     #undefined number for n, can be changed later
NDef("exit_command",  WeightedOr(
    (And(
        " ",
        NRef("exit")
    ), 0.9),
    (And(
        " ",
        NRef("exit"),
        " ",
        NRef("n")
    ), 0.1)
    )
    )
NDef("exit", "exit")
NDef("export_command", And(" ",
                            "export",
                            " ",
                            Or(
                               "-p",
                               NRef("varname"),
                               And(
                                    NRef("varname"),
                                    Or("=",
                                    And(
                                        " ",
                                        "=",
                                        " "
                                    )),
                                  NRef("WORD"))
                            ))
)
NDef("readonly_command", And(
                            " ",
                            "readonly",
                            Or(
                               "-p",
                               NRef("varname"),
                               And(NRef("varname"),
                                    Or("=",
                                        And(
                                            " ",
                                            "=",
                                            " "
                                            )
                                    ),
                                    NRef("WORD"))
                           )
                           )
)
NDef("readonly_command", WeightedOr(
    (And(
        " ",
        NRef("readonly")
    ), 0.9),
    (And(
        " ",
        NRef("readonly"),
        " ",
        NRef("n")
    ), 0.1)
))
NDef("readonly", "readonly")
NDef("shift_command", WeightedOr(
    (And(
        " ",
        NRef("shift")
    ), 0.9),
    (And(
        " ",
        NRef("shift"),
        " ",
        NRef("n")
    ), 0.1)
    )
)
NDef("return", "return")
NDef("return_command", WeightedOr(
    (And(
        " ",
        NRef("return")
    ), 0.9),
    (And(
        " ",
        NRef("return"),
        " ",
        NRef("n")
    ), 0.1)
    )
)
NDef("set_command", And(
                    " ",
                    "set",
                    " ",
                        Or("-", "+"),
                        Or(
                            And(
                                String(charset="abCefmnuvx", min=1, max=10),
                                Or(
                                    "",
                                    And(" ",
                                        Or(
                                            "-",
                                            "+"
                                        ),
                                        Or(
                                            "h",
                                            "o"
                                        ),
                                        Or("",
                                           And(
                                               " ",
                                               NRef("command")
                                           )
                                        )
                                    )
                                )),
                            And("-", Or(
                                "",
                                And(
                                    " ",
                                    NRef("command")
                                )
                            )
                            ),
                            "o",
                            "h"
                        )
))
NDef("shift", "shift")
NDef("times_command", And(" ", "times", " "))
NDef("trap_command", And(" ", "trap", " ",
                        And(
                            Or("",
                               NRef("command"),
                               NRef("globalvar")
                            ),
                            " ",
                            Or(
                                "",
                                NRef("command"),
                                NRef("n")
                            )
                        )
                    )
)
NDef("unset_command", And(" ", "unset", " ",
                          Or(
                              "-f",
                              "-fv",
                              "-v"
                          ),
                          " ",
                          NRef("varname")
                      )
)
#alias
NDef("alias_command", Or(
    And(
        "alias",
         " ",
        NRef("varname"),
         " ",
        "=",
         " ",
        NRef("s")
    ),
    And(
        "alias",
         " ",
        NRef("varname"),
         " ",
        "=",
         " ",
        NRef("varname")
    ),
    And(
        "alias",
         " ",
        NRef("varname"),
         " ",
        "=",
         " ",
        NRef("command")
    ),
    And(
        "alias",
         " ",
        NRef("varname"),
         " ",
        "=",
         " ",
        And(
            NRef("single_quote"),
            NRef("command"),
            NRef("single_quote")
        )
    ),
    And(
        "alias",
         " ",
        NRef("varname"),
         " ",
        "=",
         " ",
        And(
            NRef("double_quote"),
            NRef("command"),
            NRef("double_quote")
        )
    ),
    And(
        "alias",
         " ",
        NRef("varname"),
         " ",
        And(
            " ",
            "=",
            " "
        ),
        And(
            NRef("double_quote"),
             " ",
            NRef("command"),
             " ",
            NRef("double_quote")
        )
    ),
    And(
        "alias",
         " ",
        NRef("varname"),
         " ",
        And(
            " ",
            "=",
            " "
        ),
        And(
            NRef("single_quote"),
             " ",
            NRef("command"),
             " ",
            NRef("single_quote")
        )
    )
)
)
#bg
NDef("bg_command", Or(
    "bg",
    And(
        "bg",
        " ",
        NRef("job_id")
    )
 )
)
NDef("job_id", Or(
    "%%",
    "%+",
    "%-",
    And("%", NRef("job_number")),
    And("%", NRef("s")),
    And("%?", NRef("s"))
  )
)
PID_MAX_LIMIT=32768
#99998 for macOS
NDef("job_number",  UInt(odds = [(0.4, [0, 2]),
                               (0.4, [3, 9]),
                               (0.2,  [10, PID_MAX_LIMIT])]))
#cd
NDef("posix_directories", Or(
    "/dev",
    "/dev/null",
    "/dev/tty",
    "/tmp",
    "/",
    "/dev/console"
    )
)
NDef("possible_directory_names", And(
    String(charset = charset_alphanum, min=1, max=20),
    String(charset = charset_not_slash, min=1, max=7)
    )
)
NDef("cd_command", Or(
    And(" ", "cd",
        " ",
        Or(
            "-L",
            "-P",
            ""
        ),
        " ",
        Or(
            NRef("possible_directory_names"),
            NRef("posix_directories")
        )
    )
    )
     )
#command
NDef("command_command", And(
        "command",
        " ",
        Or(
            "-p",
            Or(
                "-v",
                "-V"
            ),
            "",
            And(
                "-p",
                 Or(
                     "-v",
                     "-V"
                 )
            ),
        ),
        " ",
        Or(
            NRef("s"),
            Or(
                NRef("built-in"),
                NRef("special-built-in")),
            NRef("command")
        )
    )
)
#false
NDef("false_command", "false")
#fc
#seems wrong what goes on for first and last
'''
fc [-r] [-e editor] [first [last]]

fc -l [-nr] [first [last]]

fc -s [old=new] [first]
'''
NDef("editor", NRef("s")) #for now
NDef("number",  UInt(odds = [(0.45, [0, 20]),
                               (0.45, [20, 90]),
                               (0.1,  [90, 65535])]
    ))
NDef("first", Or(
                 NRef("s"),
                 NRef("command"),
                 NRef("number"),
                 And("-", NRef("number"))
              ))
NDef("last", NRef("first"))
NDef("old", NRef("command"))
NDef("new", NRef("command"))
NDef("fc_command", And(
    "fc",
     " ",
     Or(
         Or(
             "-r",
             And("-e",  " ", NRef("editor"),  " "),
             Or(
                 NRef("first"),
                 And(
                     NRef("first"),
                      " ",
                     NRef("last"),
                      " ",
                )
             ),
             And(
                 "-r",
                  " ",
                 And("-e", NRef("editor")),
                  " ",
             ),
             And(
                 Or(
                     "-r",
                      " ",
                     And("-e", NRef("editor")),
                      " "
                ),
                 Or(
                     NRef("first"),
                     And(
                         NRef("first"),
                          " ",
                         NRef("last"),
                          " ",
                     )
                 )
             )
         ),
         And(
             "-l",
              " ",
             Or(
                 "-nr",
                 ""
             ),
             Or(
                 NRef("first"),
                 And(
                     NRef("first"),
                      " ",
                     NRef("last"),
                      " ",
                 ),
                 ""
             )
         ),
         And(
             "-s",
              " ",
             Or(
                 And(NRef("old"),  " ", "=",  " ", NRef("new")),
                 ""
             ),
             Or(
                 NRef("first"),
                 ""
            )
         )
     )
)
     )
#fg
NDef("fg_command", Or(
    "fg",
    And(
        "fg",
        " ",
        NRef("job_id")
    )
 )
)
#getopts:
'''
how to implement? opstring as $options?
getopts optstring name [arg...]
'''
NDef("getopts_command", And("getopts",  " ", NRef("s"),  " ", NRef("varname")))
#hash (not sure if this is right?)
NDef("hash_command", Or("-r", NRef("command")))
#jobs
NDef("jobs_command", And(
                     "jobs",
                     " ",
                     Or(
                         "-l",
                         "-p",
                         ""
                        ),
                     " ",
                     NRef("job_id"),
                      " "

))
#kill
NDef("signal_name", Or(
     "SIGABRT",
     "SIGALRM",
     "SIGBUS",
     "SIGCHLD",
     "SIGCONT",
     "SIGFPE",
     "SIGHUP",
     "SIGILL",
     "SIGINT",
     "SIGKILL",
     "SIGPIPE",
     "SIGQUIT",
     "SIGSEGV",
     "SIGSTOP",
     "SIGTERM",
     "SIGTSTP",
     "SIGTTIN"
     "SIGTTOU",
     "SIGUSR1",
     "SIGUSR2",
     "SIGPOLL"
     "SIGPROF",
     "SIGSYS",
     "SIGTRAP",
     "SIGURG",
     "SIGVTALRM",
     "SIGXCPU",
     "SIGXFSZ"))
'''
kill -s signal_name pid...

kill -l [exit_status]

[XSI] [Option Start] kill [-signal_name] pid...

kill [-signal_number] pid...
'''
NDef("kill_command", And("kill", " ",
                         Or(
                             And(
                                 "-l",
                                 " ",
                                 NRef("job_number"),
                                  " "
                             ),
                             And(
                                 "-s",
                                 " ",
                                 NRef("signal_name"),
                                 " ",
                                 NRef("job_number"),
                                  " "
                             ),
                             And(
                                 "-",
                                 NRef("signal_name"),
                                 " ",
                                 NRef("job_number"),
                                  " "
                             ),
                          )
     )
)
#newgrp
NDef("group", NRef("varname"))
NDef("newgrp_command", And("newgrp",
                           Or(
                             "",
                             And(" ", "-l",  " "),
                              And(" ", "-l", " ", NRef("group")),
                               And(" ", NRef("group"),  " "),
)
))
#pwd
NDef("pwd_command", And("pwd", " ",
                        Or(
                            "-L",
                            "-P",
                            And("-L", " ", "-P",  " "),
                             And("-P", " ", "-L",  " "),
                            ""
                            ))
)
#read
NDef("read_command", And("read", " ",
                         Or(
                             And("-r", " ", NRef("varname"),  " "),
                             NRef("varname")
                        )
                     )
)
#true
NDef("true_command", "true")
#type
NDef("type_command", And("type", " ", NRef("varname"),  " "))
#ulimit ulimit [-f] [blocks][Option End]
NDef("ulimit_command", And("ulimit", " ",
                           Or(
                               "-f",
                               And("-f", " ", NRef("number"),  " "),
                               NRef("number")
                           )
))
#umask
NDef("umask_command", And("umask", " ",
                          And(
                              Or(
                                  "",
                                  And("-S", " "),
                              ),
                              And(
                                  NRef("digit"),
                                  NRef("digit"),
                                  NRef("digit"),
                                   " "
                              )
                        )

                       )
     )
#unalias
NDef("unalias_command", And("unalias", " ",
                            Or(
                                NRef("varname"),
                                "-a"
                            ),
                             " "
                            )
)
#wait
NDef("wait_command", And("wait", " ",
                         Or(
                             NRef("job_number"),
                             NRef("job_id")
                         ),  " ")
)
