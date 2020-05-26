from setuptools import setup


def read(fname):
    import os
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='sklearn-fracdiff',
      version='0.1.1',
      description='sklearn wrapper for numpy-fracdiff',
      long_description=read('README.md'),
      long_description_content_type='text/markdown',
      url='http://github.com/ulf1/sklearn-fracdiff',
      author='Ulf Hamster',
      author_email='554c46@gmail.com',
      license='MIT',
      packages=['sklearn_fracdiff'],
      install_requires=[
          'setuptools>=40.0.0',
          'numpy>=1.18.*',
          'scikit-learn>=0.22.*',
          'numpy-fracdiff>=0.3.1'],
      python_requires='>=3.6',
      zip_safe=False)
