"""
Created on Nov 30, 2014

@author: Aitor Gómez Goiri <aitor.gomez@deusto.es>

To install/reinstall/uninstall the project and its dependencies using pip:
     pip install ./
     pip install ./ --upgrade
     pip uninstall pyclientliblightsec
"""
from setuptools import setup  # , find_packages

setup(name="lightsecclient",
      version="0.1",
      description="Client library for HTTP servers following the lightsec protocol.",
      # long_description = "",
      author="Aitor Gomez-Goiri",
      author_email="aitor.gomez@deusto.es",
      maintainer="Aitor Gomez-Goiri",
      maintainer_email="aitor.gomez@deusto.es",
      url="https://github.com/lightsec/python-lightsecclient",
      #  license = "http://www.apache.org/licenses/LICENSE-2.0",
      platforms=["any"],
      package_dir={
          '': 'src',
      },
      packages=["lightsecclient"],
      install_requires=["liblightsec"],
)