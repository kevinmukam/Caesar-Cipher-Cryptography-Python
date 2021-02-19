#Network Security
#Caesar Encryption/Decryption Algorithm
#February 7, 2021



#Function for the encryption algorithm
def caesar_str_enc(enc_string, enc_shift):
  cipher = ""

  for letter in enc_string:
    if ord(letter) == 32:       #Verifying if the character is a space or not
      cipher = cipher + " "
    else:                       #If it's not a space, perform the Caesar algorithm
      temp = ord(letter) - 65   #Finding the ASCII code of the letter in the alphabet range 0-26
      update = (temp + enc_shift)%26  #Performing the Caesar algorithm with modulo 26 because the alphabet is wrapped around
      new_value = update + 65  #Returning to the normal ASCII grid with the updated value
      cipher = cipher + chr(new_value)  #Adding the new value to the string to form the output
  return cipher


#Function for the decryption algorithm
def caesar_str_dec(decr_string, decr_shift):
  original = ""

  for lett in decr_string:
    if ord(lett) == 32:
      original = original + " "
    else:
      temporary = ((ord(lett) - 65) - decr_shift)%26
      new = temporary + 65
      original = original + chr(new)
  return original


#Main code with testing
if __name__ == "__main__":
  mytest = "HAPPY"
  secondtest = "A TEST SENTENCE"

  """
  print ("The text is ", mytest)
  mytest_enc = caesar_str_enc(mytest, 3)
  print("The encrypted text is ", mytest_enc)
  mytest_orig = caesar_str_dec(mytest_enc, 3)
  print("The decrypted text is ", mytest_orig)"""


  print ("The text is ", secondtest)
  secondtest_enc = caesar_str_enc(secondtest, 2)
  print("The encrypted text is ", secondtest_enc)
  secondtest_orig = caesar_str_dec(secondtest_enc, 2)
  print("The decrypted text is ", secondtest_orig)
