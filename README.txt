Copyright (c) 2003-2005 Infrae. All rights reserved.
See also LICENSE.txt

Meta::
  
    Valid for:  PTProfiler 0.3
    Author:     Guido Wesdorp
    Email:      guido@infrae.com
    CVS:        $Revision: 1.3 $

PTProfiler

    PTProfiler is a small profiling system for pagetemplates. It times each
    TAL expression and shows the results on a webpage.

Installing PTProfiler

    See INSTALL.txt

Using PTProfiler

    To use the profiler on a site, just place the product in Zope's Products
    directory. Do mind that this product (when enabled, see below) requires
    some extra processing time for pagetemplates, so isn't recommended for
    production sites.
    To enable profiling and view the results, place a 'PTProfiler Viewer'
    object somewhere in the Zope tree, and press the 'Enable'. After some
    pagetemplates are viewed, you will see a list of paths to each of those
    pagetemplates (or, in the rare case the path isn't known, the id). When you
    click one of the items, you will see a list of all the expression calls in
    the template, ordered by total time spent on that expression.

License
  
    PTProfiler is released under the BSD license. See 'LICENSE.txt'.
