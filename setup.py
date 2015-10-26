from setuptools import setup, find_packages
import os

version = '1.4.1dev'

setup(name='Products.PTProfiler',
      version=version,
      description="PageTemplate profiler for Zope 2",
      long_description=open(os.path.join("Products", "PTProfiler", "README.txt")).read() + "\n" +
                       open(os.path.join("Products", "PTProfiler", "HISTORY.txt")).read(),
      classifiers=[
          "Framework :: Zope2",
          "License :: OSI Approved :: BSD License",
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      keywords='zope2 page template profiler',
      author='Guido Wesdorp and Infrae',
      author_email='info@infrae.com',
      url='https://github.com/infrae/Products.PTProfiler',
      license='BSD',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          ],
      extras_require=dict(
          test=[
              'plone.testing',
          ]),
      )
