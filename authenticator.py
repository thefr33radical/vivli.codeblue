import bcrypt

def get_hashed_password(plain_text_password):
  return bcrypt.hashpw(plain_text_password, bcrypt.gensalt())

def check_password(plain_text_password, hashed_password):
  return bcrypt.checkpw(plain_text_password, hashed_password)

access={}

access["admin"]=get_hashed_password(("password").encode())
access["user"]=get_hashed_password(("password1").encode())
access["poweruser"]=get_hashed_password(("password2").encode())
#check_password(("password").encode(),access["user"])
