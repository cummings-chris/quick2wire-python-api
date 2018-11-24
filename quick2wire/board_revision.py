def revision():
    try:
        with open('/proc/cpuinfo','r') as f:
            for line in f:
                if line.startswith('Revision'):
# This line needs to be fixed to detect the new rPi 3 B+
                    return 1 if line.rstrip()[-1] in ['2','3'] else 2
            else:
                return 0
    except:
        return 0

