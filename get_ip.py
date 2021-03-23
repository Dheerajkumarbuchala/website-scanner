import os

def get_ip_address(tld):
    command = "host " + tld
    process = os.popen(command)
    results = str(process.read())
    mark = results.find('has address') + 12
    return results[mark:].splitlines()[0]

#print(get_ip_address("geeksforgeeks.org"))