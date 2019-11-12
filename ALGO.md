LOCAL_RSA_KEY_PAIR = generated at init run time of the program<br>
GLOBAL_RSA_PUBLIC_KEY = the public key of the server, hard coded into the program

### Encrypt a file

1. Generate an AES key
2. Encrypt file's content
3. Encrypt AES key using public key of the LOCAL_RSA_KEY_PAIR
4. Append the encrypted AES key to the beginning of the encypted file

### Algo

1. Search for files
2. Encrypt each file
3. Encrypt the private key of the LOCAL_RSA_KEY_PAIR using the GLOBAL_RSA_PUBLIC_KEY
4. Write the encrypted private key of the LOCAL_RSA_KEY_PAIR to a file
5. Create a README.txt

### Decrypt a file

1. Get the encrypted AES key from the beginning of the file
2. Decrypt the AES key using the decrypted RSA private key of the locally generated RSA key pair
3. Use the decrypted AES key to decrypt the contents of the file
4. Save the decrypted contents of the encrypted file into a new file
5. Delete the encrypted file
