import Globals
from AccessControl import ClassSecurityInfo
from OFS.SimpleItem import SimpleItem
from Products.PageTemplates.PageTemplateFile import PageTemplateFile
from Products.Silva.helpers import add_and_edit

from ProfileContainer import profile_container

"""Here the actual patching of the expression calls takes place

Of course this is also used to register the product code to Zope
"""

"""
Copyright (c) 2003 Infrae. All rights reserved.
See also LICENSE.txt
Version of this file: $Revision: 1.3 $
Written by Guido Wesdorp
E-mail: guido@infrae.com
"""

class PTProfilerViewer(SimpleItem):
    """The view object for the PTProfiler
    """

    security = ClassSecurityInfo()
    meta_type = 'PTProfiler Viewer'
    
    manage_options = ({'label': 'View', 'action': 'view_tab'},) + SimpleItem.manage_options
    
    manage_main = view_tab = PageTemplateFile('www/PTProfilerViewTab', globals(), __name__='view_tab')

    _perm = 'View PTProfiler'
    
    security.declareProtected(_perm, 'full_result')
    def full_result(self, name=None):
        res = profile_container._templates

        if name:
            return res[name]
        else:
            return res

    security.declareProtected(_perm, 'result_sorted_by_time')
    def result_sorted_by_time(self, name):
        """Returns a list of (expr, time, hits) tuples sorted by time"""
        res = profile_container._templates[name]

        ret = []
        for expr, value in res.items():
            if not expr == 'total':
                ret.append((expr, value['time'], value['hits']))

        ret.sort(self._sort_by_time)

        return ret

    security.declareProtected(_perm, 'profiled_templates')
    def profiled_templates(self):
        return profile_container._templates.keys()

    security.declareProtected(_perm, 'total_rendering_time')
    def total_rendering_time(self, ptname):
        return profile_container._templates[ptname]['total']['time']

    security.declareProtected(_perm, 'total_pt_hits')
    def total_pt_hits(self, ptname):
        return profile_container._templates[ptname]['total']['hits']

    def _sort_by_time(self, a, b):
        return cmp(b[1], a[1])

Globals.InitializeClass(PTProfilerViewer)

manage_addPTProfilerViewerForm = PageTemplateFile(
        'www/addPTProfilerViewer', globals(),
        __name__ = 'manage_addPTProfilerViewerForm')

def manage_addPTProfilerViewer(self, id, title='', REQUEST=None):
    """Add viewer
    """
    id = self._setObject(id, PTProfilerViewer(id, title))
    add_and_edit(self, id, REQUEST)
    return ''
