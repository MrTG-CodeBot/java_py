# Java File Runner

This project provides a Python script to compile and execute Java source code files (.java) from a specified folder.

## Installation

No installation is required. You can run the script directly from your Python environment.

## Usage

1.  Make sure you have Python 3 installed.
2.  Clone or download this repository.
3.  Open a terminal or command prompt and navigate to the project directory.
4.  Run the script with `python javac_run.py`.
5.  Follow the interactive prompts:
    - Create or Edit folder file (Option 1): This allows you to set the folder path where your Java programs reside. You can either create a new file named `folderpath.txt` or edit an existing one.
    - Run Java code (Option 2): Enter the filename of the Java program you want to compile and execute, including the `.java` extension.

## Example Usage

Let's assume you have a Java program named `HelloWorld.java` in a folder named `java_programs`. Follow these steps:

1.  Run the script `python java_runner.py`.
2.  If the `folderpath.txt` doesn't exist, you'll be prompted to enter the folder path. In this case, enter `java_programs`.
3.  When prompted for the filename, enter `HelloWorld.java`.

The script will compile and run your Java program.

## License

This code is distributed under the MIT License (see LICENSE.txt for details).
