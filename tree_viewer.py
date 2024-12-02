import os
import argparse

def print_tree(directory, exclude_dir=None, dirs_only=False, indent=""):
    """
    Recursively prints the directory tree structure.
    :param directory: Root directory to start the tree from.
    :param exclude_dir: Directory to exclude (only top-level contents).
    :param dirs_only: Whether to display only directories.
    :param indent: Current indentation for nested directories.
    """
    try:
        entries = sorted(os.listdir(directory))
    except PermissionError:
        print(f"{indent}|-- [Permission Denied]")
        return

    for entry in entries:
        full_path = os.path.join(directory, entry)
        is_dir = os.path.isdir(full_path)

        # Skip excluded directory contents
        if exclude_dir and entry == exclude_dir:
            print(f"{indent}|-- {entry}")
            continue

        # Show only directories if dirs_only is True
        if dirs_only and not is_dir:
            continue

        print(f"{indent}|-- {entry}")

        # Recursively process subdirectories
        if is_dir:
            if exclude_dir and entry == exclude_dir:
                continue  # Skip contents of the excluded directory
            print_tree(full_path, exclude_dir, dirs_only, indent + "    ")

def main():
    parser = argparse.ArgumentParser(description="Display directory structure.")
    parser.add_argument(
        "directory",
        nargs="?",  # Make this argument optional
        default=".",  # Default to the current directory
        help="The root directory to display (default: current directory)."
    )
    parser.add_argument(
        "--exclude", 
        help="Exclude all contents below this directory (default: 'node_modules').",
        default="node_modules"
    )
    parser.add_argument("--dirs-only", help="Show only directories, exclude files.", action="store_true")

    args = parser.parse_args()

    root_dir = args.directory
    exclude_dir = args.exclude
    dirs_only = args.dirs_only

    if not os.path.exists(root_dir):
        print(f"Error: Directory '{root_dir}' does not exist.")
        return

    print(f"Directory structure for: {root_dir}\n")
    print_tree(root_dir, exclude_dir, dirs_only)

if __name__ == "__main__":
    main()
