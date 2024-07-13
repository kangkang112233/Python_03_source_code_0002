# `shutil.copytree` を使用してディレクトリをコピーする: `shutil` モジュールの `copytree` 関数は、
# 指定されたソースディレクトリとその中身（サブディレクトリとファイルすべて）を新しい場所にコピーするために使用されます。
# 例えば、`shutil.copytree(src, dst)` は `src` ディレクトリを `dst` ディレクトリに完全にコピーします。
#
# Copying Directory with `shutil.copytree`: The `copytree` function in the `shutil` module
# is used to copy a specified source directory and all its contents (subdirectories and files)
# to a new location. For example, `shutil.copytree(src, dst)` completely copies the `src` directory
# to the `dst` directory.

import shutil
import os

# Example: Book Management System - Copy book data directory

# Define source and destination directories
src_dir = "book_data"
dst_dir = "backup/book_data_backup"

# Ensure the destination directory exists
os.makedirs("backup", exist_ok=True)

# Copy the entire source directory to the destination
shutil.copytree(src_dir, dst_dir)

print(f"Directory '{src_dir}' copied to '{dst_dir}'")

# Code Explanation:
# This example assumes that there is a directory named 'book_data' containing subdirectories and files.
# The `shutil.copytree` function is used to copy 'book_data' to 'backup/book_data_backup'.
# The `os.makedirs` function ensures that the 'backup' directory exists before copying.
