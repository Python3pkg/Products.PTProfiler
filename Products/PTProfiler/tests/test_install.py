import unittest

from Products.PTProfiler.testing import PTPROFILER


class TestInstall(unittest.TestCase):
    layer = PTPROFILER

    def test_patched(self):
        from zope.pagetemplate.pagetemplate import PageTemplate
        self.assertTrue(hasattr(PageTemplate, '_patching_class'))
