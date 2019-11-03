import os

from setuptools import setup


def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths


def required(requirements_file):
    """ Read requirements file and remove comments and empty lines. """
    with open(os.path.join(os.path.dirname(__file__), requirements_file),
              'r') as f:
        requirements = f.read().splitlines()
        return [pkg for pkg in requirements
                if pkg.strip() and not pkg.startswith("#")]


#extra_files = package_files('lingua_franca')

with open("readme.md", "r") as fh:
    long_description = fh.read()

setup(
    name='corpus-file-gen',
    version='0.0.1',
    packages=['test', 'lingua_franca', 'lingua_franca.lang'],
    url='https://github.com/gras64/corpus-file-gen.git',
    license='Apache2.0',
    #package_data={'': extra_files},
    #include_package_data=True,
    install_requires=required('requirements.txt'),
    author='Gras64',
    author_email='gras64@web.de',
    description='Mycroft\'s A tool to generate corpus file for mimic-recording-studio (tacotron)',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Linguistic',
        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
