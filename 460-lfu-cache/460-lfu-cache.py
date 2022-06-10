class LFUCache(object):

    def addFreq(self, key):
        freq = self.freq[key]
        self.freq[key] = freq + 1
        self.fk[freq].remove(key)
        if freq + 1 not in self.fk:
            self.fk[freq+1] = []
        self.fk[freq+1].append(key)
        if len(self.fk[freq]) == 0:
            del self.fk[freq]
            if freq == self.mi:
                self.mi = self.mi + 1


    def __init__(self, capacity):
        self.capacity = capacity
        self.mi = 0
        self.freq = {}  
        self.fk = {}  
        self.val = {}


    def get(self, key):
        if key in self.val:
            self.addFreq(key)
            return self.val[key]
        else:
            return -1


    def put(self, key, value):
        if self.capacity <= 0:
            return

        if key in self.val:
            self.val[key] = value
            self.addFreq(key)
            return

        if self.capacity < len(self.val)+1:
            minKey = self.fk[self.mi][0]
            self.fk[self.mi].remove(minKey)
            if len(self.fk[self.mi]) == 0:
                del self.fk[self.mi]
            del self.freq[minKey]
            del self.val[minKey]
        self.val[key] = value
        self.freq[key] = 1
        if 1 not in self.fk.keys():
            self.fk[1] = []
        self.fk[1].append(key)
        self.mi = 1
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)