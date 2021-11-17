System1 = int(input("Solve Mass Defect (1) or Energy/Wavelength/Freqency (2): "))
if System1 == 1:
    Nucleus = (float(input("Enter Mass Number: ")) * float(1.66054E-27)) - (float(input("Enter Electron Amount: ")) * float(9.10915E-31))
    Protons = (float(input("Enter Proton Amount: ")) * float(1.67262E-27)) + (float(input("Enter Neutron Amount: ")) * float(1.67495E-27))
    print("Nucleus Mass =", Nucleus), print("Proton Mass =", Protons), print("Mass Defect =", Nucleus - Protons)
if System1 == 2:
    System2 = int(input("Solve for Energy (1), Wavelength (2), or Frequency (3): "))
    if System2 == 1:
        print("Energy = ", float(6.63E-34) * float(input("Enter Frequency (Example: 4.97e-33): ")))
    if System2 == 2:
        print("Wavelength = ", float(3E8) / float(input("Enter Frequency (Example: 4.97e-33): ")),"m")
    if System2 == 3:
        print("Frequency = ", float(3E8) / float(input("Enter Wavelength (Example: 4.0e-7): ")),"Hz")
    if System2 > 3:
        print("Please Select A Valid Number")
    if System2 < 1:
        print("Please Select A Valid Number")
if System1 < 1:
    print("Please Select A Valid Number")
if System1 > 2:
    print("Please Select A Valid Number")
input("Press Enter to Exit")
