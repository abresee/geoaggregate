from urllib.request import urlopen
from json import loads,load,dump
import os
import matplotlib.pyplot as plt
class ApiConnection:
    cachename = 'apicache'
    
    def __init__(self):
        if os.path.exists(self.cachename):
            with open(self.cachename) as cache:
                self.cache = load(cache)
        else:
            self.cache = {}

    def save(self):
        with open(self.cachename,'w') as cache:
            dump(self.cache,cache,indent=True)

    def _call(self, call_type, id_str):
        eia_url="http://api.eia.gov/{t}?api_key=F4A37BD0D3E8D3ADC5E0D6671D2CB5FE&{t}_id={i}".format(t=call_type, i=id_str)
        return loads(urlopen(eia_url).read().decode('utf-8'))

    def _call_cache(self, call_type, id_str):
        key = call_type + str(id_str)
        if key in self.cache:
            return self.cache[key]
        else:
            cache_value = self._call(call_type, id_str)
            self.cache[key] = cache_value
            return cache_value

    def category(self, category_id):
        return self._call_cache("category", category_id)

    def series(self, series_id):
        return self._call_cache("series", series_id)

    def _get_data(self,series):
        d= series["series"][0]["data"]
        x=[int(i[0]) for i in d]
        y=[int(i[1]) for i in d]
        return x,y

    def plot_series(self,series_id):
        s=self.series(series_id)
        x,y=self._get_data(s)
        plt.plot(x,y)
if __name__ == "__main__":
    eia = ApiConnection()
