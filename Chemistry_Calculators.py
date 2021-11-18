x = 1
while True:
    System1 = (input("Solve Mass Defect (1) or Energy/Wavelength/Freqency (2): "))
    if System1 == "1":
        Nucleus = (float(input("Enter Mass Number: ")) * float(1.66054E-27)) - (float(input("Enter Electron Amount: ")) * float(9.10915E-31))
        Protons = (float(input("Enter Proton Amount: ")) * float(1.67262E-27)) + (float(input("Enter Neutron Amount: ")) * float(1.67495E-27))
        print("Nucleus Mass =", Nucleus), print("Proton Mass =", Protons), print("Mass Defect =", Nucleus - Protons)
    elif System1 == "2":
        System2 = (input("Solve for Energy (1), Wavelength (2), or Frequency (3): "))
        if System2 == "1":
            print("Energy = ", float(6.63E-34) * float(input("Enter Frequency (Example: 4.97e-33): ")))
        elif System2 == "2":
            print("Wavelength = ", float(3E8) / float(input("Enter Frequency (Example: 4.97e-33): ")),"m")
        elif System2 == "3":
            print("Frequency = ", float(3E8) / float(input("Enter Wavelength (Example: 4.0e-7): ")),"Hz")
        else:
            print("Please Select A Valid Number")
    else:
        print("Please Select A Valid Number")
    System3 = (input("Exit (1), or Restart (Enter)?: "))
    if System3 == "1":
        break
    elif System3 == "":
        None
else:
    print("Please Select A Valid Number")
