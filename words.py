from weightedOr import *
# TODO
# generalize whitespace to zero-or-more space or tabs
# clean up formatting
#of code?
# different categories for words and program statements? (not super important)
# figure out how to generate more strings and fewer special characters
# do you mean more valid strings?
charset_nonspecial = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
charset_nonspecial_rest="-_+.,/!"
charset_not_slash="~!@#$%^&*()_+~"
#the problem with this method is I can't use String()
#and an NRef object is printed
NDef("random_string",  String(charset = charset_nonspecial, min=1, max=15))
NDef("s", And(
    NRef("WHITESPACE"),
    NRef("random_string"),
    NRef("WHITESPACE")
)
)
    #, 0.8),
    #String(charset=charset_nonspecial_rest, min=1, max=10),
     #0.1),
    #NRef("parens"), #0.9),
    #NRef("tilde") #, 0.1) 
#print(NRef("s"))
NDef("~", "~")
NDef("tilde", WeightedOr(
    (NRef("s"), 0.8),
    (NRef("parens"), 0.1),
    (NRef("~"), 0.1)
)
) 
    #(And(
        #"~",
     #   String(charset=String.charset_alpha, min=1, max=1),
      #  String(charset=String.charset_alphanum, min=0, max=10)
    #), 0.6),
    #(And(
        #"~",
      #  NRef("s"), 0.4)
     #)
    #)
