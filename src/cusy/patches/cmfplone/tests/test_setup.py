# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from cusy.patches.cmfplone.testing import INTEGRATION_TESTING  # noqa: E501,

import pkg_resources
import unittest


class TestSetup(unittest.TestCase):
    """Test that cusy.patches.cmfplone is properly installed."""

    layer = INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]

    def test_collective_monkypatcher_available(self):
        """Validate that `collective.monkeypatcher` is available."""
        self.assertTrue(pkg_resources.get_distribution("collective.monkeypatcher"))
