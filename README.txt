Copyright (c) 2003 Infrae. All rights reserved.
See also LICENSE.txt

Meta::
  
  Valid for:  PTProfiler 0.1 
  Author:     Guido Wesdorp
  Email:      guido@infrae.com
  CVS:        $Revision: 1.1 $

PTProfiler

    PTProfiler is a small profiling system for pagetemplates. It times each
    call to Python expressions, path expressions and string expressions and
    shows the results on a webpage.

Installing PTProfiler

  See INSTALL.txt

Using PTProfiler

    To use the profiler on a site, just place the product in Zope's Products
    directory. From that moment on, the website will be profiled. Do mind that
    this requires some extra processing time for pagetemplates, so isn't 
    recommended for production sites.
    To view the results, place a 'PTProfiler Viewer' object somewhere in the
    Zope tree and view it through the ZMI. You will see a list of paths to
    pagetemplates (or, in the rare case the path isn't known, the id), all of
    which are clickable. When you click one of the items, you will see a
    list of all the expression calls in the template, ordered by total time 
    spent on that expression.

License
  
  PTProfiler is released under the BSD license. See 'LICENSE.txt'.
