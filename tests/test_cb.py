# $Id$

## PycURL module
import pycurl

## Callback function invoked when body data is ready
def body(buf):
    print buf
    return len(buf)

## Callback function invoked when header data is ready
def header(buf):
    print buf
    return len(buf)


c = pycurl.init()
c.setopt(pycurl.URL, 'http://www.python.org/')
c.setopt(pycurl.WRITEFUNCTION, body)
c.setopt(pycurl.HEADERFUNCTION, header)
c.setopt(pycurl.NOPROGRESS, 1)
c.setopt(pycurl.FOLLOWLOCATION, 1)
c.setopt(pycurl.MAXREDIRS, 5)
c.perform()
c.setopt(pycurl.URL, 'http://curl.haxx.se/')
c.perform()
c.cleanup()
