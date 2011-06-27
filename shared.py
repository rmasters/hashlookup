# -*- coding: iso-8859-15 -*-

import sqlite3

def get_db():
    return sqlite3.connect("hashes.db")

def count_all():
    cur = get_db().cursor()
    cur.execute("SELECT COUNT(plaintext) FROM hashes")
    return cur.fetchone()[0]

def fetch_all(count = None):
    cur = get_db().cursor()
    qry = "SELECT plaintext, md5, sha1, sha224, sha256, sha384,\
                sha512, base16, base32, base64 FROM hashes"
    if count is not None:
        qry += " LIMIT " + str(int(count))

    cur.execute(qry)
    return cur

def fetch_all_rev(count = None):
    cur = get_db().cursor()
    qry = "SELECT plaintext, md5, sha1, sha224, sha256, sha384,\
                sha512, base16, base32, base64 FROM hashes ORDER BY\
                ROWID DESC"
    if count is not None:
        qry += " LIMIT " + str(int(count))
    
    cur.execute(qry)
    return cur

def find(hash):
    cur = get_db().cursor()
    cur.execute("SELECT * FROM hashes WHERE md5=:hash OR sha1=:hash\
                OR sha224=:hash OR sha256=:hash OR sha384=:hash OR\
                sha512=:hash OR base16=:hash OR base32=:hash OR\
                base64=:hash", {"hash": hash})
    return cur

def display_row(row):
    result =  "Plaintext: %s\n" % row[0].encode("iso-8859-1")
    result += "MD5: %s\n" % row[1].encode("iso-8859-1")
    result += "SHA1: %s\n" % row[2].encode("iso-8859-1")
    result += "SHA224: %s\n" % row[3].encode("iso-8859-1")
    result += "SHA256: %s\n" % row[4].encode("iso-8859-1")
    result += "SHA384: %s\n" % row[5].encode("iso-8859-1")
    result += "SHA512: %s\n" % row[6].encode("iso-8859-1")
    result += "Base16: %s\n" % row[7].encode("iso-8859-1")
    result += "Base32: %s\n" % row[8].encode("iso-8859-1")
    result += "Base64: %s" % row[9].encode("iso-8859-1")
    return result