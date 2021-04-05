from pywebio.input import *
from pywebio.output import *
from get_tld import *
from get_ip import *
from nmap import *
from robots_txt import *
from whois import *

url = input('Enter URL', type=TEXT, placeholder='Please enter the full URL.(i.e including https://)', required=True)

try:
    tld = get_fld(url)
    put_text("The Top Level Domain is : ",tld)
    ip = get_ip_address(tld)
    put_text("IP Address is : ",ip)
    whois = get_whois(tld)
    put_text("The information of the website : ",whois)
    nmap = get_nmap('-F', ip)
    put_text("NMAP : ",nmap)
    robots = get_robots_txt(url)
    put_text("These are not accessable : ",robots)
except:
    put_text("Your URL is not valid")