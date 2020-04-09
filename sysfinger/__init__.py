



def run():
    print(' YES. SYSFINGER ')

import platform as p
import uuid
import hashlib
#import netifaces

def basic():
    sb = []
    sb.append(p.node())
    sb.append( ''.join([ x for x in p.architecture() ]) )
    sb.append(p.machine())
    sb.append(p.processor())
    sb.append(p.system())
    sb.append(str(uuid.getnode())) # MAC address
    text = '.'.join(sb)
    return text


def eth0():
    print(' eth 0')
    #netifaces.interfaces() # returns e.g. ['lo', 'eth0', 'tun2']
    #return netifaces.ifaddresses('eth0')[netifaces.AF_LINK]


def basic_md5():
    unhashed =basic()
    #    md5 = hashlib.md5().encode('utf8')
    #md5.update(text)
    #return md5.hexdigest().encode('utf8')
    # hash here
    return unhashed