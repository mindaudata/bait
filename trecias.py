import pandas

#Task 0
df = pandas.read_csv('https://raw.githubusercontent.com/vilnius/darzeliai/master/data/Darzeliu%20galimu%20priimti%20ir%20lankantys%20vaikai2018.csv',
                    sep=';')

#Task 1
maximum = df.CHILDS_COUNT.max()
minimum = df.CHILDS_COUNT.min()

print('Didžiausia reikšmė: {}'.format(maximum))
print('Mažiausia reikšmė: {}'.format(minimum))

#Task 2
with open('1_Maximum.txt','w') as f:
    f.write('Didžiausia reikšmė: {}'.format(maximum))
    max = df[df.CHILDS_COUNT==maximum]
    for index, row in max.iterrows():
      f.write('\n'+row.iloc[1][0:3]+'_'+row.iloc[3].split()[1]+'-'+row.iloc[3].split()[3]+'_'+row.iloc[5][0:4])

with open('2_Minimum.txt','w') as f:
    f.write('Mažiausia reikšmė: {}'.format(minimum))
    min = df[df.CHILDS_COUNT==minimum]
    for index, row in min.iterrows():
      f.write('\n'+row.iloc[1][0:3]+'_'+row.iloc[3].split()[1]+'-'+row.iloc[3].split()[3]+'_'+row.iloc[5][0:4])

#Task 3
kalbos = df.groupby('LAN_LABEL').sum()
procentai = kalbos.FREE_SPACE*100/kalbos.CHILDS_COUNT
with open('3_Kalbos.txt','w') as f:
    f.write('Laisvų vietų dalis pagal kalbas:\n')
    procentai.round(2).map('{:.2f}%'.format).to_csv(f, sep=':')

#Task 4
with open('4_LaisvosVietos.txt','w') as f:
    f.write('Darželiai turintys grupes su 2-4 laisvomis vietomis:\n')
    for darzelis in df.query('2 <= FREE_SPACE <= 4').groupby('SCHOOL_NAME').count().sort_values(by='SCHOOL_NAME', ascending=False).index.get_level_values(0).tolist():
        f.write(darzelis+'\n')
