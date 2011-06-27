# -*- coding: iso-8859-15 -*-

from shared import display_row, find

if __name__ == "__main__":
    hash = raw_input("Enter the hash to search for: ")
    cur = find(hash)
    
    if cur.rowcount == 0:
        print "No passwords found for that hash"
    else:
        for row in cur.fetchall():
            print "-"*20
            print display_row(row)
    