/* Generated automatically from Python-2.7.13/Modules/config.c.in */
/* -*- C -*- ***********************************************
Copyright (c) 2000, BeOpen.com.
Copyright (c) 1995-2000, Corporation for National Research Initiatives.
Copyright (c) 1990-1995, Stichting Mathematisch Centrum.
All rights reserved.

See the file "Misc/COPYRIGHT" for information on usage and
redistribution of this file, and for a DISCLAIMER OF ALL WARRANTIES.
******************************************************************/

/* Module configuration */

/* !!! !!! !!! This file is edited by the makesetup script !!! !!! !!! */

/* This file contains the table of built-in modules.
   See init_builtin() in import.c. */

#include "Python.h"

#ifdef __cplusplus
extern "C" {
#endif


extern void initcStringIO(void);
extern void initerrno(void);
extern void initfastlex(void);
extern void initfcntl(void);
extern void initlibc(void);
#ifdef HAVE_READLINE
extern void initline_input(void);
#endif
extern void initposix_(void);
extern void initpwd(void);
extern void initresource(void);
extern void initsignal(void);
extern void inittermios(void);
extern void inittime(void);
extern void init_weakref(void);
extern void inityajl(void);
extern void initzipimport(void);

extern void PyMarshal_Init(void);
extern void initimp(void);
extern void initgc(void);
extern void init_ast(void);
extern void _PyWarnings_Init(void);

struct _inittab _PyImport_Inittab[] = {

    {"cStringIO", initcStringIO},
    {"errno", initerrno},
    {"fastlex", initfastlex},
    {"fcntl", initfcntl},
    {"libc", initlibc},
#ifdef HAVE_READLINE
    {"line_input", initline_input},
#endif
    {"posix_", initposix_},
    {"pwd", initpwd},
    {"resource", initresource},
    {"signal", initsignal},
    {"termios", inittermios},
    {"time", inittime},
    {"_weakref", init_weakref},
    {"yajl", inityajl},
    {"zipimport", initzipimport},

    /* This module lives in marshal.c */
    {"marshal", PyMarshal_Init},

    /* This lives in import.c */
    {"imp", initimp},

    /* This lives in Python/Python-ast.c */
#ifndef OVM_MAIN
    {"_ast", init_ast},
#endif

    /* These entries are here for sys.builtin_module_names */
    {"__main__", NULL},
    {"__builtin__", NULL},
    {"sys", NULL},
    {"exceptions", NULL},

    /* This lives in gcmodule.c */
    {"gc", initgc},

    /* This lives in _warnings.c */
    {"_warnings", _PyWarnings_Init},

    /* Sentinel */
    {0, 0}
};


#ifdef __cplusplus
}
#endif
