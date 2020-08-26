#Write a program that turns a sentence into camel case. The first word is lowercase, 
# the rest of the words have their initial letter capitalized, and all of the words are joined together. 
# For example, with the input "fOnt proCESSOR and ParsER", your program will output "fontProcessorAndParser". 

#Optional extra question: print a warning message if the input will not produce a valid variable name. 
# You don't need to be exhaustive in checking, but test for a few common issues, such as starting 
# with a number, or containing invalid characters such as # or + or ". 

#Test your program with different example inputs, and comment your code. 

def camelCase(str):
    # if input contains number 
    if str.isdigit():
        print('Invalid input - contains a number')
        return
    
    words = str.split()
    #print(words)
    result = '' + words[0].lower()
    for i in range(1, len(words)):
        result= result + words[i].title()
    
    #title case each word and combine with no spaces
    print(result)


#calling the function with various inputs
camelCase('my cats are acadia and zion')
camelCase('it is really hot today')
camelCase('1234')
