import io
import sys

from setuptools import find_packages, setup

with io.open('calysto_hy/version.py', encoding="utf-8") as fid:
    for line in fid:
        if line.startswith('__version__'):
            __version__ = line.strip().split()[-1][1:-1]
            break

with open('README.md') as f:
    readme = f.read()

setup(name='calysto_hy',
      version=__version__,
      description='A Hy kernel for Jupyter based on MetaKernel',
      long_description=readme,
      author='Douglas Blank',
      author_email='doug.blank@gmail.com',
      url="https://github.com/Calysto/calysto_hy",
      install_requires=["metakernel", "hy", "toolz"],
      dependency_links=[
          "git+https://github.com/ekaschalk/jedhy.git"
      ],
      packages=find_packages(include=["calysto_hy", "calysto_hy.*"]),
      package_data={'calysto_hy': ["images/*.png", "modules/*.ss"]},
      classifiers=[
          'Framework :: IPython',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 2',
          'Programming Language :: Lisp',
          'Topic :: System :: Shells',
      ]
)
