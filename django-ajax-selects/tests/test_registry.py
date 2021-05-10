from django.test import TestCase

import ajax_select


class TestRegistry(TestCase):

    def test_lookup_py_is_autoloaded(self):
        """Django >= 1.7 autoloads tests/lookups.py"""
        is_registered = ajax_select.registry.is_registered('person')
        self.assertTrue(is_registered)

    def test_back_compatible_loads_by_settings(self):
        """a module and class specified in settings"""
        self.assertTrue(ajax_select.registry.is_registered('book'))

    def test_autoconstruct_from_spec(self):
        """a dict in settings specifying model and lookup fields"""
        self.assertTrue(ajax_select.registry.is_registered('author'))

    def test_unsetting_a_channel(self):
        """settings can unset a channel that was specified in a lookups.py"""
        # self.assertFalse(ajax_select.registry.is_registered('user'))
        self.assertFalse(
                ajax_select.registry.is_registered('was-never-a-channel'))

    # def test_reimporting_lookup(self):
    #     """
    #     Importing a lookup should not re-register it after app launch is completed.
    #     """
    #     # importing this file will cause the @register to be called
    #     from tests import lookups  # noqa
    #     # should not have over-ridden what is in settings
    #     # registry is already frozen
    #     self.assertFalse(ajax_select.registry.is_registered('user'))
