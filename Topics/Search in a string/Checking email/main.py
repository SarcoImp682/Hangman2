def check_email(email):
    at_space = email.find("@")
    period_space = email.find(".")
    period_back = email.rfind('.')
    if '@.' in email or ' ' in email or '@' not in email or '.' not in email:
        return False
    elif at_space < period_space:
        return True
    elif at_space > period_back:
        return False
    else:
        return True
