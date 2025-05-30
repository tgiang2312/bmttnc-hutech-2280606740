class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt(self, text, key):
        encrypt_text = ''
        for col in range(key):
            pointer = col
            while pointer < len(text):
                encrypt_text += text[pointer]
                pointer += key
        return encrypt_text

    def decrypt(self, text, key):
        n = len(text)
        q = n // key
        r = n % key
        decrypted_text = [''] * key
        idx = 0
        for col in range(key):
            if col < r:
                column_length = q + 1
            else:
                column_length = q
            decrypted_text[col] = text[idx:idx + column_length]
            idx += column_length
        max_rows = max(len(col) for col in decrypted_text)
        result = ''
        for row in range(max_rows):
            for col in range(key):
                if row < len(decrypted_text[col]):
                    result += decrypted_text[col][row]
        return result