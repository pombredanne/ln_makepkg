
"""
This module parses a pom XML file in search project variables which
can later be accessed through the Project class members
"""

import lxml.etree as et


class Project:

    dependencies = list()
    name = str()
    version = str()
    description = ""
    url = ""

    def __init__(self, pom_path):

        ns = {"pom": "http://maven.apache.org/POM/4.0.0"}
        tree = et.parse(open(pom_path))

        name_path = '/pom:project/pom:name/text()'
        version_path = '/pom:project/pom:version/text()'
        dependencies_path = ('/pom:project/pom:dependencies/pom:dependency/'
                             'pom:artifactId/text()')
        description_path = '/pom:project/pom:description/text()'
        homepage_path = '/pom:project/pom:url/text()'

        self.name = tree.xpath(name_path, namespaces=ns)[0]
        self.version = tree.xpath(version_path, namespaces=ns)[0]

        dependencies = tree.xpath(dependencies_path, namespaces=ns)
        if dependencies:
            self.dependencies = dependencies

        description = tree.xpath(description_path, namespaces=ns)
        if description:
            self.description = description[0]

        url = tree.xpath(homepage_path, namespaces=ns)
        if url:
            self.url = url[0]
