 1.
   28 newPosition = position + cipherKey       // Original code
   28 newPosition = position + int(cipherKey)  //Corrected code
 2.
   25 uppercaseMessage = message               // Original code
   25 uppercaseMessage = message.upper()       //Corrected code
 3.
   38 return encryptMessage(message, cipherKey, alphabet)    // Original code
   38 return encryptMessage(message, decryptKey, alphabet)  //Corrected codecode  
 4.
   53 print(f'Decrypted Message: {myEncryptedMessage}')      // Original code
   53 print(f'Decrypted Message: {myDecryptedMessage}')     //Corrected code