import re
import unittest


def check_mail(mail):
    check_at = re.findall('^[^@]+@[^@]+$', mail)
    if (not check_at):
        print "no at"
        return False
    check_name = re.findall('^[a-z0-9"\.!,;_-]{1,128}@', check_at[0])
    if (not check_name):
        print "wrong name"
        return False
    name_dots = re.findall('(\.\.)', check_name[0])
    if name_dots:
        print "two dots"
        return False
    #print check_name[0][:-1]

    name_quot = re.findall('^[^"!,;]*("[^"]*?"[^"!,;]*?)*$',check_name[0][:-1])
    if (not name_quot):
        print "wrong quotes"
        return False
    domain_check = re.findall('@((?!-)[a-z0-9_-]+(?<!-)\.)+((?!-)[a-zA-Z0-9_-]+(?<!-))$', check_at[0])

    if (not domain_check):
        print "wrong domain"
        return False
    #print domain_check[0]
    domain_check_str = ' '.join(domain_check[0])
    domain_check_str1 =  domain_check_str.replace(' ', '')
    #print domain_check_str1
    domain_check_length = re.findall('.{1,256}$', domain_check_str1)
    #print type(domain_check_length)
    if (not domain_check_length):
       # print "domain length"
        return False
   # print(mail,"mail")
    return True


#
print check_mail('mterpugov@gmail.com')
print check_mail('mterpugov@d.')
print check_mail('mterpugov@d.c')
print check_mail('mterpugov@d.c.sad.asd.asd.asd')
print check_mail('to\"s\"sdf@d.c.sad.asd.asd.asd')
#print check_mail('dsgf"dfd,;!"sdg,fdfg@d.c.sad.asd.asd.asd')


