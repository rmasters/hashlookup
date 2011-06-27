# -*- coding: iso-8859-15 -*-
"""
A script to construct a hash database, suitable for reverse-lookups.

This script builds strings in a brute-force fashion, generates lots of
hashes of it and stores it for lookup. It can be run 

"""

import base64
import hashlib
import string
import sqlite3

def get_charset():
    special_chars = u"!\"£$#%^&*()[]{}-_=+#~'@`¬|\\/:;"
    charset = string.letters + string.digits + special_chars
    return charset

def permutate(charset):
    # Index
    index = (0, 0)
    # List of permutations
    perms = list(charset)
    
    # Number of permutations
    for n in range(1, len(perms)):
        index = (index[1], len(perms))
        for s in perms[index[0]:]:
            for c in charset:
                result = s + c
                perms.append(result)
                save_row(result)

def save_row(plain):
    global cursor, db, commit_offset, insert_count
    values = (plain, hashlib.md5(plain.encode("iso-8859-1")).hexdigest(),
              hashlib.sha1(plain.encode("iso-8859-1")).hexdigest(),
              hashlib.sha224(plain.encode("iso-8859-1")).hexdigest(),
              hashlib.sha256(plain.encode("iso-8859-1")).hexdigest(),
              hashlib.sha384(plain.encode("iso-8859-1")).hexdigest(),
              hashlib.sha512(plain.encode("iso-8859-1")).hexdigest(),
              base64.b16encode(plain.encode("iso-8859-1")),
              base64.b32encode(plain.encode("iso-8859-1")),
              base64.b64encode(plain.encode("iso-8859-1"))
    )
                
    cursor.execute("insert into hashes (plaintext, md5, sha1, sha224,\
                   sha256, sha384, sha512, base16, base32, base64)\
                   values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", values)
    insert_count += 1
    
    if insert_count % commit_offset == 0:
        db.commit()

db = sqlite3.connect("hashes.db")
db.execute("""create table if not exists hashes (
    plaintext TEXT,
    md5 TEXT,
    sha1 TEXT,
    sha224 TEXT,
    sha256 TEXT,
    sha384 TEXT,
    sha512 TEXT,
    base16 TEXT,
    base32 TEXT,
    base64 TEXT
);""")

cursor = db.cursor()

insert_count = 0
commit_offset = 50

print "Starting permutations"
print "Try not to cancel the script as it might corrupt the database (threaded version coming soon)"
print "Committing to database every %d results" % commit_offset

permutate(get_charset())

print "Finished permutating!"