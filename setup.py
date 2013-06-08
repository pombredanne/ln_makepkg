from distutils.core import setup

setup(
        name='ln_makepkg',
        version='0.1',
        scripts=['ln_makepkg'],
        packages=['leinpkg'],
        package_data = {
            'leinpkg': ['templates/*']
        }
     )
