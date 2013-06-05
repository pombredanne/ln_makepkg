import libxml2, re, sys
import lxml.etree as et
from subprocess import call

class Project:

    dependencies = list()
    name = str()
    version = str()
    description = ""
    url = ""

    def __init__(self, pom_path):
        ns = {"pom": "http://maven.apache.org/POM/4.0.0"}

        tree = et.parse(open(pom_path))
        self.name = tree.xpath('/pom:project/pom:name/text()', namespaces=ns)[0]
        self.version = tree.xpath('/pom:project/pom:version/text()', namespaces=ns)[0]

        dependencies = tree.xpath('/pom:project/pom:dependencies/pom:dependency/pom:artifactId/text()', namespaces=ns)
        if dependencies:
            self.dependencies = dependencies
        description = tree.xpath('/pom:project/pom:description/text()', namespaces=ns)
        if description:
            self.description = description[0]
        url = tree.xpath('/pom:project/pom:url/text()', namespaces=ns)
        if url:
            self.url = url[0]

