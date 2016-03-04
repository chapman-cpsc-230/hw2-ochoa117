
t = 0
T_tea = 100.0
T_air = 20.0
k = 0.055
print "Temperature of the air: 20"
print "Number of minutes: 20"
print "Minute Temperature"
while t < 20:
    print t, "%0.1f" %T_tea
    T_tea -= k*(T_tea - T_air)
    t += 1
