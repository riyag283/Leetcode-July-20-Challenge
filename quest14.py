def func(hour,minutes):
    hr = hour*60+minutes
    hr = hr%720
    mn = minutes%360
    hrh = hr*0.5
    mnh = mn*6
    a = abs(hrh-mnh)
    b = 360 - a
    return a if a<b else b

print(func(1,57))
