import time

focus_time = int(input("Enter the number of minutes to focus: "))

break_time = int(input("Enter the number of minutes to break: "))

cycles = int(input("Enter cycle times: "))

def countdown(minutes):
    seconds = minutes * 60
    while seconds > 0:
        time_format = "{:02d}:{:02d}".format(seconds // 60, seconds % 60)
        print(time_format, end="\r")
        time.sleep(1)
        seconds -= 1

print("Start focus！")
for i in range(cycles):
    print(f"cycle {i + 1}")
    print("Focus time left:")
    countdown(focus_time)
    print("\a")
    if i == cycles - 1:
        print("Cycle finished!")
        break
    print("Time to break!")
    countdown(break_time)
    print("\a")
