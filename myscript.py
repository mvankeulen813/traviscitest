def hello_world(myvar):
    if myvar == 4:
        print("hello!")
        return True
    return False

def run_script():
    assert hello_world(4) == True
    
run_script()
