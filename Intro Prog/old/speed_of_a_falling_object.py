#Variable input and Math library import
import math
mass=float(input('What is the mass of the object in Kilograms? :'))
gravity=float(input('What is the Gravity in m/^2 ? '))
time=float(input('What is the amount of time the object is falling? '))
fluid_density=float(input('What is the Desnsity of the fluid the object is falling through?'))
cross_sectional=float(input('What is the cross sectional area in m^2 ? '))
drag_constant=float(input('What is the drag constant? 1.1 for cylander, and 0.5 for a sphere '))

#Value of inner c calculations
inner_c= (1/2) * fluid_density * cross_sectional * drag_constant

print(f'Your inner c value is : {inner_c:.3f}')

velocity= float(math.sqrt((mass*gravity)/inner_c) * (1-math.exp(((-1*(math.sqrt(mass*gravity*inner_c)))/mass)*time)))

print(f'Your velocity after {time} is : {velocity}')