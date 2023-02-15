from setuptools import setup

setup(name='ipeadatapy',
      version='0.1.9',
      description='An API wrapper for Ipeadata',
      url='https://github.com/luanborelli/ipeadatapy',
      author='Luan Borelli',
      author_email='contato@luanborelli.net',
      license='MIT',
      packages=['ipeadatapy'],
      zip_safe=False,
      install_requires=['pandas', 'requests'])