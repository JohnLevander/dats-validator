import os
from unittest import TestCase

from dats import dats_model


class DatasetValidation(TestCase):

    def setUp(self):
        self.path = os.path.join(os.path.dirname(__file__), "../json-instances")

    def tearDown(self):
        pass

    def test_validate_dats_schemas(self):
        self.assertTrue(dats_model.validate_dats_schemas())

    def test_validate_dats_contexts(self):
        self.assertTrue(dats_model.validate_dats_contexts())

    def test_validate_dataset(self):
        self.assertTrue(dats_model.validate_dataset(self.path, "<your filename>", 0))

