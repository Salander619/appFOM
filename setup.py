from setuptools import setup, find_packages

setup(
    name='appFOM',
    version='0.1.0',
    description='Common file of the application FOM',
    url='https://github.com/Salander619/FOM_app.git',
    author='Come Badet',
    author_email='come.badet@apc.in2p3.fr',
    license='',
    packages=find_packages('appFOM'),
    install_requires=['numpy',
                      'lisaconstants',
                      'matplotlib',
                      'scipy',
                      'lisaorbits',
                      'fastgb'],

    classifiers=[],
)
