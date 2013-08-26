from loader.models import NationalArchive, StateArchive, CountyArchive

with open('nfeat') as nfeat:
    sn = {i.strip() for i in nfeat.readlines()}
with open('sfeat') as sfeat:
    ss = {i.strip() for i in sfeat.readlines()}
with open('cfeat') as cfeat:
    sc = {i.strip() for i in cfeat.readlines()}

ss = ss - sn

nfeats = [NationalArchive.objects.filter(feature=i) for i in sn]
nfeats = [i[0] for i in nfeats if i]
sfeats = [StateArchive.objects.filter(feature=i) for i in ss]
sfeats = [i[0] for i in sfeats if i]
cfeats = [CountyArchive.objects.filter(feature=i) for i in sc]
cfeats = [i[0] for i in cfeats if i]

features = set()

features.update(nfeats)
features.update(sfeats)
features.update(cfeats)

with open('featmodels','w') as featmodels:
    for i in features:
        print(i.model,file=featmodels)

