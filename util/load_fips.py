from loader import models
import yaml

with open('loader/fips.yaml') as fips_file:
    mapping = yaml.load(fips_file,yaml.CLoader)

for fips_code, place in mapping.items():
    if len(fips_code) == 2:
        m = models.StateEquiv(
            name = place,
            code = fips_code
        )

        if not models.StateEquiv.objects.filter(code=m.code):
            m.save()
skipped = set()

for fips_code, place in mapping.items():
    if len(fips_code) == 5:
        s_code = fips_code[:2]
        state = models.StateEquiv.objects.filter(code=s_code)

        if not state:
            skipped.add((fips_code,place))
            continue

        m = models.CountyEquiv(
            name = place,
            code = fips_code,
            parent = state[0]
        )

        if not models.CountyEquiv.objects.filter(code=m.code):
            m.save()


