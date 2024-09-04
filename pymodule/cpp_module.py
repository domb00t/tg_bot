import ctypes

c_func = ctypes.CDLL("/home/user/tg_bot/cppmodule/cpp_module.so")

encrypt = c_func._encrypt
decrypt = c_func._decrypt

decrypt.argtypes = [ctypes.c_char_p,ctypes.c_char_p]
decrypt.restype = ctypes.POINTER(ctypes.c_char_p)

encrypt.argtypes = [ctypes.c_char_p,ctypes.c_char_p]
encrypt.restype = ctypes.POINTER(ctypes.c_char_p)

def _encrypt(message,key):
    b_message = message.encode('utf-8').strip()
    b_key = key.encode('utf-8').strip()
    cstr_pointer = encrypt(b_message,b_key)
    cstr = ctypes.c_char_p.from_buffer(cstr_pointer)
    return cstr.value.decode('utf-8').strip()
    

def _decrypt(message,key):
    b_message = message.encode('utf-8').strip()
    b_key = key.encode('utf-8').strip()
    cstr_pointer = decrypt(b_message,b_key)
    cstr = ctypes.c_char_p.from_buffer(cstr_pointer)
    return cstr.value.decode('utf-8').strip()
    

if __name__ == "__main__":
    x = int(input("Enter x: "))
    if x == 0:
        print("coder")
        imessage = input("Enter str: ")
        ikey = input("Enter key: ")
        res = _encrypt(imessage,ikey)
        print(res)
    elif x == 1:
        print("decoder")
        imessage = input("Enter str: ")
        ikey = input("Enter key: ")
        res = _decrypt(imessage,ikey)
        print(res)
    else:
        print("error")