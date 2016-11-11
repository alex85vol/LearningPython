# -*- coding: utf8 -*-
'''
@author: vl
'''

resume_collection = []

resume = {
    'name_surname': u"Василь Лупиніс",
    'years_old': 30,
    'languages': {"Python", "C/C++", "Java", "JavaScript"},
    'english_level': u"високий",
    'hobby': [u"футбол", u"волейбол", u"баскетбол"]
}

resume_collection.append(resume)

resume = {
    'name_surname': u"Петро Іванов",
    'years_old': 25,
    'languages': {"C/C++", "Java", "JavaScript"},
    'english_level': u"високий",
    'hobby': [u"футбол", u"волейбол", u"баскетбол", u"плавання"]
}

resume_collection.append(resume)

for resume in resume_collection:
    print u'Ім\'я та прізвище:', resume['name_surname']
    print u'Вік:', resume['years_old']
    languages = list(resume['languages'])

    print u'Мови програмування:'
    for l in range(len(languages)):
        print l + 1, ' ', languages[l]

    print u'Рівень англійської:', resume['english_level']
    print u'Хобі:', ", ".join(resume['hobby'])
    print ''    