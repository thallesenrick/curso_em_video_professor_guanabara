from time import sleep
import emoji
for c in range(10, -1, -1):
    print('\033[1;34m', c)
    sleep(0.5)
print(emoji.emojize('\033[1;31m'':boom::tada:BUM!:boom::tada:', use_aliases=True))
print(emoji.emojize('\033[1;32m'':boom::tada:BUM!:boom::tada:', use_aliases=True))
print(emoji.emojize('\033[1;33m'':boom::tada:POOW!:boom::tada:', use_aliases=True))