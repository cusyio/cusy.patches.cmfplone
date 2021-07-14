# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
)
from plone.testing import z2

import cusy.patches.cmfplone


class CusyPatchesCmfploneLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=cusy.patches.cmfplone)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'cusy.patches.cmfplone:default')


CUSY_PATCHES_CMFPLONE_FIXTURE = CusyPatchesCmfploneLayer()


CUSY_PATCHES_CMFPLONE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(CUSY_PATCHES_CMFPLONE_FIXTURE,),
    name='CusyPatchesCmfploneLayer:IntegrationTesting',
)


CUSY_PATCHES_CMFPLONE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(CUSY_PATCHES_CMFPLONE_FIXTURE,),
    name='CusyPatchesCmfploneLayer:FunctionalTesting',
)


CUSY_PATCHES_CMFPLONE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        CUSY_PATCHES_CMFPLONE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='CusyPatchesCmfploneLayer:AcceptanceTesting',
)
