def DetectSQLInjection(string):
    detect = ["SELECT", "FROM", "*"]
    s = str(string).lower()
    for a in detect:
        if s.find(str(a).lower()) >= 0:
            return True
    return False
