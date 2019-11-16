from setuptools import setup

setup(
    name='sysfinger', # Needed to silence warnings (and to be a worthwhile package)
    url='https://github.com/psytron/sysfinger',
    author='Mico Malecki',
    author_email='m@psytron.com',
    packages=['os'], # Needed to actually package
    install_requires=['pyyaml'],# Needed for dependencies
    version='0.22',
    license='PSYTRON', # Can be anything
    description='Sysfinger print.'
    # long_description=open('README.txt').read(), # Readme eventually (there will be a warning)
)