#braces needed?
NDef("FMTw", Or("-", "-:", "=", "=:", "+", "+:", "?", "?:", "%", "%%",  "#", "##"))
'''
The application shall quote the following characters if they are to represent themselves:

|  &  ;  <  >  (  )  $  `  \  "  '  <space>  <tab>  <newline>

Questions:
is \" the same as "
shouldn't there be cases with multiple characters (i.e "|&(" )
do i need to close parens since it is only representing itself
'''
NDef("repr", Or("|", "&", ";","<",">","(",")","$","\`","\\","\"", "\'", " ","\t","\n"))
NDef("single_quote", "\'")
NDef("double_quote", "\"")
NDef("representsitself", Or(
                         And(NRef("single_quote"), NRef("repr"),NRef("single_quote"),  NRef("WHITESPACE"),),
                         And(NRef("double_quote"), NRef("repr"), NRef("double_quote"),  NRef("WHITESPACE"),)
                         )
)
NDef("digit", Or("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"))
'''
Will implement this later:
and the following may need to be quoted under certain circumstances. That is, these characters may be special depending on conditions described elsewhere in this volume of POSIX.1-2017:

*   ?   [   #   ˜   =   %
'''
Def("charset_special_conditions_for_quoting", Or("*", "?", "[", "#", "˜", "=", "%"))
#NDef("header", "#!/bin/")
#for beginning of programs i.e. #!/bin/zsh
'''Not posix but in shells:
    [[ ]]	
    function	
    select
  other bashisms(for me to implement later): https://mywiki.wooledge.org/Bashism 
'''
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
    NRef("true_command"),
    NRef("type_command"),
    NRef("ulimit_command"),
    NRef("umask_command"),
    NRef("unalias_command"),
    NRef("wait_command")
)
     '''
NDef("special-built-ins", Or(
    NRef("break_command"), 
    NRef("colon_command"),
    NRef("continue_command"),
    NRef("dot_command"),
    NRef("eval"),
    NRef("exec"),
    NRef("exit"),
    NRef("export"), 
    NRef("readonly"), 
    NRef("return"),
    NRef("set"),
    NRef("shift"), 
    NRef("times"),
    NRef("trap"),
    NRef("unset")
    )
)
'''
#
#    Include this later:
#     
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
'''
#alias
NDef("alias_command", Or(
    And(
        "alias",
         NRef("WHITESPACE"),
        NRef("varname"),
         NRef("WHITESPACE"),
        "=",
         NRef("WHITESPACE"),
        NRef("s"),
         NRef("WHITESPACE"),
    ),
    And(
        "alias",
         NRef("WHITESPACE"),
        NRef("varname"),
         NRef("WHITESPACE"),
        "=",
         NRef("WHITESPACE"),
        NRef("varname"),
         NRef("WHITESPACE"),
    ),
    And(
        "alias",
         NRef("WHITESPACE"),
        NRef("varname"),
         NRef("WHITESPACE"),
        "=",
         NRef("WHITESPACE"),
        NRef("command"),
         NRef("WHITESPACE"),
    ),
    And(
        "alias",
         NRef("WHITESPACE"),
        NRef("varname"),
         NRef("WHITESPACE"),
        "=",
         NRef("WHITESPACE"),
        And(
            NRef("single_quote"),
            NRef("command"),
            NRef("single_quote")
        ),
         NRef("WHITESPACE"),
    ),
    And(
        "alias",
         NRef("WHITESPACE"),
        NRef("varname"),
         NRef("WHITESPACE"),
        "=",
         NRef("WHITESPACE"),
        And(
            NRef("double_quote"),
            NRef("command"),
            NRef("double_quote")
        ),
         NRef("WHITESPACE"),
    ),
    And(
        "alias",
         NRef("WHITESPACE"),
        NRef("varname"),
         NRef("WHITESPACE"),
        And(
            NRef("WHITESPACE"),
            "=",
            NRef("WHITESPACE")
        ),
        And(
            NRef("double_quote"),
             NRef("WHITESPACE"),
            NRef("command"),
             NRef("WHITESPACE"),
            NRef("double_quote")
        ),
         NRef("WHITESPACE"),
    ),
    And(
        "alias",
         NRef("WHITESPACE"),
        NRef("varname"),
         NRef("WHITESPACE"),
        And(
            NRef("WHITESPACE"),
            "=",
            NRef("WHITESPACE")
        ),
        And(
            NRef("single_quote"),
             NRef("WHITESPACE"),
            NRef("command"),
             NRef("WHITESPACE"),
            NRef("single_quote")
        ),
         NRef("WHITESPACE"),
    )
)
)
#bg
NDef("bg_command", Or(
    "bg",
    And(
        "bg",
        NRef("WHITESPACE"),
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
    String(charset = charset_nonspecial, min=1, max=20),
    String(charset = charset_not_slash, min=1, max=7)
    )
)
NDef("cd_command", Or(
    And(NRef("WHITESPACE"), "cd",
        NRef("WHITESPACE"),
        Or(
            "-L",
            "-P",
            ""
        ),
        NRef("WHITESPACE"),
        Or(
            NRef("possible_directory_names"),
            NRef("posix_directories")
        ),
         NRef("WHITESPACE"),
    )
    )
     )
#command
NDef("command_command", And(
        "command",
        NRef("WHITESPACE"),
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
        NRef("WHITESPACE"),
        Or(
            NRef("s"),
            NRef("built-in"),
            NRef("command")
        ),
     NRef("WHITESPACE"),
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
     NRef("WHITESPACE"),
     Or(
         Or(
             "-r",
             And("-e",  NRef("WHITESPACE"), NRef("editor"),  NRef("WHITESPACE")),
             Or(
                 NRef("first"),
                 And(
                     NRef("first"),
                      NRef("WHITESPACE"),
                     NRef("last"),
                      NRef("WHITESPACE"),
                )
             ),
             And(
                 "-r",
                  NRef("WHITESPACE"),
                 And("-e", NRef("editor")),
                  NRef("WHITESPACE"),
             ),
             And(
                 Or(
                     "-r",
                      NRef("WHITESPACE"),
                     And("-e", NRef("editor")),
                      NRef("WHITESPACE")
                ),
                 Or(
                     NRef("first"),
                     And(
                         NRef("first"),
                          NRef("WHITESPACE"),
                         NRef("last"),
                          NRef("WHITESPACE"),
                     )
                 )
             )   
         ),
         And(
             "-l",
              NRef("WHITESPACE"),
             Or(
                 "-nr",
                 ""
             ),
             Or(
                 NRef("first"),
                 And(
                     NRef("first"),
                      NRef("WHITESPACE"),
                     NRef("last"),
                      NRef("WHITESPACE"),
                 ),
                 ""
             )
         ),
         And(
             "-s",
              NRef("WHITESPACE"),
             Or(
                 And(NRef("old"),  NRef("WHITESPACE"), "=",  NRef("WHITESPACE"), NRef("new")),
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
        NRef("WHITESPACE"),
        NRef("job_id")
    )
 )
)
#getopts: 
'''
how to implement? opstring as $options?    
getopts optstring name [arg...]
'''
NDef("getopts_command", And("getopts",  NRef("WHITESPACE"), NRef("s"),  NRef("WHITESPACE"), NRef("varname")))
#hash (not sure if this is right?)
NDef("hash_command", Or("-r", NRef("command")))
#jobs
NDef("jobs_command", And(
                     "jobs",
                     NRef("WHITESPACE"),
                     Or(
                         "-l",
                         "-p",
                         ""
                        ),
                     NRef("WHITESPACE"),
                     NRef("job_id"),
                      NRef("WHITESPACE")
                     
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
NDef("kill_command", And("kill", NRef("WHITESPACE"),
                         Or(
                             And(
                                 "-l",
                                 NRef("WHITESPACE"),
                                 NRef("job_number"),
                                  NRef("WHITESPACE")
                             ),
                             And(
                                 "-s",
                                 NRef("WHITESPACE"),
                                 NRef("signal_name"),
                                 NRef("WHITESPACE"),
                                 NRef("job_number"),
                                  NRef("WHITESPACE")
                             ),
                             And(
                                 "-",
                                 NRef("signal_name"),
                                 NRef("WHITESPACE"),
                                 NRef("job_number"),
                                  NRef("WHITESPACE")
                             ),
                          )
     )
)
#newgrp
NDef("group", NRef("varname"))
NDef("newgrp_command", And("newgrp",
                           Or(
                             "",
                             And(NRef("WHITESPACE"), "-l",  NRef("WHITESPACE")),
                              And(NRef("WHITESPACE"), "-l", NRef("WHITESPACE"), NRef("group")),
                               And(NRef("WHITESPACE"), NRef("group"),  NRef("WHITESPACE")),
)
))
#pwd
NDef("pwd_command", And("pwd", NRef("WHITESPACE"),
                        Or(
                            "-L",
                            "-P",
                            And("-L", NRef("WHITESPACE"), "-P",  NRef("WHITESPACE")),
                             And("-P", NRef("WHITESPACE"), "-L",  NRef("WHITESPACE")),
                            ""
                            ))
)
#read
NDef("read_command", And("read", NRef("WHITESPACE"),
                         Or(
                             And("-r", NRef("WHITESPACE"), NRef("varname"),  NRef("WHITESPACE")),
                             NRef("varname")
                        )
                     )
)
#true
NDef("true_command", "true")
#type
NDef("type_command", And("type", NRef("WHITESPACE"), NRef("varname"),  NRef("WHITESPACE"))) 
#ulimit ulimit [-f] [blocks][Option End]
NDef("ulimit_command", And("ulimit", NRef("WHITESPACE"),
                           Or(
                               "-f",
                               And("-f", NRef("WHITESPACE"), NRef("number"),  NRef("WHITESPACE")),
                               NRef("number")
                           )
))
#umask
NDef("umask_command", And("umask", NRef("WHITESPACE"),
                          And(
                              Or(
                                  "",
                                  And("-S", NRef("WHITESPACE")),
                              ),
                              And(
                                  NRef("digit"),
                                  NRef("digit"),
                                  NRef("digit"),
                                   NRef("WHITESPACE")
                              )
                        )
                          
                       )
     )
#unalias
NDef("unalias_command", And("unalias", NRef("WHITESPACE"),
                            Or(
                                NRef("varname"),
                                "-a"
                            ),
                             NRef("WHITESPACE")
                            )
)   
#wait
NDef("wait_command", And("wait", NRef("WHITESPACE"),
                         Or(
                             NRef("job_number"),
                             NRef("job_id")
                         ),  NRef("WHITESPACE"))
)
NDef("charsthatneedquotes",
     Or("|", "&",";", "<", ">", "(", ")", "$", "`", "\\", "\"", "\'" , " ", "\n"))
#characters that require single or double quotes
#never used?
NDef("quotedcharswithsingleordoublequotes", Or(
    And(
        "'",
        NRef("charsthatneedquotes"),
        "'"
    ),
    And(
        "\"",
       NRef("charsthatneedquotes"),
        "\""
    )
))
NDef("varname", And(NRef("WHITESPACE"),
     Or( NRef("globalvar"),
     And(String(charset=String.charset_alpha+b"_", min=1, max=1),
         String(charset=String.charset_alphanum+b"_", min=1, max=15)
     )), NRef("WHITESPACE")))
NDef("NAME", WeightedOr(
    (NRef("varname"), 0.9),
    (Or("@", "*", "#", "?", "-", "$", "!"), 0.1)))
#these parens can have parens inside themselves:
NDef("recursableparens",Or(
    And("${", NRef("WHITESPACE"), NRef("NAME"), NRef("WHITESPACE"), "}"), 
    And("${#", NRef("WHITESPACE"), NRef("NAME"), NRef("WHITESPACE"), "}"),
    And("${", NRef("WHITESPACE"), And(NRef("NAME"), NRef("FMTw"), NRef("WORD"), NRef("WHITESPACE"), "}"))),)
NDef("parens",Or(
    And("$",NRef("WHITESPACE"), NRef("NAME"),NRef("WHITESPACE"), NRef("recursableparens"))),
    And("$(",NRef("WHITESPACE"), NRef("NAME") , NRef("WHITESPACE"),")"),
    And("$((",NRef("WHITESPACE"), NRef("NAME"),NRef("WHITESPACE"), "))"))
#Rules for tilde:
NDef("~orVariable",Or(
    NRef("tilde"),
    NRef("parens")
)
)
'''
/* -------------------------------------------------------
   The grammar symbols
   ------------------------------------------------------- */
