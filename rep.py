# -*- coding: utf-8 -*-

import pywikibot

site = pywikibot.Site('ja', 'wikipedia')
asite=pywikibot.site.APISite('ja','wikipedia',user='Anakabot')

def sec001():
    for i,title in enumerate(list1):
        print(str(i)+' -- rest'+str(len(list1)-i)+'--'+str(title))
        try:
            page = pywikibot.page.BasePage(site, title)
            text = page.get(force=True, get_redirect=True)
            old_text=text
            for r in oldnew:
                old=r[0]
                new=r[1]
                old1_text=text
                if old in text:
                    print(old)
                    print(new)
                    val1=input('1：save　2：pass')
                    if int(val1)==1:
                        text = text.replace(old,new)
                    else:
                        pass
            page.text = text
            pywikibot.diff.PatchManager(old_text,text).print_hunks()
            if old_text==text:
                pass
            else:
                val6=input('1：save　2：pass')
                if int(val6)==1:
                    page.save(summary)
                    print('Ok')
                else:
                    print('No')
        except Exception as e:
            print(title, '—p',e)
    print('\nClose')

summary=""
# title_list ['コシツェ市電', 'バイオハザード (ゲーム)']
list1=[]
# two-dimensional array.[["{{Main2|","{{For2"],[{{Main|,"{{See2|"]]
oldnew=[]
sec001()