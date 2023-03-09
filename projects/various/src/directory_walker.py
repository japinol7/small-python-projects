import os
from pathlib import Path


def directory_recursive_walk_exec_func(directory_path, func):
    try:
        sub_dirs = (f.path for f in os.scandir(directory_path) if f.is_dir())
    except Exception as e:
        print(f"ERROR: Cannot access directory {'-' * 15}")
        return

    for sub_dir in sub_dirs:
        os.chdir(sub_dir)
        func()
        directory_recursive_walk_exec_func(os.getcwd(), func)


def directory_one_level_walk_exec_func(directory_path, func):
    try:
        sub_dirs = (f.path for f in os.scandir(directory_path) if f.is_dir())
    except Exception as e:
        print(f"ERROR: Cannot access directory {'-' * 15}")
        return

    for sub_dir in sub_dirs:
        os.chdir(sub_dir)
        func()


def process_directory():
    dir_ = ''
    try:
        dir_ = os.getcwd()
        print(dir_)
    except Exception as e:
        print(f"ERROR: Error processing directory: {dir_}{'-' * 15} Msg: {e}")


def main():
    working_dir = os.path.join(str(Path.home()), 'Documents')

    print(f"All subdirectories recursively:\n")
    directory_recursive_walk_exec_func(working_dir, func=process_directory)

    print(f"\n{'-' * 15}\nAll immediate subdirectories:\n")
    directory_one_level_walk_exec_func(working_dir, func=process_directory)


if __name__ == '__main__':
    main()
