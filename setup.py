try:
    from setuptools import setup, find_packages
except:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    version='0.1',
    license='BSD',
    name='zs.rstaddons',
    description='A small collection of ReST-addons',
    author='Horst Gutmann',
    author_email='zerok@zerokspot.com',
    package_dir={'':'src'},
    packages=find_packages('src'),
    namespace_packages=['zs'],
    install_requires=[
        'docutils>=0.5',
        ]
)
