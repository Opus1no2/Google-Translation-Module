Google Translation Module
=========================
 
This is a minimalistic API client for Google Translation API

Usage:
------

```python

from client import Google_Translate

c = Google_Translate('YOUR API KEY')
c.discover()
                 
```

```python

from client import Google_Translate

c = Google_Translate('YOUR API KEY')
c.translate(q='This is a test'
            source='en',
            target='gl')
```

```python

from client import Google_Translate

c = Google_Translate('YOUR API KEY')
c.detect(q='This is a test')

```