import requests
import hashlib
import sys

def request_api_data(query_data):
    url = 'https://api.pwnedpasswords.com/range/' + query_data
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again.')
    return res

def pass_leak_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0 

def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    reponse = request_api_data(first5_char)
    return pass_leak_count(reponse, tail)

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} time(s). You should change your password.')
        else: 
            print(f'{password} was not found. You can use it.')
    return 'DONE!'
    
if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

