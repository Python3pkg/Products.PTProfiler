"""
PTPathProfiler is a small pagetemplate expression profiler that monkeypatches expression
classes to measure the speed of individual expressions

Copyright (c) 2003 Infrae. All rights reserved.
See also LICENSE.txt
Version of this file: $Revision: 1.4 $
Written by Guido Wesdorp
E-mail: guido@infrae.com
"""

# import the profiling machinery and monkeypatch the objects
from ProfilerPatch import ExprProfilerPatch, PTProfilerPatch

from Products.PageTemplates.PageTemplate import PageTemplate
PTProfilerPatch(PageTemplate)

from Products.PageTemplates.ZRPythonExpr import PythonExpr
from Products.PageTemplates.Expressions import PathExpr, StringExpr
ExprProfilerPatch('python', PythonExpr)
ExprProfilerPatch('path', PathExpr)
ExprProfilerPatch('string', StringExpr)


import PTProfilerViewer

def initialize(context):
    context.registerClass(
        PTProfilerViewer.PTProfilerViewer,
        constructors=(PTProfilerViewer.manage_addPTProfilerViewerForm,
                      PTProfilerViewer.manage_addPTProfilerViewer),
        icon='',
        )
