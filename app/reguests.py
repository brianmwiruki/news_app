import reguests
from .models import Sources, Articles

API_KEY, BASE_URL, SOURCE_API_KEY = None

def configure_request(app):
    global API_KEY , BASE_URL
    API_KEY = app.config['NEWS_API_KEY']
    BASE_URL = app.config['NEWS_API_BASE_URL']
    SOURCE_API_KEY = BASE_URL + 'source'

def get_sources():
     """
    Function that gets the json response to our url request
    """

    response = requests.get(SOURCE_API_KEY, params = {"apikey": API_KEY})

    data = response.json()
return data

def process_resource(data)

    all_resources = []

    for res in data['sources']:
        new_source = Sources(res['id'],res['name'],res['title'],res['description'])
        all_resources.append(new_source)
    return all_resources

def get_articles(articles):

    get_articles_url = BASE_URL.format(articles,API_KEY)

    with urllib.request.urlopen(get_articles_url) as url:
        

    


