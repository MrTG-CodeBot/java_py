"""
Copyright (c) 2024 MrTG-CodeBot

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import os
import subprocess

class JavaRunner:
  def __init__(self):
    self.folder_path = None
    self.folderpath_file = 'folderpath.txt'

  def check_folder(self):
    try:
      if os.path.exists(self.folderpath_file):
        with open(self.folderpath_file, 'r') as file:
          self.folder_path = file.read().strip()
      else:
        self.folder_path = input("Enter the folder path of the Java programs stored: ")

      if not os.path.exists(self.folder_path):
        print(f"{self.folder_path} is not found.")
        return False
      return True
    except Exception as e:
      print(f"An unexpected error occurred: {e}")
      return False

  def compile_and_execute(self, file_name):
    try:
      file_path = os.path.join(self.folder_path, file_name)
      if not os.path.exists(file_path):
        print(f"{file_path} is not found.")
        return

      os.chdir(self.folder_path)

      javac_command = ["javac", file_name]
      subprocess.run(javac_command, check=True)

      class_name, _ = os.path.splitext(os.path.basename(file_name))
      java_command = ["java", class_name]
      subprocess.run(java_command, check=True)

      print("\nCompilation and run successful.")
    except subprocess.CalledProcessError as e:
      print(f"Error during compilation or execution: {e}")

  def set_folder(self):
    fo_name = input("Enter the folder name that Java programs are stored: ")
    if os.path.exists(fo_name):
      with open(self.folderpath_file, 'w') as fname:
        fname.write(fo_name)
      self.folder_path = fo_name
      print("Successfully added")
    else:
      print("Folder not found")

  def run(self):
    while True:
      print("\n1. Create or Edit the folder file.")
      print("2. Run java code")
      print("3. Exit")
      ch = input("Enter the choice: ")
      if ch == "1":
        self.set_folder()
      elif ch == "2":
        if self.check_folder():
          file_name = input("Enter the file name with .java extension: ")
          self.compile_and_execute(file_name)
      elif ch == "3":
        break

if __name__ == "__main__":
  runner = JavaRunner()
  runner.run()
