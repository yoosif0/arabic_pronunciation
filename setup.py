from os import path

from setuptools import setup

with open(path.join(path.dirname(__file__), 'README.md')) as readme_file:
    LONG_DESCRIPTION = readme_file.read()

setup(
    name='arabic_pronunciation',
    version=0.1,
    description='Pronounce Arabic words on the fly',
    long_description=LONG_DESCRIPTION,
    author='Youssef Sherif',
    author_email='sharief@aucegypt.edu',
    url='https://github.com/youssefsharief/arabic_pronunciation.git',
    include_package_data=True,
    zip_safe=False,
    license='GPL-3.0',
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6'
    )
)
