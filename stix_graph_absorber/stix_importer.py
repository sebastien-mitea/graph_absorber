class Graph_absorber:
    def __init__(self, blob) -> None:
        """Returns list of dictionaries"""
        self.blob=blob

    def keep(self, *funcs):
        """Returns elements that match all functions in *funcs"""
        data = self.blob
        for func in funcs:
            data = [d for d in data if func(d)]
        return Graph_absorber(data)

    def head(self, n):
        """Returns n first elements"""
        return Graph_absorber([self.blob[i] for i in range(n)])

    def tail(self, n):
        """Returns n last elements"""
        return Graph_absorber([self.blob[-i] for i in range(1, n+1)])

    def select(self, *keys):
        """Returns only elements with key in *keys"""
        return Graph_absorber([{k: d[k] for k in keys} for d in self.blob])

    def mutate(self, **kwargs):
        """Edit the value of key by applying func, for all key: func pair"""
        data = self.blob
        for key, func in kwargs.items():
            for i in range(len(data)):
                data[i][key] = func(data[i])
        return Graph_absorber(data)
    
    def sort(self, key, reverse=False):
        """Sort by key"""
        return Graph_absorber(sorted(self.blob, key=key, reverse=reverse))

    def collect(self):
        """Return instance of the data object"""
        return self.blob
