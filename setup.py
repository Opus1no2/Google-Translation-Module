from setuptools import setup

setup(
    name="Google-Translation-Module",
    version=translate.__version__,
    url='https://github.com/Opus1no2/Google-Translation-Module',
    description='A Python client for interacting with Google Translation API',
    packages=['translate'],
    
    author=translate.__author__,
    author_email='tillotson.travis@gmail.com',
    
    license='MIT',
    install_requires=['request',],
)