def check():
    try:
        with open(r"files\firsttime.txt","r") as a:
            if a.read().strip()=="True":
                return True
            else:
                return False
    except FileNotFoundError:
        with open(r"files\firsttime.txt","w") as a:
            a.write("True")
            return True