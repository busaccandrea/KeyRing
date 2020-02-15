import os, random, struct
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
 
 
def encrypt(key, folder, input_file):
    chunksize=16*4*1024
 
    output_filename = folder + input_file + '.aes'
    initial_vector = os.urandom(16) # urandom: best method :)
 
    encryptor = AES.new(key, AES.MODE_CBC, initial_vector)
    filesize = os.path.getsize(folder + input_file)
 
    with open(folder + input_file, 'rb') as in_file:
        with open(output_filename, 'wb') as out_file:
            out_file.write(struct.pack('<Q', filesize))
            out_file.write(initial_vector)

            # go block for block through the data
            while True:
                # read a block of data
                chunk = in_file.read(chunksize)
                # if chunk == 0, we are at the end
                if len(chunk) == 0:
                    break
                # else we need to fill the last block of bytes up to 16
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - len(chunk) % 16)
                # encrypt this block and append it to the file
                out_file.write(encryptor.encrypt(chunk))
    
    os.remove(folder + input_file)

def decrypt(key, folder, input_file):
    chunksize=16*4*1024
    # get rid of the .aes ending
    #output_filename = os.path.splitext(input_file)[0]
    output_filename = folder + input_file[:-4]
    with open(folder + input_file, 'rb') as in_file:
        # retrieve the original size of the encrypted data
        original_size = struct.unpack('<Q', in_file.read(struct.calcsize('Q')))[0]
        # retrieve the initialization vector
        initial_vector = in_file.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, initial_vector)
        with open(output_filename, 'wb') as out_file:
            while True:
                chunk = in_file.read(chunksize)
                if len(chunk) == 0:
                    break
                out_file.write(decryptor.decrypt(chunk))
            # restore original size
            out_file.truncate(original_size)
            
def hash(password):
    password = bytes(password, 'utf-8')
    hasher = SHA256.new(password)
    return hasher.digest()

def make_key_file(password):
    password = hash(password)
    with open("p/key.txt", 'wb') as key_file:
        key_file.write(password)
    encrypt(hash("13042008!£$%&/@#"), "p/", "key.txt")

def get_key():
    key = ""
    with open("p/key.txt", 'rb') as k:
        key = k.readline()
    return key

def password_gen(length):
    password = ""
    for i in range(0, length):
        c = random.randint(33, 125)
        password += chr(c)
    return password

def password_gen_old(length):
    while True:
        password = ""
        for i in range(0, length):
            c = random.randint(33, 125)
            password += chr(c)
        ans = input("This is your password.\n\n" + password + "\n\nIt's good enough? y/n")
        if ans == "y":
            break
    return password
