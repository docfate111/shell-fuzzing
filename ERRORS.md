I am using dash with shellcheck since it is somewhat POSIX compliant and minimal
Unspecified behavior that seems to cause errors on several shells
- {} requires a newline or ; in dash and some other shells
- "functionname"() function-definition without brackets causes errors with Dash


Unrelated issue: heredocs could be anything but in the grammar code I would need every heredoc to be the same 
random string otherwise they would not match
