class Sources:
    '''
    source class to define source objects
    '''
    def __init__(self, Source_id, name,  title, description):
        self.id = Source_id
        self.name = name 
        self.title = title
        self.description = description

class Articles:
    '''
    article class to define article objects
    '''
    def __init__(self, author, title, image_url, published_at)
        self.author = author 
        self.title = title
        self.image_url = image_url
        self.published_at = published_at