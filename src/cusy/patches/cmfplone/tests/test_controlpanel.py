# -*- coding: utf-8 -*-
"""Test the controlpanel patches."""
from cusy.patches.cmfplone.testing import INTEGRATION_TESTING  # noqa: E501,
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import plone.api
import unittest


class TestControlpanelPatch(unittest.TestCase):
    """Test that Products.CMFPlone.PloneControlPanel.PloneControlPanel is patched."""

    layer = INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        self.controlpanel = plone.api.portal.get_tool("portal_controlpanel")
        # Log in with manager role to see control panels.
        setRoles(self.portal, TEST_USER_ID, ["Manager"])

    def test_patch_applied(self):
        """Validate that the patch is applied."""
        self.assertIsNotNone(
            getattr(
                self.controlpanel, "_old_cusy_patches_cmfplone_enumConfiglets", None
            )
        )

    def test_before_patch(self):
        """Validate that we can’t use the Plone expressions before the patch."""
        self.controlpanel.registerConfiglet(
            id="test_id",
            name="Site settings",
            action="string:${plone_portal_state/navigation_root_url}/@@site-controlpanel",
            permission="Manage portal",
            category="Plone",
            visible=True,
            appId="test_id",
            icon_expr="string:${portal_url}/product_icon.png",
        )
        with self.assertRaises(KeyError) as ctx:
            configlets = self.controlpanel._old_cusy_patches_cmfplone_enumConfiglets(
                group="Plone"
            )
            configlet = [item for item in configlets if item["id"] == "test_id"][0]
            # Getting the url will raise the KeyError
            configlet["url"]
        self.assertEqual("'plone_portal_state'", str(ctx.exception))

    def test_extended_expressions(self):
        """Validate that we can use the Plone expressions."""
        self.controlpanel.registerConfiglet(
            id="test_id",
            name="Site settings",
            action="string:${plone_portal_state/navigation_root_url}/@@site-controlpanel",
            permission="Manage portal",
            category="Plone",
            visible=True,
            appId="test_id",
            icon_expr="string:${portal_url}/product_icon.png",
        )
        configlets = self.controlpanel.enumConfiglets(group="Plone")
        self.assertGreaterEqual(len(configlets), 1)
        configlet = [item for item in configlets if item["id"] == "test_id"][0]
        self.assertIn("@@site-controlpanel", configlet["url"])