%token  WORD
%token  ASSIGNMENT_WORD
%token  NAME
%token  NEWLINE //what are these?
%token  IO_NUMBER'''
word = NDef("WORD",
            Join(
                Or(
                    NRef("s"),
                    NRef("~orVariable")
                ),
                sep="",
                max=6
            )
)
NDef("ASSIGNMENT_WORD",
     WeightedOr(
        (And(
        #should there be whitespace in assignment?
             NRef("NAME"),
            NRef("WHITESPACE"),
             "=",
             NRef("WHITESPACE"),
             NRef("WORD")
         ), 0.6),
         (And(
             NRef("globalvar"),
              NRef("WHITESPACE"),
             "=",
              NRef("WHITESPACE"),
             NRef("WORD")
         ), 0.4))
     )
NDef("NEWLINE", "\n")
NDef("TAB", "\t")
NDef("IO_NUMBER", UInt(odds = [(0.45, [0, 2]),
                               (0.45, [3, 9]),
                               (0.1,  [10, 65535])])) 
'''
The following are the operators (see XBD Operator)
   containing more than one character. 
%token  AND_IF    OR_IF    DSEMI
         '&&'      '||'     ';;'    
%token  DLESS  DGREAT  LESSAND  GREATAND  LESSGREAT  DLESSDASH
        '<<'   '>>'    '<&'     '>&'      '<>'       '<<-'   */
