import os
import sys

dir_count = 0
file_count = 0


# TODO need to refactor the code.
def dir_tree(file_path, is_dir=None):
    global dir_count
    global file_count
    all_files_and_folder_with_path = [os.path.join(file_path, file) for file in os.listdir(file_path)]
    for files in all_files_and_folder_with_path:
        if os.path.isdir(files):
            dir_count += 1
            print(f'|-- {files.split("/")[-1]}(folder)/')
            dir_tree(files, True)
        elif is_dir and not files.split('/')[-1].startswith("."):
            file_count += 1
            print(f'|     |-- {files.split("/")[-1]} (file)')
        elif files.split('/')[-1].startswith("."):
            pass
        else:
            file_count += 1
            print(f'|-- {files.split("/")[-1]} (file)')


# print(f'{dir_count} directives and {file_count} file count is.')

if __name__ == '__main__':
    # dir_tree(sys.argv[1])
    dir_tree('/Users/jenildesai/Desktop/test')
    print(f'\n\n{dir_count} directives and {file_count} files.')