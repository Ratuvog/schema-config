from setuptools import setup, find_packages

setup(
    name='schema_config',
    version='0.0.1',
    author='Mikhail Kazakov',
    author_email='m.kazakov@ylab.io',
    description='A small example package',
    url='',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        "PyStaticConfiguration>=0.10,<1.0",
        "python-dotenv>=0.10,<1.0"
        "PyYAML>=5.1,<6.0"
    ],
)
