
### Import libraries
import pprint as pp
import time
import TDAPI
from datetime import datetime
import paramiko
from scp import SCPClient

def get_accounts(TDSession):
    accounts = TDSession.get_accounts(fields=['positions'])
    return accounts

def createSSHClient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client

def main():
    for i in range(60):
        try:
            TDSession = TDAPI.td_login()  
            time.sleep(10)     
            break
        except Exception as e:
            print('###########TDA API FAILURE#########')
            print(e)
            print(i)
            print('###########TDA API FAILURE#########')
            time.sleep(60)
            pass
    for i in range(1000):
        try:
            accounts = get_accounts(TDSession)[0]
            total_account_value = accounts['securitiesAccount']['currentBalances']['liquidationValue']
            pp.pprint(total_account_value)
            if total_account_value > 500:
                print('We are rich')
                ssh = createSSHClient('10.99.99.99', '22', 'pi', 'PASSWORD')
                scp = SCPClient(ssh.get_transport())
                scp.put("/home/shawn/TDAmeritrade/milestone.txt")
                exit()
            else:
                print('We will be rich soon')


        except Exception as e:
            print('###########TDA API FAILURE#########')
            print(e)
            print(i)
            print('###########TDA API FAILURE#########')
            pass
        time.sleep(60)
### Run the main function    
if __name__ == "__main__":
    main()
