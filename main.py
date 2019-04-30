import hashlib

hashes = open('hashes.txt', 'r').read()
hashes = hashes.split('\n')
hashes = list(map(lambda t: t[7:39].lower(), hashes))

answer_file = open("answer.txt", "a+")

def find_pass(hash, db):
  for password in db:
    tmp = hashlib.md5(password.encode('utf-8')).hexdigest() 
    if tmp == hash:
      return password
db_passwords = open("./1000000.txt", "r").read()
db_passwords = db_passwords.split('\n')


for i in range(len(hashes)):
  index = i + 1
  hash_tmp = hashes[i]
  password = find_pass(hash_tmp, db_passwords)
  print('Progress:', str(round((i+1) / len(hashes) * 100))+'%')
  answer_file.write(
    '{} | {} | {}\n'
    .format(index, hash_tmp, password))


def find_pass(hash, db):
  for password in db:
    tmp = hashlib.md5(password.encode('utf-8')).hexdigest() 
    if tmp == hash:
      return password





