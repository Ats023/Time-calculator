def add_time(time, duration, day=False):
    new_time=''
    days=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    start_time, meridiem=time.split()
    start_hr, start_min= start_time.split(':')

    if meridiem=='AM':
        start_hr=int(start_hr) if start_hr!='12' else 0
        start_time=start_hr*60 + int(start_min)
    elif meridiem=='PM':
        start_hr=(12+int(start_hr)) if start_hr!='12' else int(start_hr)
    
    start_time=int(start_hr)*60 + int(start_min)
    dur_hr, dur_min=duration.split(':')
    dur_time=int(dur_hr)*60+int(dur_min)
    res_time=start_time+dur_time
    new_hr, new_min=(res_time//60)%24, res_time%60

    if new_hr>=12:
        meridiem='PM'
    else:
        meridiem='AM'
    new_min=new_min if new_min>9 else '0'+str(new_min)
    day_num=int(dur_hr)//24 if int(start_hr)-new_hr<=0 else int(dur_hr)//24 + 1
    new_hr=(res_time//60)%12 if (res_time//60)%12!=0 else 12

    if day_num==0:
        day_count=''
    elif day_num==1:
        day_count=' (next day)'
    elif day_num>1:
        day_count=' (' + str(day_num) + ' days later)'

    if (day):
        day=day.capitalize()
        index=(days.index(day)+day_num)%7
        new_time=':'.join((str(new_hr), str(new_min))) + ' ' + meridiem + ', ' + days[index] + day_count
    else:
        new_time=':'.join((str(new_hr), str(new_min))) + ' ' + meridiem + day_count
    return new_time

res=add_time("8:16 PM", "466:02", "tuesday")
print(res)