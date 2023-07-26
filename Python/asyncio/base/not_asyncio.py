import time
def good_night():
    time.sleep(1)
    print('Good night')

def main():
    good_night()
    good_night()

print(f"start : {time.strftime('%X')}")
main()
print(f"end : {time.strftime('%X')}")
