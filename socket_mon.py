import psutil

def main():
    socket = psutil.net_connections(kind = 'inet')
    conn = {}
    for s in socket:
        if s.laddr and s.raddr and s.pid:
            if s.pid not in conn:
                conn[s.pid] = [s]
            else:
                conn[s.pid].append(s)

    sortpidlist = sorted(conn, key=lambda k: len(conn[k]), reverse = True)
    
    print '"pid","laddr","raddr","status"'
    for p in sortpidlist:
        connection = conn[p]
        for c in connection:
            print '"%s","%s@%s","%s@%s","%s"' % (c.pid, c.laddr[0], c.laddr[1], c.raddr[0], c.raddr[1], c.status)

if __name__ == '__main__':
    main()
