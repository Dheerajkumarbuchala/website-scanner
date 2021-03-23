import os

def get_nmap(option,ip):
    command = "nmap " + option + " " + ip
    process = os.popen(command)
    results = str(process.read())
    return results

#print(get_nmap("-F","34.218.62.116"))