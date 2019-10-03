import random
import os
prepositionDict = {"about":"over",
"above":"boven",
"across":"over",
"after":"na",
"against":"tegen",
"among":"onder",
"around":"rond",
"as":"als",
"at":"op",
"before":"voor",
"behind":"achter",
"below":"onder",
"beneath":"onder",
"beside":"naast",
"between":"tussen",
"beyond":"buiten/achter",
"but":"maar",
"by":"door",
"despite":"ondanks",
"down":"naar beneden",
"during":"gedurende/tijdens",
"except":"behalve",
"for":"voor",
"from":"uit/van",
"in":"in",
"inside":"binnen",
"into":"in",
"near":"nabij",
"next":"volgende",
"of":"van",
"on":"op",
"opposite":"tegenover",
"out":"uit",
"outside":"buiten",
"over":"over",
"per":"per",
"plus":"plus",
"round":"rond",
"since":"sinds",
"than":"dan",
"through":"via/door",
"until":"tot/totdat",
"to":"aan",
"toward":"in de richting van",
"under":"onder",
"unlike":"anders",
"until":"tot/totdat",
"up":"omhoog",
"via":"via",
"with":"met",
"within":"binnen",
"without":"zonder",
"according to":"volgens",
"because of":"vanwege",
"close to":"dicht bij",
"due to":"dankzij/door",
"except for":"met uitzondering van",
"far from":"verre van",
"inside of":"binnenin/in",
"instead of":"in plaats van",
"near to":"in de buurt van",
"next to":"naast",
"outside of":"buiten",
"prior to":"voorafgaande aan",
"as far as":"tot aan",
"as well as":"evenals",
"in addition to":"in aanvulling op",
"in front of":"voor",
"in spite of":"ondanks",
"on behalf of":"namens",
"on top of":"bovenop",

"this":"dit/deze",
"that":"dat/die",
"these":"deze",
"those":"die"}

if __name__ == "__main__":
    englishList = list(prepositionDict)
    increaseRate = round(len(englishList)/4)
    decreaseRate = round(increaseRate/2)
    if (os.name!='posix') and (os.name!='nt'):
        print("Unknown operating system! Will not clear window between words!")
        print("\n(clearing window is supported for posix-systems (such as Mac, Linux, other unix-based systems),\nas well as in nt-systems (Microsoft Windows))\n")

    while True:
        if os.name =='posix':
            os.system('clear')
        elif os.name == 'nt':
            os.system('cls')
        english = random.choice(englishList)
        dutch = set(prepositionDict[english].split('/'))
        answer = set(input(f'what is the dutch word for "{english}"? (If more than one answer, separate with\"/\")\n').lower().split('/'))
        if answer == {'exit'}:
            exit()
        if answer == dutch:
            print("that's correct!")
            if englishList.count(english)>1:
                for i in range(decreaseRate):
                    englishList.remove(english)
                    if not(englishList.count(english)>1):
                        break
        else:
            print(f"That's not correct...\nThe correct answer is: \"{'/'.join(dutch)}\"\n")
            for i in range(increaseRate):
                englishList.append(english)
        dummyResponse = input(f"press enter to continue\n")
        if dummyResponse == 'exit':
            exit()
