
"""
Created on Thu Mar 23 11:20:06 2023

@author: Michelle.Ponce
"""
import numpy as np
import pandas as pd 
from random_address import real_random_address

from random_address import real_random_address

listOrderCount1 = list(range(0, 20))

f = open('C:/Users/Michelle.Ponce/OneDrive - Solera Holdings, Inc/Documents/TesterPerformance/RealAddress.csv', 'w+')
for i in range(0,20):
    listOrderCount1[i]= real_random_address()
    realaddress= listOrderCount1[i]
    f.write(str(realaddress) + "\n")
f.close()
    

#Lectura del datasource
dataSource = pd.read_csv('C:/Users/Michelle.Ponce/OneDrive - Solera Holdings, Inc/Documents/TesterPerformance/RealAddress.csv', header=None)


dataSource.columns = ["address", "address2", "city", "state", "postalcode", "latitude", "longittude"]

#Creamos las variables para construir el dataset que va para VuGen
dataSource['Address']=''
dataSource['City']=''
dataSource['State']=''
dataSource['Postalcode']=''


#Comenzamos a separar el String, columna address
#
#Address
dataSource['Address']=dataSource.address
separado= dataSource['Address'].str.split("{'address1': '", n=1, expand=True)
separado2=separado[1].str.split("'",n=1,expand=True)
dataSource['Address']=separado2[0]

#City
dataSource['City']=dataSource.city
separado= dataSource['City'].str.split(" 'city': '", n=1, expand=True)
separado2=separado[1].str.split("'",n=1,expand=True)
dataSource['City']=separado2[0]

#State
dataSource['State']=dataSource.state
separado= dataSource['State'].str.split(" 'state': '", n=1, expand=True)
separado2=separado[1].str.split("'",n=1,expand=True)
dataSource['State']=separado2[0]

#Postalcode
dataSource['Postalcode']=dataSource.postalcode
separado= dataSource['Postalcode'].str.split(" 'postalCode': '", n=1, expand=True)
separado2=separado[1].str.split("'",n=1,expand=True)
dataSource['Postalcode']=separado2[0]

dataSource.drop('address', axis=1, inplace=True)
dataSource.drop('city', axis=1, inplace=True)
dataSource.drop('state', axis=1, inplace=True)
dataSource.drop('postalcode', axis=1, inplace=True)
dataSource.drop('address2', axis=1, inplace=True)
dataSource.drop('latitude', axis=1, inplace=True)
dataSource.drop('longittude', axis=1, inplace=True)

dataSource.to_csv('C:/Users/Michelle.Ponce/OneDrive - Solera Holdings, Inc/Documents/TesterPerformance/RealAddress2.csv', index=False)


