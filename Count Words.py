# Toay I will write a program in which
#  the function will give us as output
#  the number of words in a sentence, like
#  it happens in Google Docs #

# def count_words(sentence):
#     word_list= sentence.split()
#     print(word_list)
#     return len(word_list)

# user_input=input("Enter your sentence: ")
# num_of_words= count_words(user_input)
# print(num_of_words)

# Now i am changing it so that it excludes punctuation marks and only count words ###
import string

def count_words(sentence):
    for p in string.punctuation:
        sentence = sentence.replace(p,"")
    word_list= sentence.split()
    print(word_list)
    return len(word_list)

user_input=input("Enter your sentence: ")
num_of_words= count_words(user_input)
print(num_of_words)