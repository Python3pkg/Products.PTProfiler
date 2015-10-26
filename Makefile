PHONY: plone4.0 plone4.1 plone4.2 plone4.3 plone5.0

plone4.0:
	bin/pip install setuptools==0.6c11
	bin/python2.6 bootstrap.py --version
	bin/python2.6 bootstrap.py --setuptools-version=0.6c11 --buildout-version=1.4.4 -c plone40.cfg
	bin/buildout -vc plone40.cfg

plone4.1:
	bin/pip install setuptools==0.6c11
	bin/python2.6 bootstrap.py --version
	bin/python2.6 bootstrap.py --setuptools-version=0.6c11 --buildout-version=1.4.4 -c plone41.cfg
	bin/buildout -vc plone41.cfg

plone4.2:
	bin/pip install setuptools==0.6c11
	bin/python2.6 bootstrap.py --version
	bin/python2.6 bootstrap.py --setuptools-version=0.6c11 --buildout-version=1.7.1 -c plone42.cfg
	bin/buildout -vc plone42.cfg

plone4.3:
	bin/pip install setuptools==0.6c11
	bin/python2.7 bootstrap.py --version
	bin/python2.7 bootstrap.py --setuptools-version=0.6c11 --buildout-version=1.7.1 -c plone43.cfg
	bin/buildout -vc plone43.cfg

plone5.0:
	bin/python2.7 bootstrap.py --version
	bin/python2.7 bootstrap.py --setuptools-version=18.3.1 --buildout-version=2.4.3 -c plone50.cfg
	bin/buildout -vc plone50.cfg
