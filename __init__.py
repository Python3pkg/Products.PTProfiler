"""Small PT profiler system that monkeypatches PythonExpr, PathExpr and StringExpr to time calls
"""

"""
Copyright (c) 2003 Infrae. All rights reserved.
See also LICENSE.txt
Version of this file: $Revision: 1.1 $
Written by Guido Wesdorp
E-mail: guido@infrae.com
"""

import time

class ProfileContainer:
    def __init__(self):
        self._templates = {}

    def hit(self, templatename, expr, time):
        if not self._templates.has_key(templatename):
            self._templates[templatename] = {}

        template = self._templates[templatename]

        if not template.has_key(expr):
            template[expr] = {}
            template[expr]['time'] = time
            template[expr]['hits'] = 1
        else:
            template[expr]['time'] += time
            template[expr]['hits'] += 1

profile_container = ProfileContainer()

old_pyexpr_call = None
old_pathexpr_call = None
old_stringexpr_call = None

def pyexpr_profiling_call(self, econtext):
    if econtext.contexts.has_key('form'):
        name = getattr(econtext.contexts['form'], '_filepath', 'None') or getattr(econtext.contexts['form'], 'id')
    else:
        name = getattr(econtext.contexts['template'], '_filepath', None) or getattr(econtext.contexts['template'], 'filename', None) or getattr(econtext.contexts['template'], 'id')
    starttime = time.time()
    ret = old_pyexpr_call(self, econtext)
    profile_container.hit(name, 'python: ' + self.expr, (time.time() - starttime))
    return ret
    
def pathexpr_profiling_call(self, econtext):
    if econtext.contexts.has_key('form'):
        name = getattr(econtext.contexts['form'], '_filepath', 'None') or getattr(econtext.contexts['form'], 'id')
    else:
        name = getattr(econtext.contexts['template'], '_filepath', None) or getattr(econtext.contexts['template'], 'filename', None) or getattr(econtext.contexts['template'], 'id')
    starttime = time.time()
    ret = old_pathexpr_call(self, econtext)
    profile_container.hit(name, 'path: ' + self._s, (time.time() - starttime))
    return ret

def stringexpr_profiling_call(self, econtext):
    if econtext.contexts.has_key('form'):
        name = getattr(econtext.contexts['form'], '_filepath', 'None') or getattr(econtext.contexts['form'], 'id')
    else:
        name = getattr(econtext.contexts['template'], '_filepath', None) or getattr(econtext.contexts['template'], 'filename', None) or getattr(econtext.contexts['template'], 'id')
    starttime = time.time()
    ret = old_stringexpr_call(self, econtext)
    profile_container.hit(name, 'string: ' + self._s, (time.time() - starttime))
    return ret

from Products.PageTemplates.ZRPythonExpr import PythonExpr
old_pyexpr_call = PythonExpr.__call__
PythonExpr.__call__ = pyexpr_profiling_call

from Products.PageTemplates.Expressions import PathExpr
old_pathexpr_call = PathExpr.__call__
PathExpr.__call__ = pathexpr_profiling_call

from Products.PageTemplates.Expressions import StringExpr
old_stringexpr_call = StringExpr.__call__
StringExpr.__call__ = stringexpr_profiling_call

import PTProfilerViewer

def initialize(context):
    context.registerClass(
        PTProfilerViewer.PTProfilerViewer,
        constructors=(PTProfilerViewer.manage_addPTProfilerViewerForm,
                      PTProfilerViewer.manage_addPTProfilerViewer),
        icon='',
        )
