"""
PTPathProfiler is a small pagetemplate expression profiler that monkeypatches expression
classes to measure the speed of individual expressions

Copyright (c) 2003 Infrae. All rights reserved.
See also LICENSE.txt
Version of this file: $Revision: 1.3 $
Written by Guido Wesdorp
E-mail: guido@infrae.com
"""

# import the profiling machinery and monkeypatch the expression objects
from ProfilerPatch import ProfilerPatch
from Products.PageTemplates.ZRPythonExpr import PythonExpr
from Products.PageTemplates.Expressions import PathExpr, StringExpr
ProfilerPatch('python', PythonExpr)
ProfilerPatch('path', PathExpr)
ProfilerPatch('string', StringExpr)


import PTProfilerViewer

def initialize(context):
    context.registerClass(
        PTProfilerViewer.PTProfilerViewer,
        constructors=(PTProfilerViewer.manage_addPTProfilerViewerForm,
                      PTProfilerViewer.manage_addPTProfilerViewer),
        icon='',
        )
