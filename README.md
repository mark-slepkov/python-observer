# python-observer
[![Build Status](https://travis-ci.org/mark-slepkov/python-observer.svg?branch=master)](https://travis-ci.org/mark-slepkov/python-observer) [![Join the chat at https://gitter.im/mark-slepkov/python-observer](https://badges.gitter.im/mark-slepkov/python-observer.svg)](https://gitter.im/mark-slepkov/python-observer?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

A short library which implements Observer pattern for any classes

Using
-----

``` python
from observer import observer
@observer
class Example(object):
    pass

def do_anything():
    print("anything is done")
    
example = Example()
example.on('some_event', do_anything)
example.trigger('some_event')
# "anything is done" will be printed here
```
