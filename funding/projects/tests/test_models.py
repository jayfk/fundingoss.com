# -*- coding: utf-8 -*-
from test_plus.test import TestCase
from .factories import ProjectFactory


class ProjectTestCase(TestCase):

    def test_displayable_funding_types(self):
        project = ProjectFactory(funding_type = ["corporate"])

        self.assertEqual(
            [ftype for ftype in project.displayable_funding_types()],
            ["Corporate"]
        )
