import csv

def datafix():
    csv_coloums = ['NIM','TUGAS1','TUGAS2','QUIZ1','QUIZ2','UTS','UAS']
    dict_data = [
    {'NIM': 1101110061, 'TUGAS1': 50, 'TUGAS2': 75, 'QUIZ1': 50, 'QUIZ2': 78, 'UTS': 79, 'UAS': 40},
    {'NIM': 1101110062, 'TUGAS1': 50, 'TUGAS2': 80, 'QUIZ1': 50, 'QUIZ2': 50, 'UTS': 65, 'UAS': 26},
    {'NIM': 1101110063, 'TUGAS1': 60, 'TUGAS2': 75, 'QUIZ1': 77, 'QUIZ2': 79, 'UTS': 50, 'UAS': 51},
    {'NIM': 1101110064, 'TUGAS1': 52, 'TUGAS2': 85, 'QUIZ1': 50, 'QUIZ2': 80, 'UTS': 80, 'UAS': 30},
    {'NIM': 1101110065, 'TUGAS1': 70, 'TUGAS2': 85, 'QUIZ1': 50, 'QUIZ2': 80, 'UTS': 80, 'UAS': 88},
    {'NIM': 1101110066, 'TUGAS1': 75, 'TUGAS2': 80, 'QUIZ1': 50, 'QUIZ2': 95, 'UTS': 50, 'UAS': 67},
    {'NIM': 1101110067, 'TUGAS1': 72, 'TUGAS2': 80, 'QUIZ1': 70, 'QUIZ2': 90, 'UTS': 85, 'UAS': 86},
    {'NIM': 1101110068, 'TUGAS1': 95, 'TUGAS2': 80, 'QUIZ1': 50, 'QUIZ2': 95, 'UTS': 50, 'UAS': 85},
    {'NIM': 1101110069, 'TUGAS1': 76, 'TUGAS2': 95, 'QUIZ1': 90, 'QUIZ2': 100, 'UTS': 95, 'UAS': 79},
    {'NIM': 1101110070, 'TUGAS1': 94, 'TUGAS2': 80, 'QUIZ1': 90, 'QUIZ2': 100, 'UTS': 100, 'UAS': 66},
    {'NIM': 1101110071, 'TUGAS1': 92, 'TUGAS2': 75, 'QUIZ1': 60, 'QUIZ2': 92, 'UTS': 95, 'UAS': 79},
    {'NIM': 1101110072, 'TUGAS1': 59, 'TUGAS2': 85, 'QUIZ1': 60, 'QUIZ2': 80, 'UTS': 80, 'UAS': 42},
    {'NIM': 1101110073, 'TUGAS1': 50, 'TUGAS2': 80, 'QUIZ1': 70, 'QUIZ2': 90, 'UTS': 85, 'UAS': 61},
    {'NIM': 1101110074, 'TUGAS1': 60, 'TUGAS2': 85, 'QUIZ1': 60, 'QUIZ2': 82, 'UTS': 81, 'UAS': 64},
    {'NIM': 1101110075, 'TUGAS1': 98, 'TUGAS2': 95, 'QUIZ1': 80, 'QUIZ2': 100, 'UTS': 100, 'UAS': 100},
    {'NIM': 1101110076, 'TUGAS1': 50, 'TUGAS2': 50, 'QUIZ1': 70, 'QUIZ2': 70, 'UTS': 85, 'UAS': 70},
    {'NIM': 1101110077, 'TUGAS1': 100, 'TUGAS2': 100, 'QUIZ1': 90, 'QUIZ2': 90, 'UTS': 95, 'UAS': 96},
    {'NIM': 1101110078, 'TUGAS1': 60, 'TUGAS2': 90, 'QUIZ1': 60, 'QUIZ2': 80, 'UTS': 80, 'UAS': 32},
    {'NIM': 1101110079, 'TUGAS1': 66, 'TUGAS2': 100, 'QUIZ1': 90, 'QUIZ2': 90, 'UTS': 95, 'UAS': 100},
    {'NIM': 1101110080, 'TUGAS1': 50, 'TUGAS2': 80, 'QUIZ1': 60, 'QUIZ2': 80, 'UTS': 80, 'UAS': 91},
    {'NIM': 1101110081, 'TUGAS1': 73, 'TUGAS2': 95, 'QUIZ1': 90, 'QUIZ2': 90, 'UTS': 95, 'UAS': 88},
    {'NIM': 1101110082, 'TUGAS1': 100, 'TUGAS2': 95, 'QUIZ1': 90, 'QUIZ2': 98, 'UTS': 99, 'UAS': 100},
    {'NIM': 1101110083, 'TUGAS1': 80, 'TUGAS2': 95, 'QUIZ1': 90, 'QUIZ2': 90, 'UTS': 95, 'UAS': 100},
    {'NIM': 1101110084, 'TUGAS1': 50, 'TUGAS2': 51, 'QUIZ1': 50, 'QUIZ2': 51, 'UTS': 51, 'UAS': 51},
    {'NIM': 1101110085, 'TUGAS1': 62, 'TUGAS2': 95, 'QUIZ1': 90, 'QUIZ2': 90, 'UTS': 95, 'UAS': 58},
    {'NIM': 1101110086, 'TUGAS1': 80, 'TUGAS2': 50, 'QUIZ1': 90, 'QUIZ2': 90, 'UTS': 95, 'UAS': 92},
    {'NIM': 1101110087, 'TUGAS1': 60, 'TUGAS2': 95, 'QUIZ1': 70, 'QUIZ2': 70, 'UTS': 85, 'UAS': 64},
    {'NIM': 1101110088, 'TUGAS1': 64, 'TUGAS2': 80, 'QUIZ1': 80, 'QUIZ2': 80, 'UTS': 90, 'UAS': 54},
    {'NIM': 1101110089, 'TUGAS1': 85, 'TUGAS2': 85, 'QUIZ1': 90, 'QUIZ2': 95, 'UTS': 50, 'UAS': 100},
    {'NIM': 1101110090, 'TUGAS1': 50, 'TUGAS2': 90, 'QUIZ1': 50, 'QUIZ2': 60, 'UTS': 70, 'UAS': 15},
    {'NIM': 1101110091, 'TUGAS1': 60, 'TUGAS2': 80, 'QUIZ1': 80, 'QUIZ2': 80, 'UTS': 80, 'UAS': 72},
    {'NIM': 1101110092, 'TUGAS1': 67, 'TUGAS2': 95, 'QUIZ1': 70, 'QUIZ2': 90, 'UTS': 85, 'UAS': 92},
    {'NIM': 1101110093, 'TUGAS1': 60, 'TUGAS2': 90, 'QUIZ1': 60, 'QUIZ2': 84, 'UTS': 82, 'UAS': 71},
    {'NIM': 1101110094, 'TUGAS1': 52, 'TUGAS2': 70, 'QUIZ1': 50, 'QUIZ2': 78, 'UTS': 79, 'UAS': 25},
    {'NIM': 1101110095, 'TUGAS1': 53, 'TUGAS2': 100, 'QUIZ1': 90, 'QUIZ2': 90, 'UTS': 95, 'UAS': 74},
    {'NIM': 1101110096, 'TUGAS1': 50, 'TUGAS2': 85, 'QUIZ1': 60, 'QUIZ2': 80, 'UTS': 80, 'UAS': 42},
    {'NIM': 1101110097, 'TUGAS1': 72, 'TUGAS2': 85, 'QUIZ1': 50, 'QUIZ2': 91, 'UTS': 50, 'UAS': 73},
    {'NIM': 1101110098, 'TUGAS1': 50, 'TUGAS2': 50, 'QUIZ1': 70, 'QUIZ2': 90, 'UTS': 85, 'UAS': 37},
    {'NIM': 1101110099, 'TUGAS1': 88, 'TUGAS2': 90, 'QUIZ1': 80, 'QUIZ2': 88, 'UTS': 94, 'UAS': 56},
    {'NIM': 1101110100, 'TUGAS1': 85, 'TUGAS2': 85, 'QUIZ1': 90, 'QUIZ2': 95, 'UTS': 50, 'UAS': 100},
    {'NIM': 1101110101, 'TUGAS1': 50, 'TUGAS2': 90, 'QUIZ1': 50, 'QUIZ2': 60, 'UTS': 70, 'UAS': 15},
    ]
    
    
    return dict_data

