# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from atreal.trello.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of atreal.trello into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if atreal.trello is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('atreal.trello'))

    def test_uninstall(self):
        """Test if atreal.trello is cleanly uninstalled."""
        self.installer.uninstallProducts(['atreal.trello'])
        self.assertFalse(self.installer.isProductInstalled('atreal.trello'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that IAtrealTrelloLayer is registered."""
        from atreal.trello.interfaces import IAtrealTrelloLayer
        from plone.browserlayer import utils
        self.failUnless(IAtrealTrelloLayer in utils.registered_layers())
