import string
if __name__ == '__main__':
  letters = list(string.ascii_lowercase)
  letter_to_num = dict()
  num_to_letter = dict()
  for i in range(26):
    letter_to_num[letters[i]] = i+1
    num_to_letter[i+1] = letters[i]

  encrypted_text = 'ynkooejcpdanqxeykjrbdofgkq'
  decrypted_text = ''
  for i in range(25):
    for letter in encrypted_text:
      decrypted_text += num_to_letter[(letter_to_num[letter] + i) % 26 + 1]
    
    print(decrypted_text)
    decrypted_text = ''
    

  
