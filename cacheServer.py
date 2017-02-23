class CacheServer :

    def __init__(self,latency,capacity):
        super(, self).__init__()
        self.__latency = float(latency)
        self.__capacity = int(capacity)