def ReadCSVFile(filename):
    dataMahasiswa = []
    
    with open(filename) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            dataMahasiswa.append(row)
            
    return dataMahasiswa

def DictionaryNilaiSemuaMahasiswa(dataMahasiswa):
    dictDataNilaiMahasiswa={}
    dataNIM=[]
    dataTugas1=[]
    dataTugas2=[]
    dataQuiz1=[]
    dataQuiz2=[]
    dataUTS=[]
    dataUAS=[]
    
    for data in dataMahasiswa:
        dataNIM.append(data['NIM'])
        dataTugas1.append(data['TUGAS1'])
        dataTugas2.append(data['TUGAS2'])
        dataQuiz1.append(data['QUIZ1'])
        dataQuiz2.append(data['QUIZ2'])
        dataUTS.append(data['UTS'])
        dataUAS.append(data['UAS'])
    
    dictDataNilaiMahasiswa['NIM'] = dataNIM
    dictDataNilaiMahasiswa['TUGAS1'] = dataTugas1
    dictDataNilaiMahasiswa['TUGAS2'] = dataTugas2
    dictDataNilaiMahasiswa['QUIZ1'] = dataQuiz1
    dictDataNilaiMahasiswa['QUIZ2'] = dataQuiz2
    dictDataNilaiMahasiswa['UTS'] = dataUTS
    dictDataNilaiMahasiswa['UAS'] = dataUAS
    
    return dictDataNilaiMahasiswa

