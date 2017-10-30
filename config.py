CSRF_ENABLE = True
SECRET_KEY = 'you-will-never-know'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'http://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyopenID', 'url': 'https://www.myopenid.com'}
]
