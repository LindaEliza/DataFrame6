# -*- coding: utf-8 -*-
"""
Created on Tue May 03 10:52:11 2016

@author: Isa Miranda
"""

%matplotlib inline
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

datos = pd.read_csv("diabetic_data.csv")

datos.head()

sexo = datos.gender

raza = datos.race

total = raza.count()

probabilidad = 100 * datos['race'].value_counts() / len(datos['race'])


f = (datos.race == "Caucasian")& (datos.gender == "Female")
caucasianf = raza[f]
freqcauf = caucasianf.count()

m = (datos.race == "Caucasian") & (datos.gender == "Male")
caucasianm = raza[m]
freqcaum = caucasianm.count()


pcaucasian = 100 * (datos.race == "Caucasian").value_counts() / len(datos['race'])


#Son 76099 registros de raza caucasian
#probabilidad de que sea caucasian 0.748 = 74.8%

g = (datos.race == "AfricanAmerican")& (datos.gender == "Female")
afroamericanosf = raza[g]
freqafrof = afroamericanosf.count()

h = (datos.race == "AfricanAmerican")& (datos.gender == "Male")
afroamericanosm = raza[h]
freqafrom = afroamericanosm.count()

pafroamerican = 100 * (datos.race == "AfricanAmerican").value_counts() / len(datos['race'])

#Son 19210 registros de raza afroamericana
#probabilidad de que sea afroamericanos 0.188 = 18.9%

s = (datos.race == "Hispanic") & (datos.gender == "Female")
hispanosf = raza[s]
freqhispf = hispanosf.count()

l = (datos.race == "Hispanic") & (datos.gender == "Male")
hispanosm = raza[l]
freqhispm = hispanosm.count()

phispanos = 100 * (datos.race == "Hispanic").value_counts() / len(datos['race'])

#probabilidad de que sea hispano 0.02 = 2%

a = (datos.race == "Asian") & (datos.gender == "Female")
asiaticof = raza[a]
freqaf = asiaticof.count()

b = (datos.race == "Asian") & (datos.gender == "Male")
asiaticom = raza[b]
freqam = asiaticom.count()

pasiaticos = 100 * (datos.race == "Asian").value_counts() / len(datos['race'])

#probabilidad de que sea asiatico 0.0063 = 0.63%

o = (datos.race == "Other") & (datos.gender == "Male")
otrosm = raza[o]
freqotrosm = otrosm.count() 

p = (datos.race == "Other") & (datos.gender == "Female")
otrosf = raza[p]
freqotrosf = otrosf.count() 

potros = 100 * (datos.race == "Other").value_counts() / len(datos['race'])

#probabilidad de que sea otra raza 0.0148 = 1.48%

n = (datos.race == "?") & (datos.gender == "Female")
nulosf = raza[n]
freqnullf = nulosf.count()

t = (datos.race == "?") & (datos.gender == "Male")
nulosm = raza[t]
freqnullm = nulosm.count()

pnull = 100 * (datos.race == "?").value_counts() / len(datos['race'])

#no hay data de un 0.0223 = 2.2%

raw_data = {'Raza': ['Caucásico', 'Afroamericano', 'Hispano', 'Asiatico', 'Otro', 'No hay info'],
        'Masculino': [freqcaum, freqafrom, freqhispm, freqam, freqotrosm, freqnullm],
        'Femenino': [freqcauf, freqafrof, freqhispf, freqaf, freqotrosf, freqnullf]
        }
        
df = pd.DataFrame(raw_data, columns = ['Raza', 'Masculino', 'Femenino'])

df['Total'] = df['Masculino'] + df['Femenino'] 

sum_row = df[["Masculino","Femenino","Total",]].sum()
sum_row

df_sum = pd.DataFrame(data=sum_row).T
df_sum

df_sum = df_sum.reindex(columns= df.columns)
df_sum

#Dataframe final con totales 
df_final = df.append(df_sum,ignore_index=True)
df_final.tail()


Razaspiegraph = datos['race'].value_counts().plot(kind='pie', autopct='%.2f', 
                                            figsize=(6, 6),
                                            title='Personas diagnosticadas con diabetes')

plot = (100 * datos['race'].value_counts() / len(datos['race'])).plot(
kind='bar', title='Razas diagnosticadas con diabetes %')

tablacont = pd.crosstab(index=datos['race'],
            columns=datos['gender'], margins=True)
            
tablaprob = pd.crosstab(index=datos['race'], columns=datos['gender']).apply(lambda r: r/r.sum() *100,
                                axis=1)


graficars = pd.crosstab(index=datos['race'],
            columns=datos['gender']).apply(lambda r: r/r.sum() *100, axis=1).plot(kind='bar')

fig = graficars.get_figure()
fig.savefig("relacion_razaysexo.png")


#¿Qué rango de edad tiene la probabiidad más alta de tener diabetes?



graficaedad = (100 * datos['age'].value_counts() / len(datos['age'])).plot(
kind='bar', title='Rango de edades diagnosticadas con diabetes %')

#R// El rango de edad con la probabilidad más alta de tener diabetes es el de 70-80 años de edad con un porcentaje de . 

fig = graficaedad.get_figure()
fig.savefig("graficaedad.png")

#¿Existe una relación entre el tiempo que las personas con diabetes están en el hospital y el número de laboratorios que les hacen?

#agrupar por tiempo en el hospital  sacando las medianas



tiempo = datos.time_in_hospital

labs = datos.num_lab_procedures

dfcuant = pd.DataFrame({'Tiempo en el hospital' : tiempo,
                'Num. de laboratorios': labs})
dfcuant.describe()


tabtiempolabs = pd.crosstab(index=datos['time_in_hospital'],
            columns=datos['num_lab_procedures'], margins=True)

medlabs = tabtiempolabs.mean(axis=1)


dispcuant= dfcuant.plot(kind='scatter', x='Tiempo en el hospital', y='Num. de laboratorios')
correlacion = dfcuant.corr()

#R// NO EXISTE RELACIÓN ENTRE LAS VARIABLES

