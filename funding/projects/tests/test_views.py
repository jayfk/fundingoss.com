# -*- coding: utf-8 -*-
from test_plus.test import TestCase
from .factories import ProjectFactory
from django.core.urlresolvers import reverse


class TestProjectListView(TestCase):

    def setUp(self):
        self.project_1 = ProjectFactory()
        self.project_2 = ProjectFactory()

    def test_context_data(self):
        resp = self.client.get(reverse("projects:list"))
        self.assertTrue("status_choices" in resp.context_data)
        self.assertTrue("projects" in resp.context_data)
        self.assertTrue(self.project_1 in resp.context_data.get("projects", []))
        self.assertTrue(self.project_2 in resp.context_data.get("projects", []))


class TestProjectCreateView(TestCase):

    def test_form_valid(self):
        data = {
            "name": "foo",
            "website": "http://bar.com",
            "added": "baz",
            "languages": "fii",
            "maintainers": "bar",
            "license": "unknown",
            "funding_status": "unknown",
        }
        resp = self.client.post(reverse("projects:create"), data=data, follow=True)
        self.assertRedirects(resp, reverse("projects:list"))


class TestProjectDetailView(TestCase):

    def setUp(self):
        self.project = ProjectFactory()

    def test_template(self):
        resp = self.client.get(reverse("projects:detail", kwargs={"pk": self.project.pk}))
        self.assertContains(resp, "disqus_thread")

class TestProjectJSONView(TestCase):

    def setUp(self):
        self.project_1 = ProjectFactory()

    def test_json_data(self):
        resp = self.client.get(reverse("projects:json"))
        self.assertTrue("projects" in resp.json())
        self.assertTrue(self.project_1.name in [p["name"] for p in resp.json().get("projects")])
