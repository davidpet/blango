import hashlib

# Level 1 - hash
print(hashlib.sha256(b"password").hexdigest())
print(hashlib.sha256(b"hello wold").hexdigest())
print(hashlib.sha256(b"password123").hexdigest())

#Level 2 - salt
print(hashlib.sha256(b"abc123" + b"password123").hexdigest())

#Level 3 - iterations
hash = hashlib.sha256(b"abc123" + b"password123").hexdigest()
for i in range(1000):
  hash = hashlib.sha256(b"abc123" + hash.encode('ascii')).hexdigest()
print(hash)
