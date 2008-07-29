################################################################################
# Ganga Project. http://cern.ch/ganga
#
# $Id: PACKAGE.py,v 1.2 2008-07-29 09:51:14 bsamset Exp $
################################################################################

""" Refer to Ganga/PACKAGE.py for details on the purpose of this module.
"""

_external_packages = {
    'nordugrid-arc-standalone' : {'version' : '0.6.3', 'PYTHONPATH':'lib/python2.2/site-packages', 'LD_LIBRARY_PATH':'lib', 'PATH' : 'bin', 'ARC_LOCATION' : '', 'GLOBUS_LOCATION' : ''}
    }

import os
import Ganga.Utility.Setup
from Ganga.Utility.Setup import PackageSetup
from Ganga.Utility.Config import getConfig

setup = PackageSetup(_external_packages)

def standardSetup(setup=setup):
    for p in setup.packages:
        #setup.prependPath(p,'PYTHONPATH')
        #setup.prependPath(p,'LD_LIBRARY_PATH')
        #setup.prependPath(p,'PATH')
        setup.prependPath(p,'ARC_LOCATION')
        if not os.environ.has_key('GLOBUS_LOCATION'):
            setup.prependPath(p,'GLOBUS_LOCATION')

