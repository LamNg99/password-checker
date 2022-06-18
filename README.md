# Password Checker
Check how many times have your password been exposed in data breaches by sending the first 5 characters of a SHA-1 password hash (not case-sensitive) to be passed to the API. When a password hash with the same first 5 characters is found in the Pwned Passwords repository, the API will respond with an HTTP 200 and include the suffix of every hash beginning with the specified prefix, followed by a count of how many times it appears in the data set.

## Prerequisites
Installation of below module using command line:
<pre>pip3 install requests</pre>

## Usage
Running `checkmypass.py` file followed with as many passwords as you want to check separately by space.
<pre>python3 checkmypass.py fisrtpass secondpass</pre>

