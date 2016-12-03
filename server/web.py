from Crypto.PublicKey import RSA
from Crypto import Random

random_generator = Random.new().read
key = RSA.generate(2048, random_generator)
public_key = key.publickey()
data = public_key.encrypt('hello', 0)[0]

print "############ Encrypted #############"
print
print data
print
print "############ Decrypted #############"
print
print key.decrypt(data)
print