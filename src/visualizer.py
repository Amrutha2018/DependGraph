import subprocess

def get_installed_packages():
    """List all installed packages with their versions."""
    result = subprocess.run(["pip", "list", "--format=freeze"], capture_output=True, text=True)
    installed_packages = {}
    for line in result.stdout.splitlines():
        package, version = line.split('==')
        installed_packages[package.lower()] = version
    return installed_packages

def get_primary_packages():
    """List packages that are not required by any other packages (user-installed)."""
    result = subprocess.run(["pip", "list", "--not-required", "--format=freeze"], capture_output=True, text=True)
    primary_packages = {}
    for line in result.stdout.splitlines():
        package, version = line.split('==')
        primary_packages[package.lower()] = version
    return primary_packages

def get_package_dependencies(package_name):
    """Get dependencies of a given package using pip show."""
    result = subprocess.run(["pip", "show", package_name], capture_output=True, text=True)
    dependencies = []
    for line in result.stdout.splitlines():
        if line.startswith("Requires:"):
            dependencies = line.split(":", 1)[1].strip().split(", ")
            dependencies = [dep.lower() for dep in dependencies if dep]
            break
    return dependencies

def get_dependency_version_ranges(package_name):
    """Get version ranges required by the package."""
    result = subprocess.run(["pip", "show", package_name], capture_output=True, text=True)
    version_ranges = {}
    for line in result.stdout.splitlines():
        if line.startswith("Requires-Dist:"):
            parts = line.split(" ")
            dep_name = parts[1].lower()
            dep_version = parts[2] if len(parts) > 2 else "Any"
            version_ranges[dep_name] = dep_version
    return version_ranges

def build_dependency_tree(package_name, installed_packages, depth=0):
    """Recursively build and display the dependency tree."""
    indent = "    " * depth
    installed_version = installed_packages.get(package_name)
    print(f"{indent}└── {package_name}=={installed_version}")

    dependencies = get_package_dependencies(package_name)
    version_ranges = get_dependency_version_ranges(package_name)

    for dep in dependencies:
        installed_ver = installed_packages.get(dep, "Not Installed")
        version_range = version_ranges.get(dep, "Any")
        print(f"{indent}    ├── {dep} (required: {version_range}, installed: {installed_ver})")
        build_dependency_tree(dep, installed_packages, depth + 2)

def main():
    installed_packages = get_installed_packages()
    primary_packages = get_primary_packages()

    print("Dependency Tree:")
    for pkg, ver in primary_packages.items():
        build_dependency_tree(pkg, installed_packages)

if __name__ == "__main__":
    main()
