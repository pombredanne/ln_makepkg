"""
A base class to group all common funcionality.
"""


from subprocess import call
import os
import re
import shutil


class TestTemplates():

    __test__ = False
    test_dir = None
    temp_dir = None
    control_file = None

    _pom_file = None
    _expected_source_name = None

    @classmethod
    def setup_class(cls):

        cls.test_dir = os.path.abspath(os.path.dirname(__file__))
        cls.temp_dir = cls.test_dir + '/temp'

        #Create a temporary folder where we can work in
        if not os.path.exists(cls.temp_dir):
                os.makedirs(cls.temp_dir)

        #Copy our pom file to the temporary directory
        pom_src = cls.test_dir + '/resources/' + cls._pom_file
        pom_dst = cls.temp_dir + '/pom.xml'
        shutil.copy(pom_src, pom_dst)

        os.chdir(cls.temp_dir)

        call('python ' + cls.test_dir + '/../ln_makepkg', shell=True)

        cls.control_file = open(cls.temp_dir + '/debian/control').read()

    @classmethod
    def teardown_class(cls):
        os.chdir(cls.test_dir)
        shutil.rmtree(cls.temp_dir)

    def test_control_source(self):
        source = re.match('Source: ([-a-zA-Z0-9./]+)',
                          self.control_file).group(1)
        assert source == self._expected_source_name
