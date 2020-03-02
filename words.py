from gramfuzz.fields import *
import gramfuzz.rand as gr
class NRef(Ref):
    cat = "word"
class NDef(Def):
    cat = "word"
# TODO
# whitespace around keywords
# generalize whitespace to zero-or-more space or tabs
# clean up formatting
# different categories for words and program statements? (not super important)
# figure out how to generate more strings and fewer special characters
weightedOr=lambda y,z,x : y if gr.maybe(prob=x) else z
charset_nonspecial = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
charset_nonspecial_rest="-_+.,/!"
#Def("charset_special_conditions_for_quoting", 
# Or("*", "?", "[", "#", "˜", "=", "%"), cat="word")
NDef("header", "#!/bin/")
#for beginning of programs i.e. #!/bin/zsh
NDef("charsthatneedquotes",
     Or("|", "&",";", "<", ">", "(", ")", "$", "`", "\\", "\"", "\'" , " ", "\n"))
#characters that require single or double quotes
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
NDef("s", weightedOr(
        String(charset = charset_nonspecial, min=1, max=15),
        Or(
            String(charset=charset_nonspecial_rest, min=1, max=10),
            NRef("s"),
            NRef("parens"),
            NRef("charsthatneedquotes")
        ), 0.9
    ))
NDef("tilde", Or(
    "~", 
    And(
        "~",
        String(charset=String.charset_alpha, min=1, max=1),
        String(charset=String.charset_alphanum, min=0, max=10)
    ),
    And(
        "~",
        NRef("s")
    ),
    ))
#braces needed?
NDef("FMTw", Or("-", "-:", "=", "=:", "+", "+:", "?", "?:", "%", "%%",  "#", "##"))
NDef("varname",
     And(String(charset=String.charset_alpha+b"_", min=1, max=1),
         String(charset=String.charset_alphanum+b"_", min=1, max=15)))
NDef("NAME",Or(
    NRef("varname"),
    Or("@", "*", "#", "?", "-", "$", "!")))
#these parens can have parens inside themselves:
NDef("recursableparens",Or(
    And("${", NRef("NAME"), "}"), 
    And("${#", NRef("NAME"), "}"),
    And("${", And(NRef("NAME"), NRef("FMTw"), NRef("WORD"), "}"))),)
NDef("parens",Or(
    And("$", NRef("NAME"), NRef("recursableparens"))),
    And("$(", NRef("NAME") , ")"),
    And("$((", NRef("NAME"), "))"))
#Rules for tilde:
NDef("~orVariable",Or(
    NRef("tilde"),
    NRef("parens")))
'''
/* -------------------------------------------------------
   The grammar symbols
   ------------------------------------------------------- */
%token  WORD
%token  ASSIGNMENT_WORD
%token  NAME
%token  NEWLINE //what are these?
%token  IO_NUMBER'''
word = NDef("WORD", Join(Or(NRef("s"), NRef("~orVariable")), sep="", max=6))
NDef("ASSIGNMENT_WORD", And(NRef("NAME"), "=", NRef("WORD")))
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
     Or(
         ";;",
         And(
             NRef("WHITESPACE"),
             ';;',
             NRef("WHITESPACE")
         )
    )
)    
NDef("DLESS",
     Or(
         "<<",
         And(
             NRef("WHITESPACE"),
             '<<',
             NRef("WHITESPACE")
         )
     )
)
NDef("DGREAT",
     Or(
         ">>",
         And(
             NRef("WHITESPACE"),
             '>>',
             NRef("WHITESPACE")
         )
     )
)
NDef("LESSAND",
     Or(
         "<&",
         And(
             NRef("WHITESPACE"),
             '<&',
             NRef("WHITESPACE")
         )
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
    Or(
        NRef("WHITESPACE"),
        NRef("NEWLINE"),
        NRef("TAB"),
        And(NRef("NEWLINE"), NRef("WHITESPACE")),
        And(NRef("TAB"), NRef("WHITESPACE")),
        " ",
        And(" ", NRef("WHITESPACE"))
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
    And(NRef("Bang"), NRef("pipe_sequence"))
))
NDef("pipe_sequence", Or(
    NRef("command"),
    And(NRef("pipe_sequence"), "|", NRef("linebreak"), NRef("command"))
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
NDef("term", Or(
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

NDef("case_clause", Or(And(NRef("Case"),NRef("WORD"),NRef("linebreak"),"in",NRef("linebreak"),NRef("case_list"), NRef("Esac")),
    And(NRef("Case"), NRef("WORD"), NRef("linebreak"), "in", NRef("linebreak"), NRef("case_list_ns"), NRef("Esac")),
    And(NRef("Case"),NRef("WORD"),NRef("linebreak"),"in",NRef("linebreak"), NRef("Esac"))))

NDef("case_list_ns", Or(
    And(NRef("case_list"), NRef("case_item_ns")),
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
        And(NRef("pattern"), ")", NRef("linebreak")),
        And(NRef("pattern"), NRef("compound_list")),
        And("(",NRef("pattern"),")",NRef("linebreak")),
        And("(",NRef("pattern"),")",NRef("compound_list"))))
NDef("case_item", Or(
    And(NRef("pattern"), ")",NRef("linebreak"),NRef("DSEMI"),NRef("linebreak")),
    And(NRef("pattern"), ")",NRef("compound_list"), NRef("DSEMI"), NRef("linebreak")),
    And("(",NRef("pattern"),")",NRef("linebreak"),NRef("DSEMI"), NRef("linebreak")),
    And("(",NRef("pattern"),")",NRef("compound_list"),NRef("DSEMI"),NRef("linebreak"))))
NDef("pattern", Or("WORD", And(NRef("pattern"), "|",NRef("WORD"),"\"")))
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
            And(NRef("DLESS"), NRef("here_end")),
            And(NRef("DLESSDASH"), NRef("here_end"))))
NDef("here_end", NRef("WORD"))
NDef("newline_list", Or(NRef("NEWLINE"),
                    And(NRef("newline_list"), NRef("NEWLINE"))))
NDef("linebreak",  Or(NRef("newline_list"), ""))
#is this what empty means?
NDef("separator_op", Or('&',';'))
NDef("separator", Or(And(NRef("separator_op"), NRef("linebreak")), NRef("newline_list")))
NDef("sequential_sep", Or(';',NRef("linebreak"),NRef("newline_list")))
