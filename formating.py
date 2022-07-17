# textStringLog = ""

def clearlog(inputString,var):
    textStringLog = "".join(inputString)
    print("1: " + textStringLog)
    # print("Inter: " + textStringLog)
    textStringLog = textStringLog.replace(' from', '')

    textStringLog = textStringLog.replace('user ', '', 1)
    textStringLog = textStringLog.replace(' via', '', 1)
    textStringLog = textStringLog.replace(' for', '', 1)
    textStringLog = textStringLog.replace('to romon network', 'romon_network', 1)
    print("2: " + textStringLog)
    if var == 1:
        textStringLog = textStringLog.replace(' ', '_', 1)

    # print("Exit: " + textStringLog)
    # inputString = textStringLog.strip().split(" ")
    # print("Data tools: " + textStringLog)
    print("ClearLog: " + textStringLog)
    return textStringLog
