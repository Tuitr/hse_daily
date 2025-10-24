import pandas as pd
import re

pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', None)


def get_rows(day):
    if day == 'monday':
        skip = 10
    elif day == 'tuesday':
        skip = 19
    elif day == 'wednesday':
        skip = 28
    elif day == 'friday':
        skip = 46
    return skip


def d(group, week, day):
    skip = get_rows(day)

    if group == '1': cols, cols_num = 'E:G', ['4', '5', '6']
    if group == '2': cols, cols_num = 'I:K', ['8', '9', '10']
    if group == '3': cols, cols_num = 'M:O', ['12', '13', '14']
    if group == '4': cols, cols_num = 'Q:S', ['16', '17', '18']
    if group == '5': cols, cols_num = 'U:W', ['20', '21', '22']
    if group == '6': cols, cols_num = 'Y:AA', ['24', '25', '26']
    if group == '7': cols, cols_num = 'AC:AE', ['28', '29', '30']

    data = pd.read_excel("data.xlsx", skiprows=skip, nrows=8, usecols=f'{cols}')

    name_work = [[''], [''], [''], [''], [''], [''], [''], ['']]
    number_class = [[''], [''], [''], [''], [''], [''], [''], ['']]
    place = [[''], [''], [''], [''], [''], [''], [''], ['']]
    table = [
        ['', ''], ['', ''], ['', ''], ['', ''],
        ['', ''], ['', ''], ['', ''], ['', '']
    ]
    time = [
        '𝟴:𝟬𝟬 - 𝟵:𝟮𝟬 \n', '𝟵:𝟯𝟬 - 𝟭𝟬:𝟱𝟬 \n', '𝟭𝟭:𝟭𝟬 - 𝟭𝟮:𝟯𝟬 \n', '𝟭𝟯:𝟬𝟬 - 𝟭𝟰:𝟮𝟬 \n',
        '𝟭𝟰:𝟰𝟬 - 𝟭𝟲:𝟬𝟬 \n', '𝟭𝟲:𝟮𝟬 - 𝟭𝟳:𝟰𝟬 \n', '𝟭𝟴:𝟭𝟬 - 𝟭𝟵:𝟯𝟬 \n', '𝟭𝟵:𝟰𝟬 - 𝟮𝟭:𝟬𝟬 \n'
    ]

    for i in range(8):
        if type(data[f'Unnamed: {cols_num[0]}'].iloc[i]) == str:
            name_work[i][0] += f'{str(data[f'Unnamed: {cols_num[0]}'].iloc[i])}'  # .replace('\n','')
        if type(data[f'Unnamed: {cols_num[1]}'].iloc[i]) == str or type(
                data[f'Unnamed: {cols_num[1]}'].iloc[i]) == int or str(
                type(data[f'Unnamed: {cols_num[1]}'].iloc[i])) == "<class 'numpy.float64'>":
            number_class[i][0] += f'{str(data[f'Unnamed: {cols_num[1]}'].iloc[i]).replace('\n', '')[:3]}'
        if type(data[f'Unnamed: {cols_num[2]}'].iloc[i]) == str:
            place[i][0] += f'{str(data[f'Unnamed: {cols_num[2]}'].iloc[i]).replace('\n', '')}'

    for i in range(len(name_work)):
        if '---' not in name_work[i][0]:
            name_work[i].append(name_work[i][0])
            number_class[i].append(number_class[i][0])
            place[i].append(place[i][0])
            continue
        name_work[i] = re.split(r'[-]{2,}', name_work[i][0])
        number_class[i] = re.split(r'[- ]+', number_class[i][0])
        place[i] = re.split(r'[- ]+', place[i][0])
        if len(name_work[i]) == 1: name_work[i].append('')
        if len(number_class[i]) == 1: number_class[i].append('')
        if len(place[i]) == 1: place[i].append('')

    for i in range(0, len(name_work)):
        for j in range(2):
            if name_work[i][j] != '':
                table[i][j] = time[i] + name_work[i][j] + ' ' + number_class[i][j] + place[i][j]
    shedule = ''
    if week == 'up':
        for i in table:
            shedule += i[0]
            shedule += '\n\n'
    elif week == 'down':
        for i in table:
            shedule += i[1]
            shedule += '\n\n'

    return shedule
