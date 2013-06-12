from distutils.core import setup

setup(
    name='ln_makepkg',
    version='0.1',
    scripts=['ln_makepkg'],
    packages=['leinpkg'],
    platforms=['any'],
    description='Make debian packages from Leiningen projects',
    author="Eugenio Cano-Manuel Mendoza",
    author_email="eugeniocanom@gmail.com",
    url="https://github.com/keidesu/ln_makepkg",
    package_data = {
        'leinpkg': ['templates/*']
    },
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python",
        "Topic :: System :: Archiving :: Packaging",
        "Topic :: Utilities",
    ]
 )
