from passlib.hash import sha256_crypt

def encrypt(password):
    password_encrypted = sha256_crypt.hash(password)
    return password_encrypted

def decrypt(password,hash):
    password_decrypted = sha256_crypt.verify(password,hash)
    return password_decrypted

# gib me credits 0xar1.github.io