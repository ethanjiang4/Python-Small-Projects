#!/bin/python3

#caesar cypher project
start = 'y'
select = ''
alphabet = 'abcdefghijklmnopqrstuvwxyz'

while start == 'y' or start == 'Y':
  print('Press 1 for encryption.')
  print('Press 2 for decryption.')
  print('Anything else will exit.')
  select = input('Enter your selection: ')
  
  if select == '1':
    key = int (input('Please enter your key: '))
    newMessage = ''

    message = input('Please enter a message: ')

    for character in message:
      if character in alphabet:
        pos = alphabet.find(character)
        newPos = (pos + key) % 26
        newChar = alphabet[newPos]
        newMessage += newChar
      else:
        newMessage += character
        
    print('Your coded message is', newMessage)
    start = input('Restart the program? (y/n): ')
    if start == 'y' or start == 'Y':
      continue
    
  if select == '2':
    oldMessage = ''
    message = input('Please enter a coded message: ')
    key = int (input('Please enter your key: '))
    for character in message:
      if character in alphabet:
        pos = alphabet.find(character)
        newPos = (pos - key) % 26
        newChar = alphabet[newPos]
        oldMessage += newChar
      else:
        oldMessage += character
        
    print('Your decoded message is', oldMessage)
    start = input('Restart the program? (y/n): ')
    if start == 'y' or start == 'Y':
      continue
    
  else: 
    break
print('Goodbye!')
