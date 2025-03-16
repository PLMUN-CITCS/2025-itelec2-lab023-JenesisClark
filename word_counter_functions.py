"""
Word Counter Program

This program defines two functions:
1. get_sentence_input() - Prompts the user for a sentence and returns it as a string.
2. count_words(sentence) - Counts the number of words in a given sentence.

The main program calls these functions to get a sentence from the user, 
count the number of words, and display the result in a user-friendly format.
"""

def get_sentence_input() -> str:
    """
    Prompts the user to enter a sentence and returns the input as a string.
    
    Returns:
        str: The sentence entered by the user.
    """
    sentence = input("Enter a sentence: ")
    return sentence

def count_words(sentence: str) -> int:
    """
    Counts the number of words in the given sentence.
    
    Args:
        sentence (str): The sentence whose words need to be counted.
    
    Returns:
        int: The number of words in the sentence.
    """
    words = sentence.split()  # Splitting the sentence by spaces into a list of words
    return len(words)  # The length of the list is the number of words

def main():
    """
    Main program that calls the get_sentence_input() and count_words() functions,
    and displays the word count to the user.
    """
    sentence = get_sentence_input()  # Get the sentence from the user
    word_count = count_words(sentence)  # Count the words in the sentence
    print(f"The sentence has {word_count} words.")  # Output the word count

# Calling the main function to execute the program
if __name__ == "__main__":
    main()
