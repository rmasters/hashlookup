# -*- coding: iso-8859-15 -*-

from shared import display_row, fetch_all, fetch_all_rev

if __name__ == "__main__":
    count = 10
    print "First %d rows:" % count
    for row in fetch_all(10):
        print "-"*20
        print display_row(row)
    
    print ""
    
    print "Last %d rows:" % count
    for row in fetch_all_rev(10):
        print "-"*20
        print display_row(row)