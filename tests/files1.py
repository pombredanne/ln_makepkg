from subprocess import call
import os
import shutil


#Define what pom file belongs to this test.
pom_file = 'pom1.xml'

test_dir = os.path.abspath(os.path.dirname(__file__))
temp_dir = test_dir + '/temp'


def setup_module():
    #Create a temporary folder where we can work in
    if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)

    #Copy our pom file to the temporary directory
    pom_src = test_dir + '/resources/' + pom_file
    pom_dst = temp_dir + '/pom.xml'
    shutil.copy(pom_src, pom_dst)

    os.chdir(temp_dir)

    call('python ' + test_dir + '/../ln_makepkg', shell=True)

def teardown_module():
    os.chdir(test_dir)
    shutil.rmtree(test_dir)

def test_control_version():
    assert True
