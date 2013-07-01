import requests

class Google_Translate(object):

    base = 'https://www.googleapis.com'
    path = '/language/translate/'
    
    version = 'v2'
    options = {}
    
    def __init__(self, key):
        self.options['key'] = key 
        
    def call(self, options, end_point=None):
        """ Send HTTP GET request and return response
        
        keyword arguments:
        options   -- HTTP query parameters and values
        end_point -- applicable for detect method 
        
        """
        
        url = self.get_url(end_point)
        r = requests.get(url, params=self.options)
        return r.text
        
    def translate(self, **kwargs):
        """ Translate from one language to another
        
        keyword arguments:
        q           -- text to translate | required
        target      -- language to translate to | required
        source      -- language to translate from | optional
        format      -- determine if response is html or text | optional
        callback    -- specify a javascript function to handle query results |optional
        prettyprint -- if true results returned in human readable form | optional
        
        """
        self.options.update(kwargs)
        return self.call(self.options)
        
    def detect(self, **kwargs):
        """ Detect language from a string 
        
        keyword arguments:
        q           -- text to translate | required
        callback    -- specify a javascript function to handle query results |optional
        prettyprint -- if true results returned in human readable form | optional
        
        """
        self.options.update(kwargs)
        return self.call(self.options, 'detect')
        
    def discover(self, **kwargs):
        """ Discover supported languages
        
        keyword arguments:
        target      -- language to translate to | required
        callback    -- specify a javascript function to handle query results |optional
        prettyprint -- if true results returned in human readable form | optional
        
        """
        self.options.update(kwargs)
        return self.call(self.options, 'languages')
    
    def get_url(self, end_point=None):
        """ Assemple URL for request
        """
        
        url = self.base + self.path + self.version
        
        if end_point is not None:
            url += "/%s/" % end_point

        return url
    
    def set_version(self, num):
        self.version = "v%d" % num