%token  CLOBBER
          '>|'  
'''
NDef("AND_IF",
     And(
         NRef("WHITESPACE"),
         "&&",
         NRef("WHITESPACE")
    )
)
NDef("OR_IF",
     And(
         NRef("WHITESPACE"),
         '||',
         NRef("WHITESPACE")
     )
)
NDef("DSEMI",
     WeightedOr(
         (";;", 0.1),
         (And(
             NRef("WHITESPACE"),
             ';;',
             NRef("WHITESPACE")
         ), 0.9)
    )
)    
NDef("DLESS",
     WeightedOr(
         ("<<", 0.1),
         (And(
             NRef("WHITESPACE"),
             '<<',
             NRef("WHITESPACE")
         ), 0.9)
     )
)
NDef("DGREAT",
     WeightedOr(
         (">>", 0.1),
         (And(
             NRef("WHITESPACE"),
             '>>',
             NRef("WHITESPACE")
         ), 0.9)
     )
)
NDef("LESSAND",
     WeightedOr(
         ("<&", 0.1),
         (And(
             NRef("WHITESPACE"),
             '<&',
             NRef("WHITESPACE")
         ), 0.9)
     )
)
NDef("GREATAND",
     Or(
         ">&",
         And(
             NRef("WHITESPACE"),
             '>&',
             NRef("WHITESPACE")
         )
     )
)
NDef("LESSGREAT",
     Or(
         "<>",
         And(
             NRef("WHITESPACE"),
             '<>',
             NRef("WHITESPACE")
         )
     )
)
NDef("DLESSDASH",
     Or(
         "<<-",
          And(
              NRef("WHITESPACE"),
              '<<-',
              NRef("WHITESPACE")
          )
     )
)
NDef("CLOBBER",
     Or(
         ">|",
         And(
             NRef("WHITESPACE"),
             '||',
             NRef("WHITESPACE")
         )
     )
)
NDef("WHITESPACE",
    WeightedOr(
        (NRef("NEWLINE"), 0.1),
        (NRef("TAB"), 0.1),
        #(And(NRef("NEWLINE"), NRef("WHITESPACE")), 0.02),
        #(And(NRef("TAB"), NRef("WHITESPACE")), 0.01),
        (" ", 0.8)
        #(And(" ", NRef("WHITESPACE")), 0.1),
        #(NRef("WHITESPACE"), 0.05)
    )
)
'''
/* The following are the reserved words. */
%token  If    Then    Else    Elif    Fi    Do    Done
      'if'  'then'  'else'  'elif'  'fi'  'do'  'done'   
