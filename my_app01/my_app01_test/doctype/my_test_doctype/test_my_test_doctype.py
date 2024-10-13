# Copyright (c) 2024, Anamika Nepomuceno and Contributors
# See license.txt

# import frappe
from frappe.tests import IntegrationTestCase, UnitTestCase


# On IntegrationTestCase, the doctype test records and all
# link-field test record depdendencies are recursively loaded
# Use these module variables to add/remove to/from that list
EXTRA_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]
IGNORE_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]


class TestMyTestDoctype(UnitTestCase):
	"""
	Unit tests for MyTestDoctype.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestMyTestDoctype(IntegrationTestCase):
	"""
	Integration tests for MyTestDoctype.
	Use this class for testing interactions between multiple components.
	"""

	pass
