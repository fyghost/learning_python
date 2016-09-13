import re

def email_regex(corp):
    regex = r'([0-9a-zA-Z\_\.]+\@corp.com$)'
    return re.compile(regex)
    
if __name__ == '__main__':
    str = 'someone@gmail.com'
    regex = r'^[0-9a-zA-Z]+?'
    re_mail = re.compile(regex)
    re_match = re_mail.match(str)
    print(re_match.groups(1))