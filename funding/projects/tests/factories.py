import factory


class ProjectFactory(factory.django.DjangoModelFactory):

    name = factory.sequence(lambda n: 'project-{0}'.format(n))
    website = factory.sequence(lambda n: 'http://project-{0}.com'.format(n))
    added = factory.sequence(lambda n: '@user-{0}'.format(n))
    languages = ["python", ]
    maintainers = factory.sequence(lambda n: ["@user-{0}".format(n), ])

    class Meta:

        model = "projects.Project"
        django_get_or_create = ("name", )
