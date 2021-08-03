# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


import os.path

readme = ''
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, 'README.rst')
if os.path.exists(readme_path):
    with open(readme_path, 'rb') as stream:
        readme = stream.read().decode('utf8')


setup(
    long_description=readme,
    name='pyserialem',
    version='0.3.2',
    description='Python module to read/write SerialEM .nav files.',
    python_requires='>=3.6.1',
    project_urls={
        'documentation': 'http://github.com/instamatic-dev/pyserialem',
        'homepage': 'http://github.com/instamatic-dev/pyserialem',
        'repository': 'http://github.com/instamatic-dev/pyserialem'},
    author='Stef Smeets',
    author_email='s.smeets@esciencecenter.nl',
    license='BSD-3-clause',
    keywords='serialem electron-microscopy navigator',
    classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Topic :: Software Development :: Libraries',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9'],
    packages=['pyserialem'],
    package_dir={
        '': '.'},
    package_data={},
    install_requires=[
        'lmfit>=1.0.1',
        'matplotlib>=3.1.2',
        'mrcfile>=1.1.2',
        'numpy>=1.17.3',
        'scikit-image>=0.17.2',
        'scipy>=1.5.0',
        'tqdm>=4.46.1'],
    extras_require={
        'dev': [
            'check-manifest',
            'pre-commit',
            'pytest==5.*,>=5.4.1',
            'pytest-cov==2.*,>=2.8.1']},
)
