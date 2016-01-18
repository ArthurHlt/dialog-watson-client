from setuptools import setup, find_packages
import os

setup(
    name='dialog-watson-client',
    version='1.0.2',
    packages=['dialog_watson_client', 'dialog_watson_client.exceptions'],
    url='https://github.com/HomeHabbit/dialog-watson-client',
    license='MIT',
    author='Arthur Halet',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    keywords='natural langage dialog robot watson IBM',
    classifiers=['Topic :: Software Development :: Libraries',
                 'License :: OSI Approved :: MIT License',
                 'Topic :: Communications'],
    platforms='ALL',
    install_requires=[
        'watson-developer-cloud>=0.3.3',
        'lxml>=3.5.0',
        'anyconfig',
        'bunch'
    ],
    extras_require={
        'XSD': ["lxml>=3.5.0"]
    },
    package_data={
        'dialog_watson_client': ['WatsonDialogDocument_1.0.xsd']
    },
    author_email='arthurh.halet@gmail.com',
    description='Client for dialog watson module',
    entry_points={
        'console_scripts': [
            'dialog-watson-client=dialog_watson_client.__main__:main',
        ],
    },
)
