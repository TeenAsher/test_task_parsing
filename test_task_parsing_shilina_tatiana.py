# Test task for the Bewise.ai
# Tatiana Shilina
# Parsing from the csx file

import numpy as np
import pandas as pd
from natasha import NamesExtractor, MorphVocab, PER

FILE = 'copy_test_data - test_data.csv'
morph_vocab = MorphVocab()
extractor = NamesExtractor(morph_vocab)
reader = pd.read_csv(FILE, encoding='utf-8', on_bad_lines='skip')

def get_greetings(read):
    greeting = read.loc[(read.insight == 'greeting') & (read.role == 'client')]
    greetings = []
    for string in greeting.text:
        greetings.append(string)
    return greetings

def get_names(read):
    name = read.loc[(read.insight == 'name') & (read.role == 'client')]
    names = []
    for string in name.text:
        names.append(string)
    return names

def get_goodbyes(read):
    goodbye = read.loc[(read.insight == 'goodbye') & (read.role == 'client')]
    goodbyes = []
    for string in goodbye.text:
        goodbyes.append(string)
    return goodbyes

def get_manager_name(names):
    text = ''.join(names)
    matches = extractor(text)
    if not matches:
        print("no names found")
    else:
        name_list = []
        for x in matches:
            name_list.append(x.fact.first)
        for y in name_list:
            if y == None:
                name_list.remove(y)
        for y in name_list:
            if y == None:
                name_list.remove(y)
        for y in name_list:
            if y == None:
                name_list.remove(y)
        for y in name_list:
            if y == None:
                name_list.remove(y)
        return name_list

def check_manager(number, read):
    dialog = read.loc[(read.dlg_id == int(number))]
    words = ['greeting', 'name', 'goodbye']
    word_check = dialog.loc[dialog.insight.isin(words)]
    check = []
    for i in word_check.text:
        check.append(i)
    len_check = len(check)
    if len_check >= 3:
        print(f'\nМенеджер из диалога номер {number} прошел проверку')
    elif len_check < 3:
        print(f'\nМенеджер из диалога номер {number} НЕ прошел проверку')
    else:
        print('Nothing')


def main(reader):
    print('Изъятие реплик приветствия:')
    greetings = get_greetings(reader)
    for num, item in enumerate(greetings):
        print(num + 1, '-', item)
    print('\nИзъятие реплик, содержащих имена менеджеров и компаний:')
    names = get_names(reader)
    for num, item in enumerate(names):
        print(num + 1, '-', item)
    print('\nИзъятие реплик прощания:')
    goodbyes = get_goodbyes(reader)
    for num, item in enumerate(goodbyes):
        print(num + 1, '-', item)
    print('\nСписок имен менеджеров:')
    name = get_manager_name(names=get_names(reader))
    for num, item in enumerate(name):
        print(num + 1, '-', item)
    try:
        for num in range(0, 6):
            check_manager(num, reader)
    except Exception as e:
        print(e)
    print('\nКонец задания')

main(reader=reader)