%token  Case    Esac    While    Until    For
     'case'  'esac'  'while'  'until'  'for'  
These are reserved words, not operator tokens, and are
   recognized when reserved words are recognized. 
%token  Lbrace    Rbrace    Bang
       '{'       '}'       '!'   
%token  In
/*      'in'   */'''
NDef("If", Or(And("if", NRef("WHITESPACE")), " if "))
NDef("Then", Or(And("then", NRef("WHITESPACE")), " then "))
NDef("Else", Or(And("else", NRef("WHITESPACE")), " else "))
NDef("Elif", Or(And("elif", NRef("WHITESPACE")), " elif "))
NDef("Fi", Or(And("fi", NRef("WHITESPACE")), " fi "))
NDef("Do", Or(And("do", NRef("WHITESPACE")), " do "))
NDef("Done", Or(And("done", NRef("WHITESPACE")), " done "))
NDef("Case", Or(And("case", NRef("WHITESPACE")), " case "))
NDef("Esac", Or(And("esac", NRef("WHITESPACE")), " esac "))
NDef("While", Or(And("while", NRef("WHITESPACE")), " while "))
NDef("Until",  Or(And("until", NRef("WHITESPACE")), " until "))
NDef("For", Or(And("for", NRef("WHITESPACE")), " for "))
NDef("Lbrace", Or(And("{", NRef("WHITESPACE")), " { "))
NDef("Rbrace", Or(And(NRef("WHITESPACE"), "}"), "}"))
NDef("Bang", Or(And("!", NRef("WHITESPACE")), "!"))
'''
/* -------------------------------------------------------
   The Grammar
   ------------------------------------------------------- */
%start program
%%
program          : linebreak complete_commands linebreak
                 | linebreak
                 ;
complete_commands: complete_commands newline_list complete_command
                 |                                complete_command
                 ;
complete_command : list separator_op
                 | list
                 ;
'''
Def("program",
    Or(
        And(
            NRef("linebreak"),
            NRef("complete_commands"),
            NRef("linebreak"),
            NRef("linebreak")
        )
    ),
    cat="program")
# avoid left recursion
#NDef("complete_commands", 
#     Or(And(NRef("complete_commands"), NRef("newline_list"), NRef("complete_command")),  
#        NRef("complete_command")))
NDef("complete_commands",
     And(
         Join(
             And(
                 NRef("complete_command"),
                 NRef("newline_list")
             ),
             sep=""),
         NRef("complete_command")
         )
    )
NDef("complete_command",
     Or(And(NRef("list"), NRef("separator_op")),
        NRef("list")))
'''
list             : list separator_op and_or
                 |                   and_or
                 ;
and_or           :                         pipeline
                 | and_or AND_IF linebreak pipeline
                 | and_or OR_IF  linebreak pipeline
                 ;
'''
NDef("list", Or(And(NRef("list"), NRef("separator_op"), NRef("and_or")), NRef("and_or")))
NDef("and_or", Or(NRef("pipeline"), 
                And(NRef("and_or"), NRef("AND_IF"), NRef("linebreak"), NRef("pipeline")),
                And(NRef("and_or"), NRef("OR_IF"), NRef("linebreak"), NRef("pipeline"))
))
'''
pipeline         :      pipe_sequence
                 | Bang pipe
                 ;
pipe_sequence    :                             command
                 | pipe_sequence '|' linebreak command
                 ;
