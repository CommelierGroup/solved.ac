def absolute(A_time) :
   return A_time["hour"]*60 + A_time["min"]

def relative(absolute_min) :
    rel_hour = int(absolute_min / 60)
    rel_min = absolute_min % 60
    return {"hour" : rel_hour, "min" : rel_min}

def sub_time(absolute_min) :
    if absolute_min < 45 :
        return absolute_min -45 + 1440
    else :
        return absolute_min - 45

set_time = {"hour" : 0, "min" : 0}
user_input = input().split()
set_time["hour"] = int(user_input[0])
set_time["min"] = int(user_input[1])

ab_min = absolute(set_time)
subbed_ab_min = sub_time(ab_min)
fitted_rel_time = relative(subbed_ab_min)
print(fitted_rel_time["hour"], fitted_rel_time["min"])
