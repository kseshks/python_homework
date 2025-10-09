"""ДЗ2

Есть лог гита в виде того, что выдает команда git log (обрезан, это лишь начало)

commit 56494bb16b9dcdb82844275d3a4ff0b71e1b7290 (HEAD -> main, origin/main, origin/HEAD)
Merge: cca26c5 451e1a0
Author: Tim Hoffmann <2836374+timhoffm@users.noreply.github.com>
Date:   Tue Sep 30 17:21:33 2025 +0200

    Merge pull request #30619 from anntzer/step

    Include step info in str(scroll_event).

commit cca26c579b2365c4b8398d7d2f8528de1480077a
Merge: 8e2eb5d 23b9ffd
Author: Tim Hoffmann <2836374+timhoffm@users.noreply.github.com>
Date:   Tue Sep 30 17:20:24 2025 +0200

    Merge pull request #30620 from anntzer/dd

    Add --debug flag to python -mmatplotlib.dviread CLI.

вывести топ 5 самых плодовитых коммитеров в формате
email , количество коммитов"""
import re

log = open('git_log.txt').read().split('commit')[1:]

git_authors= {}

n = 0
for i in log:
    n+=1
    email_author = str(re.findall(r'<([^>]+)>', i))[2:-2]
    if email_author in git_authors:
        git_authors[email_author]+=1
    else:
        git_authors[email_author] = 1
    #print(n, i, email_author)

print('Рейтинг пользователей по количесву коммитов ')
n = 0
for email, count in sorted(git_authors.items(), key=lambda x: x[1], reverse=True)[:5]:
    n+=1
    print(f"{n}) {email}: {count}")
        
        
    

