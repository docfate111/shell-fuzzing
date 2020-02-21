from gramfuzz.fields import *
class NRef(Ref):
    cat = "word"
class NDef(Def):
    cat = "word"
charset_nonspecial = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-_+.,/!^"
#Def("charset_special_conditions_for_quoting", 
# Or("*", "?", "[", "#", "˜", "=", "%"), cat="word")
Def("charsthatneedquotes",
Or("|", "&",";", "<", ">", "(", ")", "$", "`", "\\", "\"", "\'" , " ", "\n"), 
cat="word")
Def("quotedcharswithsingleordoublequotes", 
Or(And("'", NRef("charsthatneedquotes"), "'"),
And("\"", NRef("charsthatneedquotes"), "\"")
), cat="word")
Def("s", 
Or(String(charset = charset_nonspecial, min=1,max=10), NRef("s"), NRef("parens"),
NRef("charsthatneedquotes")), cat="word"),
Def("tilde", 
Or("~", 
And("~", String(charset=String.charset_alpha, min=1, max=1), String(charset=String.charset_alphanum, min=0, max=10)),
And("~", NRef("s"))), cat="word")
#braces needed?
Def("ifstatement", 
Or(And("if ", NRef("s"), "\nthen ", Opt(NRef("s")), Opt("else"), NRef("s"), "fi"),
                And("if ", "condition", "\nthen ", NRef("s"), Or("","else"), NRef("s"), "fi"),
                And("if [ condition ] ", "\nthen ", NRef("s"),  Or("", "else"), NRef("s"), "fi")
), cat="word")
Def("FMTw", 
Or("-", "-:", "=", "=:", "+", "+:", "?", "?:", "%", "%%",  "#", "##"),
cat="word")
Def("name",
Or(String(charset=String.charset_alphanum+b"_", min=1, max=15),
"@", "*", "#", "?", "-", "$", "!"), cat="word")
Def("recursableparens",
Or(And("${", NRef("name"), "}"), 
  And("${#", NRef("name"), "}"),
  And("${", And(NRef("name"), NRef("FMTw"), "}"))),
  cat="word")
Def("parens",
Or(And("$", NRef("name"),
  NRef("recursableparens"))),
  And("$(", NRef("name") , ")"),
  And("$((", NRef("name"), "))"), cat="word")
Def("~orVariable",
 Or(NRef("tilde"), NRef("parens")), cat="word")
