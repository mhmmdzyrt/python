def fun(s):
    # return True if s is a valid email, else return False
    s = list(s)
    if '@' not in s or '.' not in s:
        return False

    if s.count('@') > 1 or s.count('@') == 0:
        return False

    for i in s[:s.index('@')]:
        if i.isdigit() or i.isalpha() or i == '_' or i == '-':
            continue
        else:
            return False
    else:
        for i in s[s.index('@'):]:
            if i == '_':
                return False
        if len(s[:s.index('@')]) <= 0:
            return False

    if s.count('.') == 1 and len(s[s.index('.'):]) <= 4:
        return True


def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)