try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = [
        'description': 'goTenna Mini Project',
        'author': 'Aaron Kim',
        'url': '',
        'download_url': '',
        'author_email': 'akim.tke@gmail.com',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': ['NAME'],
        'scripts': [],
        'name': 'akimminiproj'
]

setup(**config)
