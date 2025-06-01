Task 1: Read a File and Handle Errors
-
Problem Statement: Write a Python program that:
1. Opens and reads a text file named sample.txt.
2. Prints its content line by line.
3. Handles errors gracefully if the file does not exist.

MY SOLUTION.
I have defined a function `read_file()` which takes a filename as an argument.
Then, I used a try-except block to attempt opening the file using the 'with open' statement.
If the file exists, it reads each line and prints it after stripping newline characters.
If the file doesn't exist, the program prints a user-friendly error message using the `FileNotFoundError` exception.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Task 2: Write and Append Data to a File
-
Problem Statement: Write a Python program that:
1. Takes user input and writes it to a file named output.txt.
2. Appends additional data to the same file.
3. Reads and displays the final content of the file.

MY SOLUTION.
I have defined a function `write_and_append_file()` which takes a filename as an argument.
First, it takes input from the user and writes it to the file (overwriting previous content).
Then, it again takes input from the user and appends it to the same file.
At last, it opens the file in read mode and prints the full content line by line to show the final output.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
