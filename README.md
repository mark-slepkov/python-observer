# python-observer
A short library which is implements Observer pattern for any classes

Using
-----

```
from observer import observer
@observer
class Example(object):
    pass

def do_anything():
    print("anything is done")
    
example = Example()
example.on('some_event', do_anything)
example.trigger('some_event')
>>> anything is done
```