'''
NDef("pipeline", Or(
    NRef("pipeline"),
    And(NRef("Bang"), NRef("WHITESPACE"), NRef("pipe_sequence"))
))
NDef("pipe_sequence", Or(
    NRef("command"),
    And(NRef("pipe_sequence"),NRef("WHITESPACE"), "|",NRef("WHITESPACE"), NRef("linebreak"),NRef("WHITESPACE"), NRef("command"))
))
'''
command          : simple_command
                 | compound_command
                 | compound_command redirect_list
                 | function_definition
                 ;
compound_command : brace_group
                 | subshell
                 | for_clause
                 | case_clause
                 | if_clause
                 | while_clause
                 | until_clause
                 ;
'''
command = NDef("command",   Or(
    NRef("built-in"),
    NRef("simple_command"),
    NRef("compound_command"),
    And(NRef("compound_command"), NRef("redirect_list")),
    NRef("function_definition")))
NDef("compound_command", Or(
    NRef("brace_group"),
    NRef("subshell"),
    NRef("for_clause"),
#    NRef("case_clause"),
    NRef("if_clause"),
    NRef("while_clause"),
    NRef("until_clause")))
'''
subshell         : '(' compound_list ')'
                 ;
compound_list    : linebreak term
                 | linebreak term separator
                 ;
term             : term separator and_or
                 |                and_or
                 ;
'''
NDef("subshell", And('(', NRef("compound_list"), ")"))
NDef("compound_list", Or(
    And(NRef("linebreak"), NRef("term")),
    And(NRef("linebreak"), NRef("term"), NRef("separator"))))
NDef("term", Or(NRef("true_command"), NRef("false_command"), 
    And(NRef("term"), NRef("separator"), NRef("and_or")),
        NRef("and_or")))
'''
for_clause       : For name                                      do_group
                 | For name                       sequential_sep do_group
                 | For name linebreak in          sequential_sep do_group
                 | For name linebreak in wordlist sequential_sep do_group
                 ;
name             : NAME                     /* Apply rule 5 */
                 ;
in               : In                       /* Apply rule 6 */
                 ;
wordlist         : wordlist WORD
                 |          WORD
                 ;
'''
NDef("for_clause", Or(
    And(NRef("For")," ", NRef("NAME")," ", NRef("do_group")),
    And(NRef("For")," ", NRef("NAME"),NRef("sequential_sep")," ", NRef("do_group")),
    And(NRef("For")," ", NRef("NAME"),NRef("linebreak")," in ",NRef("sequential_sep")," ", NRef("do_group")),
    And(NRef("For")," ", NRef("NAME"),NRef("linebreak")," in ",NRef("wordlist"),NRef("sequential_sep")," ", NRef("do_group"))))
NDef("wordlist", Or(
    And(NRef("wordlist"), NRef("WORD")),
    NRef("WORD")))
'''
case_clause      : Case WORD linebreak in linebreak case_list    Esac
                 | Case WORD linebreak in linebreak case_list_ns Esac
                 | Case WORD linebreak in linebreak              Esac
                 ;
case_list_ns     : case_list case_item_ns
                 |           case_item_ns
                 ;
case_list        : case_list case_item
                 |           case_item
'''

NDef("case_clause", Or(And(NRef("Case"),NRef("WHITESPACE"),NRef("WORD"),NRef("linebreak"),"in",NRef("linebreak"),NRef("case_list"), NRef("Esac")),
    And(NRef("Case"), NRef("WHITESPACE"), NRef("WORD"), NRef("linebreak"), "in", NRef("linebreak"), NRef("case_list_ns"), NRef("Esac")),
    And(NRef("Case"), NRef("WHITESPACE"), NRef("WORD"),NRef("linebreak"),"in",NRef("linebreak"), NRef("Esac"))))

NDef("case_list_ns", Or(
    And(NRef("case_list"), NRef("WHITESPACE"), NRef("case_item_ns")),
    NRef("case_item_ns")))

# avoid left recursion
#NDef("case_list", Or(
#    And(NRef("case_list"), NRef("case_item")),
#    Or(NRef("case_item"))))
NDef("case_list", Join(NRef("case_item"), sep=""))

'''
case_item_ns     :     pattern ')' linebreak    
                 |     pattern ')' compound_list
                 | '(' pattern ')' linebreak
                 | '(' pattern ')' compound_list
                 ;
