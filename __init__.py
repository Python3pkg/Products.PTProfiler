"""Small PT profiler system that monkeypatches PythonExpr, PathExpr and StringExpr to time calls
"""

"""
Copyright (c) 2003 Infrae. All rights reserved.
See also LICENSE.txt
Version of this file: $Revision: 1.2 $
Written by Guido Wesdorp
E-mail: guido@infrae.com
"""

import time

class ProfileContainer:
    """The container (nested dict) for the profiling result
    """
    def __init__(self):
        self._templates = {}

    def hit(self, templatename, expr, time):
        """Add the data of a hit to the dict
        """
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

# create a global instance of the container
profile_container = ProfileContainer()

def __patched_call__(self, econtext):
    """The actual patched method

    Doesn't do much more than recording the time calling an expression takes
    """
    name = self._patching_class._get_name(econtext)
    expr = self._patching_class._get_expr(self)
    starttime = time.time()
    ret = self._patching_class._org_method(self, econtext)
    profile_container.hit(name, expr, time.time() - starttime)

    return ret

class ProfilerPatch:
    """A generic class to hook into expression objects
    """
    def __init__(self, type, class_to_patch):
        self._type = type
        self._org_method = class_to_patch.__call__
        class_to_patch.__call__ = __patched_call__
        class_to_patch._patching_class = self

    def _get_name(self, econtext):
        if econtext.contexts.has_key('template'):
            name = getattr(econtext.contexts['template'], '_filepath', None) or getattr(econtext.contexts['template'], 'filename', None) or getattr(econtext.contexts['template'], 'id')
        else:
            name = getattr(econtext.contexts['form'], '_filepath', 'None') or getattr(econtext.contexts['form'], 'id')
        return name

    def _get_expr(self, obj):
        if self._type == 'python':
            return 'python: %s' % obj.expr
        else:
            return '%s: %s' % (self._type, obj._s)

# here the actual monkeypatching takes place
from Products.PageTemplates.ZRPythonExpr import PythonExpr
ProfilerPatch('python', PythonExpr)

from Products.PageTemplates.Expressions import PathExpr
ProfilerPatch('path', PathExpr)

from Products.PageTemplates.Expressions import StringExpr
ProfilerPatch('string', StringExpr)

#-----------------------------------------------------------------------------
# Plain Zope Product registration
#-----------------------------------------------------------------------------

# of course we have some registration to Zope to do here as well...
import PTProfilerViewer

def initialize(context):
    context.registerClass(
        PTProfilerViewer.PTProfilerViewer,
        constructors=(PTProfilerViewer.manage_addPTProfilerViewerForm,
                      PTProfilerViewer.manage_addPTProfilerViewer),
        icon='',
        )
