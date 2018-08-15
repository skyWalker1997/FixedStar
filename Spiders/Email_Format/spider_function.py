import re

Email = []

def func(content):
    pattern_Email = re.compile(u"email'.*?data-id=.*?fl'>(.*?)</div>", re.S)
    result_Email = re.findall(pattern_Email, content)

    i = 4
    for r_Email in result_Email:
        temp = str(r_Email.encode('utf-8').replace("\n\t\t\t\t", ''))
        t_email = temp.strip()
        Email.append(t_email)
    return Email