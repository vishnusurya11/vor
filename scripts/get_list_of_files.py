import pandas

'''
stock_df = pandas.read_csv('NYSE.txt', sep = '\t')

print(stock_df)'''

def clean_data():
    with open('NYSE.txt', 'r') as f:
        a = f.readlines()
    a = a[1:]
    with open('NYSE_new.txt', 'w') as j:
        for x in a:
            if '-' in x or '.' in x:
                continue
            j.write(x)
    return True


def create_process_log():
    with open('process_log.csv', 'w') as f:
        f.write('Symbol,Description,Status,Daily_Stock_Data_Created_Time,Daily_Stock_Data_Updated_Time,Minute_Stock_Data_Created_Time,Minute_Stock_Data_Updated_Time\n')
    return True

def add_to_process_log():
    with open('NYSE_new.txt', 'r') as f:
        a = f.readlines()

    with open('process_log.csv', 'a') as j:
        try:
            for x in a:
                j.write(','.join(x.replace('\n','').split('\t'))+',0,,,,\n')
        except Exception as e:
            print(e)
    
    return True

def read_process_log():
    

if __name__ == '__main__':
    #clean_data()
    #create_process_log()
    #add_to_process_log()
    read_process_log()
