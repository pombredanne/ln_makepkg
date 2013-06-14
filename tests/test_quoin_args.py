from filetest import TestTemplates


class TestQuoinArgs(TestTemplates):

    __test__ = True
    _pom_file = 'pom_quoin.xml'
    _expected_source_name = 'quoin-clojure'
    _expected_package_name = 'libquoin2-clojure'
    _commandline_args = '-p libquoin2-clojure -v 0.1.1'
    _expected_version = '0.1.1-1'
