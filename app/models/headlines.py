class Headlines:
    '''
    Class to define the instances of new headlines
    '''
    
    def __init__(self,id,name,author,title,description,url,urlToImage,publishedAt,content):
    
        self.id = id
        self.name = name 
        self.author = author
        self.title = title
        self.description = description
        self.url = url 
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content 