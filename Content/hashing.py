from passlib.context import CryptContext
pswd_Context=CryptContext(schemes=['bcrypt'],deprecated='auto')

class Hash():
    def bcrypt(password:str):
        return pswd_Context.hash(password)
    
    def verify(hashed_password,plain_password):
        return pswd_Context.verify(plain_password,hashed_password)