format_Map = {
    "%s": "STRING",
    "%d": "NUMBER",
    "%n": "NUMBER",
}
def filterString(string: str, format: format_Map):
    try: 
        print(format_Map[format])
    except:
        return ('IMPROPER FORMAT_MAP (" {f} " does not exist)').format(f = str(format))
    a = ""
    for x in string:
        if format_Map[format] == "STRING" and not x.isalpha():
            continue
        elif format_Map[format] == "NUMBER" and not x.isdigit():
            continue
        a += x
    return a
