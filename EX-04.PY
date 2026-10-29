#Check if a word given by the user is a palindrome or not. Example of a palindromes: "kayak", "level", "was it a car or a cat i saw".



word=input('enter a word:')
reverse = ''
for letter in word :
    reverse = letter +reverse 
if word== reverse :
        print ('its a palidrome')
else:
        
        print('its not a palidrom ')