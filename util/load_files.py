from loader.models import CountyArchive, StateArchive, NationalArchive, CountyEquiv, StateEquiv
from yaml import dump, CDumper, load, CLoader
with open('files.txt') as files:
    files = [i.strip().strip('/.') for i in files.readlines() if i.find('.zip') >= 0]
with open('statefiles.yaml') as statefiles:
    states = load(statefiles, Loader=CLoader)
with open('countyfiles.yaml') as countyfiles:
    counties = load(countyfiles, Loader=CLoader)
with open('nationfiles.yaml') as nationfiles:
    nation = load(nationfiles, Loader=CLoader)
county_archives = {}
skipped = set()
for ccode, filenames in counties.items():
    for filename in filenames:
        if not CountyEquiv.objects.filter(code=ccode):
            skipped.add(ccode)
            continue
        county_archives[ccode] = CountyArchive( 
            feature = filename[14:-4],
            extent = CountyEquiv.objects.get(code=ccode)
        )


state_archives = {}
for scode, filenames in states.items():
    for filename in filenames:
        state_archives[scode] = StateArchive(
            feature = filename[11:-4],
            extent = StateEquiv.objects.get(code=scode)
        )

nation_archives = [
    NationalArchive(
        feature = filename[11:-4]
    ) 
    for filename in nation
]

print(skipped)

def _save(things):
    for thing in things:
        try:
            thing.save()
        except:
            print(thing.feature)
            raise
def saveall():
    global county_archives
    global state_archives
    global nation_archives
    _save(county_archives.values())
    _save(state_archives.values())
    _save(nation_archives)
saveall()
