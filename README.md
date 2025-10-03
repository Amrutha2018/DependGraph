# DependGraph

A Dependency Visualizer is a command-line tool that analyzes the dependencies in a software project and generates a visual graph representing these dependencies. The graph helps developers understand the relationships between different modules, libraries, or packages in their project. This tool can be extremely useful for large projects with complex dependency trees, making it easier to identify potential issues like circular dependencies, outdated packages, or overly complicated structures.
```
Dependency Tree:
└── dependgraph==0.1.0
└── pip-tools==7.4.1
    ├── build (required: >=1.0,<2.0, installed: 1.2.1)
        └── build==1.2.1
            ├── packaging (required: >=21.0, installed: 24.1)
                └── packaging==24.1
            ├── pyproject-hooks (required: >=1.0.0, installed: 1.1.0)
                └── pyproject-hooks==1.1.0
    ├── click (required: >=7.1.2, installed: 8.1.7)
        └── click==8.1.7
    ├── pip (required: >=20.0, installed: 24.2)
        └── pip==24.2
    ├── pyproject-hooks (required: >=1.0.0, installed: 1.1.0)
        └── pyproject-hooks==1.1.0
    ├── setuptools (required: >=40.8.0, installed: 72.2.0)
        └── setuptools==72.2.0
    ├── wheel (required: >=0.36.2, installed: 0.44.0)
        └── wheel==0.44.0
└── requests==2.32.3
    ├── certifi (required: >=2021.5.30, installed: 2024.7.4)
        └── certifi==2024.7.4
    ├── charset-normalizer (required: >=2.0.0, installed: 3.3.2)
        └── charset-normalizer==3.3.2
    ├── idna (required: >=2.5, installed: 3.7)
        └── idna==3.7
    ├── urllib3 (required: >=1.26.5, installed: 2.2.2)
        └── urllib3==2.2.2
```
