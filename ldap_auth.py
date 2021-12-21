from ldap3 import Server, Connection, ALL

def get_ldap(user_id, password):
    address = 'openldap.telechips.com'
    dn = f'uid={user_id},cn=RND Innovation Team,cn=RND Planning Group,ou=RND Center,ou=People,dc=telechips,dc=com'
    server = Server(address, get_info=ALL)
    conn = Connection(server, dn, password)

    if not conn.bind():
        print('error in bind', conn.result)
    else:
        print(conn.bind())

    conn.search('dc=telechips,dc=com', '(&(uid=B180093))', attributes=['cn', 'uid', 'givenName', 'sn', 'mail'])
    print(conn.entries)


get_ldap('B180093', 'infra4938hC!')
