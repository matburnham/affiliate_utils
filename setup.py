from distutils.core import setup
import sys

#sys.path.append('affiliate_utils')
import affiliate_utils

setup(
    name='AffiliateUtils',
    version='0s.1dev',
    author='Mat Burnham',
    author_email='matburnham@gmail.com',
    # TODO: py_modules -> package_dir?
    #packages=['affiliate_utils',],
    url='***',
    download_url='***',
    description='Utility module to process affiliate URLs.',
    long_description=affiliate_utils.__doc__,
    #package_dir={'': 'affiliate_utils'},
    py_modules=['affiliate_utils'],
    provides=['affiliate_utils'],
    keywords='',
    license='Creative Commons Attribution-Noncommercial-ShareAlike 3.0 license',
    #long_description=open('README.txt').read(),
    install_requires=[],
)
