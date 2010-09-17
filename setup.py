from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='Products.FileExchange',
      version=version,
      description="Provides a userfriendly view to exchange files between users",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='Plone File Exchange Upload',
      author='Raptus AG',
      author_email='dev@raptus.com',
      url='http://plone.org/products/fileexchange',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
