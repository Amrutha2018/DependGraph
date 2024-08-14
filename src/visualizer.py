import sys
import os

def parse_requirements(file_path):
    dependencies = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith('#'):
                    dependencies.append(line)
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    return dependencies

if __name__ == "__main__":
    # Check if a file path was provided
    if len(sys.argv) < 2:
        print("Usage: python visualizer.py <path_to_requirements.txt>")
        sys.exit(1)

    file_path = sys.argv[1]

    # Check if the provided path exists and is a file
    if not os.path.isfile(file_path):
        print(f"The provided path {file_path} is not a valid file.")
        sys.exit(1)

    deps = parse_requirements(file_path)
    print("Extracted Dependencies:")
    for dep in deps:
        print(dep)
