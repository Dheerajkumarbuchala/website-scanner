import os

def get_whois(tld):
    command = "whois " + tld
    process = os.popen(command)
    results = str(process.read())
    return results

#print(get_whois("geeksforgeeks.org"))