from specified import *
from builtin import *
NDef("s",  String(charset = charset_nonspecial, min=1, max=25))
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
                         And(NRef("single_quote"), NRef("repr"),NRef("single_quote"),  " ",),
                         And(NRef("double_quote"), NRef("repr"), NRef("double_quote"),  " ",)
                         )
)
NDef("digit", Or("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"))
Def("charset_special_conditions_for_quoting", Or("*", "?", "[", "#", "˜", "=", "%"))
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
NDef("varname", And(" ",
     Or( NRef("globalvar"),
     And(String(charset=String.charset_alpha+b"_", min=1, max=1),
         String(charset=String.charset_alphanum+b"_", min=1, max=15)
     )), " "))
NDef("NAME", WeightedOr(
    (NRef("varname"), 0.9),
    (Or("@", "*", "#", "?", "-", "$", "!"), 0.1)))
#these parens can have parens inside themselves:
NDef("recursableparens",Or(
    And("${ ", NRef("NAME"), " }"),
    And("${# ", NRef("NAME"), " }"),
    And("${ ", And(NRef("NAME"), NRef("FMTw"), NRef("WORD"), " }"))),)
NDef("parens",Or(
    And("$ ", NRef("NAME")," ", NRef("recursableparens"))),
    And("$( ", NRef("NAME") , " )"),
    And("$(( ", NRef("NAME")," ))"))
#Rules for tilde:
NDef("~orVariable",Or(
    NRef("tilde"),
    NRef("parens")
)
)
