from setuptools import setup, find_packages

setup(
    name='dependgraph',
    version='0.1.0',
    description='A tool for visualizing and analyzing project dependencies',
    author='Amrutha E',
    author_email='amruthaje@gmail.com',
    url='https://github.com/Amrutha2018/DependGraph',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        # Add any dependencies here, e.g., 'requests', 'setuptools'
    ],
    entry_points={
        'console_scripts': [
            'dependgraph=visualizer:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
