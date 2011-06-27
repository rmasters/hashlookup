# Hash-cracker

Python scripts to perform reverse lookups on hashes in the following
encryptions:

* MD5
* SHA1
* SHA224
* SHA256
* SHA385
* SHA512
* Base16
* Base32
* Base64

## Usage

> Be aware this is my first Python project, it's kinda quirky but it
works for now. As such please let me know any comments you have so that
I can improve :)

1.  Build your database by running `populate-nothread.py`. 
    *   At the moment this is unthreaded and saves records to the
        database every 50 records - so watch out if you make searches
        while it's generating as the database will lock up.
    *   Note that the default charset is very long and will take a long
        time to complete :)
2. Search using `search.py`
3. Check the number of rows stored using `count.py`
4. Check out the last 10 inserted rows using `list.py`