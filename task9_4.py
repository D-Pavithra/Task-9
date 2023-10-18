import re
def reg_exp(ip_string, pattern):
    if re.match(pattern, ip_string):
        return True
    else:
        return False
    
email_pattern = '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-z]{2,4}$'
bd_mob_pattern = '^\+8801[3-9]\d{8}$'
us_tele_pattern = '^\(\d{3}\) \d{3}-\d{4}$'
pswd_pattern = '^(?=.*[a-z](?=.*[A-Z])(>=.*\d)(?=.*[@#$%^&+=])[A-Za-z\d@#$%^&+=]{16}$)'

print(reg_exp,("adb@gmail.com", email_pattern))
print(reg_exp,("+88017134546678", bd_mob_pattern))
print(reg_exp,("(123) 897-234325", us_tele_pattern))
print(reg_exp,("ASdecvwe@#$", pswd_pattern))