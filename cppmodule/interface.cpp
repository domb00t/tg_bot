#include <iostream>
#include <string>
#include "encrypt.h"

class Inter
{
private:
    char *p_mes = nullptr;

public:
    Inter() = default;
    Inter(const std ::string &str) : p_mes(new char[str.size() + 1])
    {
        memcpy(p_mes, str.c_str(), str.size() + 1);
    }
    char *getPointer()
    {
        return p_mes;
    }
    ~Inter()
    {
        delete[] p_mes;
    }
};

extern "C"
{
    char *_encrypt(char *message, char *key);
    char *_decrypt(char *message, char *key);
}

char *_encrypt(char *message, char *key)
{
    std ::string _message(message), _key(key), _res;
    _res = encrypt(_message, _key);
    Inter I_res(_res);
    return I_res.getPointer();
}

char *_decrypt(char *message, char *key)
{
    std ::string _message(message), _key(key), _res;
    _res = decrypt(_message, _key);
    Inter I_res(_res);
    return I_res.getPointer();
}


