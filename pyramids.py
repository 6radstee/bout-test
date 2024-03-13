#normal pyramid 

print("\nNormal pyramid")
for i in range(6):
    z='* '
    z=z*i
    print (f'{z:^10}')

#inverted pyramid
print ('\nInverted pyramid')
for i in range(5):
    x=' *'
    x=x*(5-i)
    print (f'{x:^10}')

print("Left sided pyramid")
for i in range (5):
    x='* '
    x=x*i
    print (f'{x:<10}')


print("Right sided pyramid")
for i in range (5):
    x='* '
    x=x*i
    print (f'{x:>10}')