def MeanValue(dictionaryNilaiSemuaMahasiswa, key):
    convertToInt  = [int(value) for value in dictionaryNilaiSemuaMahasiswa[key]]
    meanValue = sum(convertToInt)/len(convertToInt)
    
    return ("%.2f" % meanValue)

def MaxValue(dictionaryNilaiSemuaMahasiswa, key): 
    convertToInt  = [int(value) for value in dictionaryNilaiSemuaMahasiswa[key]]
    maxValue = max(convertToInt)
    
    return maxValue

def MinValue(dictionaryNilaiSemuaMahasiswa, key): 
    convertToInt  = [int(value) for value in dictionaryNilaiSemuaMahasiswa[key]]
    minValue = min(convertToInt)
    
    return minValue

def ModValue(dictionaryNilaiSemuaMahasiswa, key): 
    import statistics
    convertToInt  = [int(value) for value in dictionaryNilaiSemuaMahasiswa[key]]
    data = []
    for bilangan in convertToInt :
        data.append(int(bilangan))
    modusValue = statistics.mode(data)
    
    return modusValue

def MedValue(dictionaryNilaiSemuaMahasiswa, key): 
    convertToInt  = [int(value) for value in dictionaryNilaiSemuaMahasiswa[key]]
    
    n = len(convertToInt)
    convertToInt.sort()
    
    if n % 2 == 0:
        median1 = convertToInt[n//2]
        median2 = convertToInt[n//2 - 1]
        medianValue = (median1 + median2)/2
    else:
        medianValue = convertToInt[n//2]
    
    return medianValue
    
def VarValue(dictionaryNilaiSemuaMahasiswa, key): 
    convertToInt  = [int(value) for value in dictionaryNilaiSemuaMahasiswa[key]]
    meanValue = sum(convertToInt)/len(convertToInt)
    list_varian = []
    for bilangan in convertToInt :
        list_varian.append((bilangan - meanValue) ** 2)
    varValue = sum(list_varian)/(len(convertToInt)-1)
    
    return ("%.2f" % varValue)
    
def Stddev(dictionaryNilaiSemuaMahasiswa, key):
    import statistics
    convertToInt  = [int(value) for value in dictionaryNilaiSemuaMahasiswa[key]]
    standardeviasiValue = statistics.stdev(convertToInt)
    
    return  ("%.2f" % standardeviasiValue)
    
def Q1Value(dictionaryNilaiSemuaMahasiswa, key): 
    convertToInt  = [int(value) for value in dictionaryNilaiSemuaMahasiswa[key]]
    n = len(convertToInt)
    q1Value = convertToInt[1*(n+1)//4]
    
    return  q1Value

def Q3Value(dictionaryNilaiSemuaMahasiswa, key): 
    convertToInt  = [int(value) for value in dictionaryNilaiSemuaMahasiswa[key]]
    n = len(convertToInt)
    q3Value = convertToInt[(3*(n+1))//4]
    
    return  q3Value

    
def DictionaryNilaiPerMahasiswa(dataMahasiswa): 
    dictNilaiPerMahasiswa ={}
    
    for data in dataMahasiswa:
        dictNilaiPerMahasiswa[data['NIM']] = data['TUGAS1'], data['TUGAS2'], data['QUIZ1'], data['QUIZ2'], data['UTS'], data['UAS']
   
    return dictNilaiPerMahasiswa


def AkumulasiNilai(dictionaryNilaiPerMahasiswa, nim):
    
    convertToInt  = [int(value) for value in dictionaryNilaiPerMahasiswa[nim]]
    rataRataTugas = sum(convertToInt[0:2])/len(convertToInt[0:2])
    rataRataQuiz  = sum(convertToInt[2:4])/len(convertToInt[2:4])
    akumulasiNilai = ((0.15*rataRataTugas)+(0.15*rataRataQuiz)+(0.35*convertToInt[4])+(0.35*convertToInt[5]))
    return ("%.2f" % akumulasiNilai)

datamean = [] 
datamax = []
datamin = []
datamed = []
dataq1 = [] 
dataq3 = []
datavarian = []
datastandardeviasi = []
datamodus = []

dataMahasiswa = datafix()
dictionaryNilaiMahasiswa = DictionaryNilaiSemuaMahasiswa(dataMahasiswa)

for key in dictionaryNilaiMahasiswa:
    if key == 'NIM':
        meanValue= 'Mean'
        maxValue = 'Nilai Maksimum'
        minValue = 'Nilai Minimum'
        modusValue = 'Modus'
        medianValue = 'Median'
        q1Value = 'Nilai Q1'
        q3Value = 'Nilai Q3'
        varValue = 'Varian'
        standardeviasiValue = 'Standar Deviasi'
    
    else:
        meanValue = MeanValue(dictionaryNilaiMahasiswa, key)
        maxValue = MaxValue(dictionaryNilaiMahasiswa, key)
        minValue = MinValue(dictionaryNilaiMahasiswa, key)
        modusValue = ModValue(dictionaryNilaiMahasiswa, key)
        medianValue = MedValue(dictionaryNilaiMahasiswa, key)
        q1Value = Q1Value(dictionaryNilaiMahasiswa, key)
        q3Value = Q3Value(dictionaryNilaiMahasiswa, key)
        varValue = VarValue(dictionaryNilaiMahasiswa, key)
        standardeviasiValue = Stddev(dictionaryNilaiMahasiswa, key)
        
    datamean.append(meanValue)
    datamax.append(maxValue)
    datamin.append(minValue)
    datamodus.append(modusValue)
    datamed.append(medianValue)
    dataq1.append(q1Value)
    dataq3.append(q3Value)
    datavarian.append(varValue)
    datastandardeviasi.append(standardeviasiValue)
    
    

dictionaryNilaiPerMahasiswa = DictionaryNilaiPerMahasiswa(dataMahasiswa)

dictnilai = {}
for nim in dictionaryNilaiMahasiswa['NIM']:
    akumulasiNilaiPerMahasiswa = AkumulasiNilai(dictionaryNilaiPerMahasiswa, nim)
    listdata = list(dictionaryNilaiPerMahasiswa[nim])
    listdata.append(akumulasiNilaiPerMahasiswa)
    dictnilai[nim] = listdata
    
with open('dataset7_fixed.csv', mode='w') as csv_file:
    fieldnames = ['NIM', 'TUGAS1', 'TUGAS2', 'QUIZ1', 'QUIZ2', 'UTS', 'UAS', 'TOTAL']
    
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    writer.writeheader()

    for nim in dictionaryNilaiMahasiswa['NIM']:
         writer.writerow({'NIM':nim,'TUGAS1':dictnilai[nim][0],'TUGAS2':dictnilai[nim][1],'QUIZ1':dictnilai[nim][2],'QUIZ2':dictnilai[nim][3],'UTS':dictnilai[nim][4],'UAS':dictnilai[nim][5],'TOTAL':dictnilai[nim][6]})
    writer.writerow({'NIM':datamean[0],'TUGAS1':datamean[1],'TUGAS2':datamean[2],'QUIZ1':datamean[3],'QUIZ2':datamean[4],'UTS':datamean[5],'UAS':datamean[6]})
    writer.writerow({'NIM':datamax[0],'TUGAS1':datamax[1],'TUGAS2':datamax[2],'QUIZ1':datamax[3],'QUIZ2':datamax[4],'UTS':datamax[5],'UAS':datamax[6]})
    writer.writerow({'NIM':datamin[0],'TUGAS1':datamin[1],'TUGAS2':datamin[2],'QUIZ1':datamin[3],'QUIZ2':datamin[4],'UTS':datamin[5],'UAS':datamin[6]})
    writer.writerow({'NIM':datamodus[0],'TUGAS1':datamodus[1],'TUGAS2':datamodus[2],'QUIZ1':datamodus[3],'QUIZ2':datamodus[4],'UTS':datamodus[5],'UAS':datamodus[6]})
    writer.writerow({'NIM':datamed[0],'TUGAS1':datamed[1],'TUGAS2':datamed[2],'QUIZ1':datamed[3],'QUIZ2':datamed[4],'UTS':datamed[5],'UAS':datamed[6]})
    writer.writerow({'NIM':dataq1[0],'TUGAS1':dataq1[1],'TUGAS2':dataq1[2],'QUIZ1':dataq1[3],'QUIZ2':dataq1[4],'UTS':dataq1[5],'UAS':dataq1[6]})
    writer.writerow({'NIM':dataq3[0],'TUGAS1':dataq3[1],'TUGAS2':dataq3[2],'QUIZ1':dataq3[3],'QUIZ2':dataq3[4],'UTS':dataq3[5],'UAS':dataq3[6]})
    writer.writerow({'NIM':datavarian[0],'TUGAS1':datavarian[1],'TUGAS2':datavarian[2],'QUIZ1':datavarian[3],'QUIZ2':datavarian[4],'UTS':datavarian[5],'UAS':datavarian[6]})
    writer.writerow({'NIM':datastandardeviasi[0],'TUGAS1':datastandardeviasi[1],'TUGAS2':datastandardeviasi[2],'QUIZ1':datastandardeviasi[3],'QUIZ2':datastandardeviasi[4],'UTS':datastandardeviasi[5],'UAS':datastandardeviasi[6]})
