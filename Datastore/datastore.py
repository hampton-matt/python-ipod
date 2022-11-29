import redis
import pickle
from functools import lru_cache

class Datastore:

    _instance = None
    r = redis.Redis(decode_responses=True)

    def __new__(cls):
        if cls._instance is None:
          cls._instance = super(Datastore, cls).__new__(cls)
        return cls._instance
            
    # Theme
    def set_theme(self, theme):
        self.r.set("theme", theme)
    
    def get_theme(self):
        return self.r.get("theme")

test1 = Datastore()
print(test1.get_theme())