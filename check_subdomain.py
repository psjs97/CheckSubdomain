#!/usr/bin/python

# Libraries
import requests
from sys import argv

# Check arguments
if len(sys.argv) < 3: 
    print('Usage: ',sys.argv[0],'<domain>','<list>')
    sys.exit(1)

# Reading file with words to test potential subdomains
with open(sys.argv[2]) as wordlist_file: 
    word_list = wordlist_file.readlines()
    word_list = [word.rstrip() for word in word_list]

# Creating result dataframe empty 
subdomains_result_df = pd.DataFrame(columns=['subdomain', 'valid'])

# Checking "subdomains"
for sub in word_list:
    domain = f"http://{sub}.{sys.argv[1]}" 
    valid_domain = False
    
    try:
        requests.get(domain)
    
    except requests.ConnectionError: 
        valid_domain = False
    
    else:
        valid_domain = True
        
    new_row = {'domain': domain, 'valid': valid_domain}
    subdomains_result_df = subdomains_result_df.append(new_row, ignore_index=True)
    
# Writing output results
subdomains_result_df.to_csv('subdomains.csv',sep=';',index=False)