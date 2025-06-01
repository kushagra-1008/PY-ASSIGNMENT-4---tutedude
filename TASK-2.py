
def write_and_append_file(filename):
   
    user_input = input("Enter some data to write: ")
    with open(filename, 'w') as file:
        file.write(user_input + '\n')

    
    additional_input = input("Enter additional data to append: ")
    with open(filename, 'a') as file:
        file.write(additional_input + '\n')

    
    print("\nFinal content of the file:")
    with open(filename, 'r') as file:
        print(file.read())


write_and_append_file("output.txt")
