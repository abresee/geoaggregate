from urllib.request import urlopen
from json import loads

def _call(call_type, id_str):
	eia_url="http://api.eia.gov/{t}?api_key=F4A37BD0D3E8D3ADC5E0D6671D2CB5FE&{t}_id={i}".format(t=call_type, i=id_str)
	return loads(urlopen(eia_url).read().decode('utf-8'))

def category(category_id):
	return _call("category", category_id)

def series(series_id):
	return _call("series", series_id)



