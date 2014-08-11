from distutils.core import setup

setup(name='namamamonom',
      author='Thomas Levine',
      author_email='_@thomaslevine.com',
      description='Search for name columns in data tables.',
      url='https://github.com/tlevine/namamamonom',
      packages=['namamamonom'],
      install_requires = [
      ],
      scripts = [
          'bin/namamamonom',
      ],
      tests_require = ['nose'],
      version='0.0.1',
      license='AGPL',
      classifiers=[
          'Programming Language :: Python :: 3.4',
      ],
)
