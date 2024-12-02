import os
import argparse

def print_tree(directory, exclude_dirs=None, dirs_only=False, indent=""):
    """
    Recursively prints the directory tree structure.
    :param directory: Root directory to start the tree from.
    :param exclude_dirs: List of directories to exclude.
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

        # Skip excluded directories
        if exclude_dirs and entry in exclude_dirs:
            print(f"{indent}|-- {entry} [Excluded]")
            continue

        # Show only directories if dirs_only is True
        if dirs_only and not is_dir:
            continue

        print(f"{indent}|-- {entry}")

        # Recursively process subdirectories
        if is_dir:
            print_tree(full_path, exclude_dirs, dirs_only, indent + "    ")

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
        nargs="+",
        help="Exclude all contents below these directories (default: ['node_modules', '.git']).",
        default=["node_modules", ".git"]
    )
    parser.add_argument("--dirs-only", help="Show only directories, exclude files.", action="store_true")

    args = parser.parse_args()

    root_dir = args.directory
    exclude_dirs = args.exclude
    dirs_only = args.dirs_only

    if not os.path.exists(root_dir):
        print(f"Error: Directory '{root_dir}' does not exist.")
        return

    print(f"Directory structure for: {root_dir}\n")
    print_tree(root_dir, exclude_dirs, dirs_only)

if __name__ == "__main__":
    main()