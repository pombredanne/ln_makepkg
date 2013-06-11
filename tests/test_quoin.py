from filetest import TestTemplates


class TestQuoin(TestTemplates):

    __test__ = True
    _pom_file = 'pom1.xml'
    _expected_source_name = 'quoin-clojure'
    _expected_package_name = 'libquoin-clojure'
    _expected_version = '0.1.0-1'
