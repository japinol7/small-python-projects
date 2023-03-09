import os
from pathlib import Path


def directory_recursive_walk_exec_func(directory_path, func):
    try:
        sub_dirs = [f.path for f in os.scandir(directory_path) if f.is_dir()]
        for sub_dir in sub_dirs:
            os.chdir(sub_dir)
            func()
            directory_recursive_walk_exec_func(os.getcwd(), func)
    except Exception as e:
        print("-- Cannot access folder ___")


def directory_one_level_walk_exec_func(directory_path, func):
    try:
        sub_dirs = [f.path for f in os.scandir(directory_path) if f.is_dir()]
        for sub_dir in sub_dirs:
            os.chdir(sub_dir)
            func()
    except Exception as e:
        print("-- Cannot access folder ___")


def process_directory():
    print(os.getcwd())


def main():
    working_dir = os.path.join(str(Path.home()), 'Documents')

    print(f"All subdirectories recursively:\n")
    directory_recursive_walk_exec_func(working_dir, func=process_directory)

    print(f"\n{'-' * 15}\nAll immediate subdirectories:\n")
    directory_one_level_walk_exec_func(working_dir, func=process_directory)


if __name__ == '__main__':
    main()