case_item        :     pattern ')' linebreak     DSEMI linebreak
                 |     pattern ')' compound_list DSEMI linebreak
                 | '(' pattern ')' linebreak     DSEMI linebreak
                 | '(' pattern ')' compound_list DSEMI linebreak
                 ;
pattern          :             WORD         /* Apply rule 4 */
                 | pattern '|' WORD         /* Do not apply rule 4 */
                 ;
'''
NDef("case_item_ns", Or(
        And(NRef("pattern"), NRef("WHITESPACE"), ")", NRef("WHITESPACE"), NRef("linebreak")),
        And(NRef("pattern"), NRef("WHITESPACE"), NRef("compound_list")),
        And("(",NRef("pattern"),")",NRef("linebreak")),
        And("(",NRef("pattern"),")",NRef("WHITESPACE"), NRef("compound_list"))))
NDef("case_item", Or(
    And(NRef("pattern"), NRef("WHITESPACE"), ")",NRef("linebreak"),NRef("DSEMI"),NRef("linebreak")),
    And(NRef("pattern"),NRef("WHITESPACE"), ")",NRef("WHITESPACE"), NRef("compound_list"), NRef("DSEMI"), NRef("linebreak")),
    And("(",NRef("pattern"),NRef("WHITESPACE"), ")",NRef("linebreak"),NRef("DSEMI"), NRef("linebreak")),
    And("(",NRef("pattern"),NRef("WHITESPACE"),")",NRef("WHITESPACE"),NRef("compound_list"),NRef("DSEMI"),NRef("linebreak"))))
NDef("pattern", Or("WORD", And(NRef("pattern"), NRef("WHITESPACE"),"|",NRef("WHITESPACE"),NRef("WORD"),"\"")))
'''
if_clause        : If compound_list Then compound_list else_part Fi
                 | If compound_list Then compound_list           Fi
                 ;
else_part        : Elif compound_list Then compound_list
                 | Elif compound_list Then compound_list else_part
                 | Else compound_list
                 ;
while_clause     : While compound_list do_group
                 ;
until_clause     : Until compound_list do_group
                 ;
function_definition : fname '(' ')' linebreak function_body
                 ;
                 '''
NDef("if_clause", Or(
    And(NRef("If"), NRef("compound_list"), NRef("Then"), NRef("compound_list"),NRef("else_part"),NRef("Fi")),
    And(NRef("If"),NRef("compound_list"),NRef("Then"),NRef("compound_list"),NRef("Fi"))))
NDef("else_part", Or(
    And(NRef("Elif"),NRef("compound_list"),NRef("Then"),NRef("compound_list")),
    And(NRef("Elif"),NRef("compound_list"),NRef("Then"),NRef("compound_list"),NRef("else_part")),
    And(NRef("Else"),NRef("compound_list"))))
NDef("while_clause",And(NRef("While"),NRef("compound_list"),NRef("do_group")))
NDef("until_clause",And(NRef("Until"),NRef("compound_list"),NRef("do_group")))
NDef("function_definition", And(NRef("fname"), "(", ")",NRef("linebreak"),NRef("function_body")))
'''
function_body    : compound_command                /* Apply rule 9 */
                 | compound_command redirect_list"
fname            : NAME                            /* Apply rule 8 */
                 ;
brace_group      : Lbrace compound_list Rbrace
                 ;
do_group         : Do compound_list Done           /* Apply rule 6 */
                 ;
simple_command   : cmd_prefix cmd_word cmd_suffix
                 | cmd_prefix cmd_word
                 | cmd_prefix
                 | cmd_name cmd_suffix
                 | cmd_name
'''
NDef("function_body", Or(
    NRef("compound_command"),
    And(NRef("compound_command"), NRef("redirect_list"))))
NDef("fname",NRef("NAME"))
NDef("brace_group", Or(And(NRef("Lbrace"),NRef("compound_list"),NRef("Rbrace"))))
NDef("do_group",And(NRef("Do"),NRef("compound_list"),NRef("Done")))
simple_command = NDef("simple_command", And(NRef("cmd_prefix"),NRef("cmd_word"),NRef("cmd_suffix")))
#     Or(And(NRef("cmd_prefix"),NRef("cmd_word"),NRef("cmd_suffix")),
#        And(NRef("cmd_prefix"), NRef("cmd_word")),
#        NRef("cmd_prefix"),
#        And(NRef("cmd_name"),NRef("cmd_suffix")),
#        NRef("cmd_name"))
#
'''
cmd_name         : WORD                   /* Apply rule 7a */
                 ;