#Def("fields",
#Join(NRef("w"), sep=" ", max=10),
#cat="word")
'''
/* -------------------------------------------------------
   The grammar symbols
   ------------------------------------------------------- */
%token  WORD
%token  ASSIGNMENT_WORD
%token  NAME
%token  NEWLINE //what are these?
%token  IO_NUMBER'''
Def("WORD", NRef("s"))
Def("ASSIGNMENT_WORD", "assignmenthere")
Def("NAME", NRef("name"))
Def("NEWLINE", "\n")
Def("IO_NUMBER", "number here")
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
Def("AND_IF", "&&")
Def("OR_IF", '||')
Def("DSEMI", ";;")
Def("DLESS", "<<")
Def("DGREAT", ">>")
Def("LESSAND", "<&")
Def("GREATAND", ">&")
Def("LESSGREAT", "<>")
Def("DLESSDASH", "<<-")
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
Def("If", "if")
Def("Then", "then")
Def("Else", "else")
Def("Elif", "elif")
Def("Fi", "fi")
Def("Do", "do")
Def("Done", "done")
Def("Case", "case")
Def("Esac", "esac")
Def("While", "while")
Def("Until",  "until")
Def("For", "for")
Def("Lbrace", "{")
Def("Rbrace", "}")
Def("Bang", "!")
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
Def("program", Or(And(NRef("linebreak"), NRef("complete_commands"), NRef("linebreak"), NRef("linebreak"))))
Def("complete_commands", Or(And(NRef("complete_commands"), NRef("newline_list"), NRef("complete_command")), NRef("complete_command")))
'''
list             : list separator_op and_or
                 |                   and_or
                 ;
and_or           :                         pipeline
                 | and_or AND_IF linebreak pipeline
                 | and_or OR_IF  linebreak pipeline
                 ;
'''
Def("list", Or(And(NRef("list"), NRef("separator_op"), NRef("and_or")), NRef("and_or")))
Def("and_or", Or(NRef("pipeline"), 
                And(NRef("and_or"), NRef("AND_IF"), NRef("linebreak"), NRef("pipeline")),
                And(NRef("and_or"), NRef("OR_IF"), NRef("linebreak"), NRef("pipeline"))
))
'''
pipeline         :      pipe_sequence
                 | Bang pipe_sequence
                 ;
pipe_sequence    :                             command
                 | pipe_sequence '|' linebreak command
                 ;
'''
Def("pipeline", Or(
    NRef("pipeline"),
    And(NRef("Bang"), NRef("pipe_sequence"))
))
Def("pipe_sequence", Or(
    NRef("command"),
    And(NRef("pipesequence"), "|", NRef("linebreak"), NRef("command"))
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
Def("command",   Or(
    NRef("simple_command"),
    NRef("compound_command"),
    And(NRef("compound_command"), NRef("redirect_list")),
    NRef("function_definition")))
Def("compound_command", Or(
    NRef("brace_group"),
    NRef("subshell"),
    NRef("for_clause"),
    NRef("case_clause"),
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
Def("subshell", And('(', NRef("compound_list"), ')'))
Def("compound_list", Or(
    And(NRef("linebreak"), NRef("term")),
    And(NRef("linebreak"), NRef("term"), NRef("separator"))))
Def("term", Or(
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
Def("for_clause", Or(
    And(NRef("For"),NRef("name"),NRef("do_group")),
    And(NRef("For"),NRef("name"),NRef("sequential_sep"),NRef("do_group")),
    And(NRef("For"),NRef("name"),NRef("linebreak"),NRef("in"),NRef("sequential_sep,do_group")),
    And(NRef("For"),NRef("name"),NRef("linebreak"),NRef("in"),NRef("wordlist"),NRef("sequential_sep"),NRef("do_group"))))
Def("name", NRef("NAME"))
Def("in", NRef("In"))
Def("wordlist", Or(
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
Def("case_clause", Or(
    And(NRef("Case"),NRef("WORD"),NRef("linebreak"),NRef("in"),NRef("linebreak"),NRef("case_list"), NRef("Esac")),
    And(NRef("Case"), NRef("WORD"), NRef("linebreak"), NRef("in"), NRef("linebreak"), NRef("case_list_ns"), NRef("Esac")),
    And(NRef("Case"),NRef("WORD"),NRef("linebreak"),NRef("in"),NRef("linebreak"), NRef("Esac"))))
Def("case_list_ns", Or(
    And(NRef("case_list"), NRef("case_item_ns")),
    NRef("case_item_ns")))
Def("case_list", Or(
    And(NRef("case_list"), NRef("case_item")),
    Or(NRef("case_item"))))
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
Def("case_item_ns", Or(
        And(NRef("pattern"), ")", NRef("linebreak")),
        And(NRef("pattern"), NRef("compound_list")),
        And("(",NRef("pattern"), NRef(")"),NRef("linebreak")),
        And("(",NRef("pattern"),")",NRef("compound_list"))))
Def("case_item", Or(
    And(NRef("pattern"), ")",NRef("linebreak"),NRef("DSEMI"),NRef("linebreak")),
    And(NRef("pattern"), ")",NRef("compound_list"), NRef("DSEMI"), NRef("linebreak")),
    And("(",NRef("pattern"),")",NRef("linebreak"),NRef("DSEMI"), NRef("linebreak")),
    And("(",NRef("pattern"),")",NRef("compound_list"),NRef("DSEMI"),NRef("linebreak"))))
Def("pattern", Or("WORD", And(NRef("pattern"), NRef('|'),NRef("WORD"),"\"")))
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
Def("if_clause", Or(
    And(NRef("If"), NRef("compound_list"), NRef("Then"), NRef("compound_list"),NRef("else_part"),NRef("Fi")),
    And(NRef("If"),NRef("compound_list"),NRef("Then"),NRef("compound_list"),NRef("Fi"))))
Def("else_part", Or(
    And(NRef("Elif"),NRef("compound_list"),NRef("Then"),NRef("compound_list")),
    And(NRef("Elif"),NRef("compound_list"),NRef("Then"),NRef("compound_list"),NRef("else_part")),
    And(NRef("Else"),NRef("compound_list"))))
Def("while_clause",And(NRef("While"),NRef("compound_list"),NRef("do_group")))
Def("until_clause",And(NRef("Until"),NRef("compound_list"),NRef("do_group")))
Def("function_definition", And(NRef("fname"), "(", ")",NRef("linebreak"),NRef("function_body")))
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
Def("function_body", Or(
    NRef("compound_command"),
    And(NRef("compound_command"), NRef("redirect_list"))))
Def("fname",NRef("NAME"))
Def("brace_group", Or(And(NRef("Lbrace"),NRef("compound_list"),NRef("Rbrace"))))
Def("do_group",And(NRef("Do"),NRef("compound_list"),NRef("Done")))
Def("simple_command", Or(
    And(NRef("cmd_prefix"),NRef("cmd_word"),NRef("cmd_suffix")),
    And(NRef("cmd_prefix"), NRef("cmd_word")),
    NRef("cmd_prefix"),
    And(NRef("cmd_name"),NRef("cmd_suffix")),
    NRef("cmd_name")))
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
Def("cmd_name", NRef("WORD"))
Def("cmd_word", NRef("WORD"))
Def("cmd_prefix", Or(
            NRef("io_redirect"),
            And(NRef("cmd_prefix"),NRef("io_redirect")),
            NRef("ASSIGNMENT_WORD")),
            And(NRef("cmd_prefix"), NRef("ASSIGNMENT_WORD")))
Def("cmd_suffix", Or(NRef("io_redirect"),
                    And(NRef("cmd_suffix"), NRef("io_redirect")),
                 NRef("WORD"),
                 And(NRef("cmd_suffix"),NRef("WORD"))))
Def("redirect_list", Or(NRef("io_redirect"), And(NRef("redirect_list"),NRef("io_redirect"))))
Def("io_redirect", Or(NRef("io_file"),
                 And(NRef("IO_NUMBER"), NRef("io_file")),
                 NRef("io_here"),
                 And(NRef("IO_NUMBER"), NRef("io_here"))))
Def("io_file", Or(
    And("<", NRef("filename")),
    And("LESSAND", NRef("filename")),
    And('>', NRef("filename")),
    And(NRef("GREATAND"), NRef("filename")),
    And(NRef("DGREAT"), NRef("filename")),
    And(NRef("LESSGREAT"), NRef("filename")),
    And(NRef("CLOBBER"), NRef("filename"))))
Def("filename",  NRef("WORD"))
Def("io_here",  Or(
            And(NRef("DLESS"), NRef("here_end")),
            And(NRef("DLESSDASH"), NRef("here_end"))))
Def("here_end", NRef("WORD"))
Def("newline_list", Or(NRef("NEWLINE"),
                    And(NRef("newline_list"), NRef("NEWLINE"))))
Def("linebreak",  Or(NRef("newline_list"), ""))
#is this what empty means?
Def("separator_op", Or('&',';'))
Def("separator", Or(And("separator_op", "linebreak"), NRef("newline_list")))
Def("sequential_sep", Or(';',NRef("linebreak"),NRef("newline_list")))
#This line breaks program :(
#Def("w", 
#Or(Join(Or(NRef("s"), NRef("~orVariable")), sep="", max=6), NRef("program")),
#cat="word")