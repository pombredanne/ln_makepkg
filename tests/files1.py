from leinpkg.tools import Project


project = None


def setup_module():
    project = Project('tests/resources/pom.xml')


def test_control_version():
    assert True
