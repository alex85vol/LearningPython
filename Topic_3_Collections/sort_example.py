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

resume = {
    'name_surname': u"Іван Петров",
    'years_old': 25,
    'languages': {"C/C++", "Java", "JavaScript"},
    'english_level': u"початковий",
    'hobby': [u"футбол", u"волейбол", u"баскетбол", u"плавання"]
}

resume_collection.append(resume)

english_levels = dict({u'початковий': 0, u'середній': 50, u'високий': 100})


def sort_by_english_level(resume):
    return english_levels[resume['english_level']]


print u'В порядку зростання'
resume_collection.sort(key=sort_by_english_level)

for resume in resume_collection:
    print u'Ім\'я та прізвище:', resume['name_surname']
    print u'Рівень англійської:', resume['english_level']
    print ''

print u'В порядку спадання'
resume_collection.sort(key=sort_by_english_level, reverse=True)

for resume in resume_collection:
    print u'Ім\'я та прізвище:', resume['name_surname']
    print u'Рівень англійської:', resume['english_level']
    print ''