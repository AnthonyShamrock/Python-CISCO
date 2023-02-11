time = {
    "min": 0,
    "hour": 0
}

endTime = {
    "days": 0,
    "min": 0,
    "hour": 0
}
def getDuration():
    try:
        return int(input("Event duration (minutes):\n"))
    except:
        print("Invalid input! Please only base10 characters!")
        return getDuration()

def getTime():
    try:
        i = input("Start Time (HH:MM):\n").split(":")
        time["hour"] = int(i[0])
        if len(i) == 1:
            def getMin():
                try:
                    i.append(int(input("Start Time (minutes):\n")))
                except:
                    getMin()
            getMin()
        time["min"] = int(i[1])
        return getDuration()
    except:
        print("Invalid input! Example: 12:45")
        return getTime()

def run():
    duration = getTime()

    if (time["hour"] + duration // 60) % 24 > 0:
        endTime["days"] = (time["hour"] + duration // 60) // 24

    endTime["min"] = (time["min"] + duration) % 60
    endTime["hour"] = (time["hour"] + ((time["min"] + duration) // 60)) % 24
    if endTime["days"] > 0:
        print("DD:HH:MM\n{:02d}:{:02d}:{:02d}".format(int(endTime["days"]), int(endTime["hour"]), int(endTime["min"])))
        return run()
    print("HH:MM\n{:02d}:{:02d}".format(int(endTime["hour"]), int(endTime["min"])))
    run()
run()