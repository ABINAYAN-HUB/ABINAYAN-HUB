def vigenere_decrypt(ciphertext, shifts):
    plaintext = ""
    shift_index = 0
    
    for char in ciphertext:
        if char.isalpha():
            
            shift = shifts[shift_index % len(shifts)]
            print(f"Decrypting '{char}' with shift {shift}")  
            
            
            if char.isupper():
                decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            
            print(f"Decrypted character: {decrypted_char}")  
            
            plaintext += decrypted_char
            shift_index += 1
        else:
            
            plaintext += char
    
    return plaintext


correct_shifts = [2, 14, 12, 15, 11, 4, 8, 19, 24, 2, 14, 12, 15, 11, 23, 8, 19, 24, 2, 14, 12, 15, 11, 4, 23]


encrypted_message = "Qpvtnx-Wkggbfto Mzhetoybtrd"
decrypted_message = vigenere_decrypt(encrypted_message, correct_shifts)
print(f"Encrypted: {encrypted_message}")
print(f"Decrypted: {decrypted_message}")