from filetest import TestTemplates


class TestSlingshot(TestTemplates):

    __test__ = True
    _pom_file = 'pom_slingshot.xml'
    _expected_source_name = 'slingshot-clojure'
    _expected_package_name = 'libslingshot-clojure'
    _expected_version = '0.10.3-1'
    _expected_itp_bug = '699546'
