"""The code used for monkeypatching and time measurement
"""

from ProfileContainer import profile_container
import time

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

