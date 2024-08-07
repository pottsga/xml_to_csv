from setuptools import setup, find_packages

setup(
    name='xml_to_csv',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'setuptools',
        'pandas',
        'rich',
        'lxml'
    ],
    entry_points={
        'console_scripts': [
            'xml_to_csv=xml_to_csv.convert:main',
        ],
    },
    author='Greg Potts',
    author_email='pottsga@gmail.com',
    description='A simple XML to CSV converter',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/pottsga/xml_to_csv',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
