from gramfuzz.fields import *
charset_nonspecial = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-_+.,/!^"
s = String(charset = charset_nonspecial, min=1,max=10)
tilde=Or("~", And("~", String(charset=String.charset_alpha, min=1, max=1), String(charset=String.charset_alphanum, min=0, max=10)))
#braces needed?
ifstatement=Or(And("if", s, "then", s, Opt("else"), s, "fi"),
                And("if", "condition", "then", s, Opt("else"), s, "fi"),
                And("if [ condition ] ", "then", s,  Opt("else"), s, "fi")
)
reserved_keywords=Or()
name=Or(String(charset=String.charset_alphanum+b"_", min=1, max=15), Opt("@"), Opt("*"), Opt("#"), Opt("?"), Opt("-"), Opt("$"), Opt("!"))
var=And(Or(name, And("${", name, "}")), "=")
k=Or(tilde, var)
w=Join(Or(s, k), sep="", max=6)
fields=Join(w, sep=" ", max=10)
for x in range(10):
    print(fields.build().decode("utf-8"))
    print()



'''class NRef(Ref):
    cat="var_def"
class NDef(Ref):
    cat="var_def"
Def("vars",
    Join(
        Opt("variable_names")
    )
)'''
