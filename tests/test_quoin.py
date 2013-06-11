from filetest import TestTemplates


class TestQuoin(TestTemplates):

    __test__ = True
    _pom_file = 'pom1.xml'
    _expected_source_name = 'quoin-clojure'
