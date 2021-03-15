class Codec:
    def __init__(self):
        self.uid = -1
        self.d = defaultdict(lambda:-1)
        
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.uid += 1
        self.d[str(self.uid).zfill(8)] = longUrl
        return 'http://tinyurl.com/' + str(self.uid).zfill(8)

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.d[shortUrl[-8:]]