cmd_word         : WORD                   /* Apply rule 7b */
                 ;
cmd_prefix       :            io_redirect
                 | cmd_prefix io_redirect
                 |            ASSIGNMENT_WORD
                 | cmd_prefix ASSIGNMENT_WORD
                 ;
cmd_suffix       :            io_redirect
                 | cmd_suffix io_redirect
                 |            WORD
                 | cmd_suffix WORD
                 ;
redirect_list    :               io_redirect
                 | redirect_list io_redirect
                 ;
io_redirect      :           io_file
                 | IO_NUMBER io_file
                 |           io_here
                 | IO_NUMBER io_here
                 ;
io_file          : '<'       filename
                 | LESSAND   filename
                 | '>'       filename
                 | GREATAND  filename
                 | DGREAT    filename
                 | LESSGREAT filename
                 | CLOBBER   filename
                 ;
filename         : WORD                      /* Apply rule 2 */
                 ;
io_here          : DLESS     here_end
                 | DLESSDASH here_end
                 ;
here_end         : WORD                      /* Apply rule 3 */
                 ;
newline_list     :              NEWLINE
                 | newline_list NEWLINE
                 ;
linebreak        : newline_list
                 | /* empty */
                 ;
separator_op     : '&'
                 | ';'
                 ;
separator        : separator_op linebreak
                 | newline_list
                 ;
sequential_sep   : ';' linebreak
                 | newline_list
                 ;
'''
NDef("cmd_name", NRef("WORD"))
NDef("cmd_word", NRef("WORD"))
#NDef("cmd_prefix", Or(
#            NRef("io_redirect"),
#            And(NRef("cmd_prefix"),NRef("io_redirect")),
#            NRef("ASSIGNMENT_WORD")),
#            And(NRef("cmd_prefix"), NRef("ASSIGNMENT_WORD")))
NDef("cmd_prefix", Join(Or(NRef("io_redirect"), NRef("ASSIGNMENT_WORD")), sep=" "))
#NDef("cmd_suffix", Or(NRef("io_redirect"), 
#                      And(NRef("cmd_suffix"), NRef("io_redirect")),
#                      NRef("WORD"),
#                      And(NRef("cmd_suffix"), NRef("WORD"))))
NDef("cmd_suffix", Join(Or(NRef("io_redirect"), NRef("WORD")), sep=" "))

NDef("redirect_list", Or(NRef("io_redirect"), And(NRef("redirect_list"),NRef("io_redirect"))))
NDef("io_redirect", Or(NRef("io_file"),
                 And(NRef("IO_NUMBER"), NRef("io_file")),
                 NRef("io_here"),
                 And(NRef("IO_NUMBER"), NRef("io_here"))))
NDef("io_file", Or(
    And("<", NRef("filename")),
    And(NRef("LESSAND"), NRef("filename")),
    And('>', NRef("filename")),
    And(NRef("GREATAND"), NRef("filename")),
    And(NRef("DGREAT"), NRef("filename")),
    And(NRef("LESSGREAT"), NRef("filename")),
    And(NRef("CLOBBER"), NRef("filename"))))
NDef("filename",  NRef("WORD"))
NDef("io_here",  Or(
            And(NRef("DLESS"), NRef("here_end")), # TODO needs more! generate the contents of the heredoc (a bunch of words on lines) followed by the delimiter. delimiter may be quoted
            And(NRef("DLESSDASH"), NRef("here_end"))))
NDef("here_end", NRef("WORD"))
NDef("newline_list", Or(NRef("NEWLINE"),
                    And(NRef("newline_list"), NRef("NEWLINE"))))
NDef("linebreak",  Or(NRef("newline_list"), ""))
#is this what empty means?
NDef("separator_op", Or('&',';'))
NDef("separator", Or(And(NRef("separator_op"), NRef("linebreak")), NRef("newline_list")))
NDef("sequential_sep", Or(';',NRef("linebreak"),NRef("newline_list")))
