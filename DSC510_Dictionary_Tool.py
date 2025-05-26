# Import libraries
import string

# This function is used to add words to the dictionary and count them
def add_word(word, g_dict):
    if word not in g_dict:
        g_dict[word] = 1
    else:
        g_dict[word] += 1

# This function is used to remove punctuation and split out the words
def process_line(line, g_dict):
    words = line.split()
    for word in words:
        if word != "--":
            word = word.strip()
            word = word.lower()
            word = word.strip(string.punctuation)
            add_word(word, g_dict)

# This function is used to format the text and print final message to new file
def process_file(g_dict, new_file_name):
    sort_g_dict = list()
    for key, val in list(g_dict.items()):
        sort_g_dict.append((val, key))
    sort_g_dict.sort(reverse=True)
    with open(new_file_name, 'a') as processed_file:
        processed_file.write("{:<15} {:<15}".format("Word", "Count")+"\n")
        processed_file.write("---------------------"+"\n")
        for key, val, in sort_g_dict:
            processed_file.write("{:<15} {:<15}".format(val, key)+"\n")

# This is the main method and calls on the other functions
def main():
    g_dict = dict()
    while True:
        file_name = input("Please input the file name you wish to process: ")
        try:
            original_file = open(file_name.lower())
        except FileNotFoundError as e:
            print(e)
        except Exception as e:
            print(e)
        else:
            new_file_name = input("Please input the file name you wish to create: ")
            with open(new_file_name, 'w') as new_file:
                for line in original_file:
                    process_line(line, g_dict)
                new_file.write("{} {}".format("Length of the dictionary: ", len(g_dict.values()))+"\n")
            process_file(g_dict, new_file_name)
            original_file.close()
            break
    print("Your new file '", new_file_name, "' has been created in this directory.")

if __name__ == "__main__":
    main()
