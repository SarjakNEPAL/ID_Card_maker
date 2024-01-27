from condata import *
cursor.execute("DELETE FROM users")
link.commit()
cursor.execute("DELETE FROM user_info")
link.commit()
# cursor("DELETE FROM user_img")
# link.commit()