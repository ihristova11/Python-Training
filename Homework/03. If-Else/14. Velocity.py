velocity = float(input())
if velocity <= 10:
    print('slow')
elif 10.0 < velocity <= 50:
    print('average')
elif 50.0 < velocity <= 150:
    print('fast')
elif 150.0 < velocity <= 1000:
    print('ultra fast')
elif velocity > 1000:
    print('extremely fast')