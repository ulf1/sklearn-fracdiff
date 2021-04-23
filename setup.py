from setuptools import setup
import pypandoc


def get_version(path):
    with open(path, "r") as fp:
        lines = fp.read()
    for line in lines.split("\n"):
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")


setup(name='sklearn-fracdiff',
      version=get_version("sklearn_fracdiff/__init__.py"),
      description='sklearn wrapper for numpy-fracdiff',
      long_description=pypandoc.convert('README.md', 'rst'),
      url='http://github.com/ulf1/sklearn-fracdiff',
      author='Ulf Hamster',
      author_email='554c46@gmail.com',
      license='Apache License 2.0',
      packages=['sklearn_fracdiff'],
      install_requires=[
          'numpy>=1.18.*',
          'six>=1.13.*',
          'scikit-learn>=0.22.*',
          'numpy-fracdiff>=0.3.1'],
      python_requires='>=3.6',
      zip_safe=False)
