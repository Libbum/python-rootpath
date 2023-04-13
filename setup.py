
# =========================================
#       IMPORTS
# --------------------------------------

import os
import setuptools
#import setupextras

# DISABLED/BUG: this line fails when `pip install palmtree` but works `pip install .`
# from palmtree import __version__

# =========================================
#       MAIN
# --------------------------------------

name = 'rootpath'
version = '0.1.1'
description = 'Python project/package root path detection.'
keywords = [
    'python',
    'utlity',
    'common',
    'root',
    'rootpath',
    'root-path',
    'detect',
    'autodetect',
    'auto-detect',
    'project-root',
    'project-root-path',
    'package-root',
    'package-root-path',
]

packages = setuptools.find_packages()
#data_files = setupextras.get_data_files(['*.*'], os.path.join(name, 'tests', '__fixtures__'))
#requirements = setupextras.get_requirements()
#readme = setupextras.get_readme()

config = {
    'name': name,
    'version': version,
    'description': (description),
    'keywords': keywords,
    'author': 'Jonas Grimfelt',
    'author_email': 'grimen@gmail.com',
    'url': 'https://github.com/grimen/python-{name}'.format(name = name),
    'download_url': 'https://github.com/grimen/python-{name}'.format(name = name),
    'project_urls': {
        'repository': 'https://github.com/grimen/python-{name}'.format(name = name),
        'bugs': 'https://github.com/grimen/python-{name}/issues'.format(name = name),
    },
    'license': 'MIT',

    'long_description': '',
    'long_description_content_type': 'text/markdown',

    'classifiers': [
        'Topic :: Software Development :: Libraries',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    'packages': packages,
    'package_dir': {
        name: name,
    },
    'package_data': {
        '': [
            'MIT-LICENSE',
            'README.md',
        ],
        name: [
            '*.*',
        ],
    },
    'include_package_data': True,
    'zip_safe': True,

    'install_requires': [
'six >= 1.11.0',
'coloredlogs >= 10.0',
'termcolor >= 1.1.0',
'colour-runner >= 0.0.5',
'deepdiff >= 3.3.0',
'pygments >= 2.2.0',
'tox >= 3.0.0',
'coverage >= 4.5.2',
    ],
    'setup_requires': [
        'setuptools_git >= 1.2',
    ],
}

setuptools.setup(**config)
