



def run():
    print(' YES SYSFINGER ')

import platform as p
import uuid
import hashlib
#import netifaces

def basic( md5=False ):
    """
    Fingerprint of the current operating system/platform.
    If md5 is True, a digital fingerprint is returned.
    """
    sb = []
    sb.append(p.node())
    sb.append(p.architecture()[0])
    sb.append(p.architecture()[1])
    sb.append(p.machine())
    sb.append(p.processor())
    sb.append(p.system())
    sb.append(str(uuid.getnode())) # MAC address
    text = '_'.join(sb)
    if md5:
        md5 = hashlib.md5()
        md5.update(text)
        return md5.hexdigest().encode('utf8')
    else:
        return text


def eth0():
    print(' eth 0')
    #netifaces.interfaces() # returns e.g. ['lo', 'eth0', 'tun2']
    #return netifaces.ifaddresses('eth0')[netifaces.AF_LINK]


