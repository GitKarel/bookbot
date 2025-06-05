# Function to return the amount of words
def get_num_words(book_text):
    list_of_words = book_text.split()
    return len(list_of_words)

#function for counter how often each character appears
def get_usecount_characters(book_text):
    #Make lower capital to reduce duplicates
    lower_book_text = book_text.lower()
    #Create empty dictionary with "character":"value"
    character_count = {}

    #Loop through the lower case text and enlist the characters + count in the dictionary
    for character in lower_book_text:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    
    return character_count


def sort_on(dict):
    return dict["count"]

def sorted_character_count_list(character_list):
    new_order_list = []
    for key, value in character_list.items():
        new_order_list.append({"char": key, "count": value})

    new_order_list.sort(reverse=True, key=sort_on)
    #print(new_order_list)
    return new_order_list
   
        