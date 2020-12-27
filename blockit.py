import os

# Block based on DNS
def dns():
    zero = '0.0.0.0'
    link = input('Please enter the domain:\n')
# Open /etc/hosts and modify it
    os.system('sudo chmod 777 /etc/hosts')
    with open('/etc/hosts',mode='a') as f:
        f.write('\n'+zero+'\t'+link)
    print(link+' was added.')

dns()
