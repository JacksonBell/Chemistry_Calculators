System1 = int(input("Solve Mass Defect (1) or Energy/Wavelength/Freqency (2): "))
if System1 == 1:
    Mnucleus = (float(input("Enter Mass Number: ")) * float(1.66054E-27)) - (float(input("Enter Electron Amount: ")) * float(9.10915E-31))
    Mprotons = (float(input("Enter Proton Amount: ")) * float(1.67262E-27)) + (float(input("Enter Neutron Amount: ")) * float(1.67495E-27))
    print("Mnucleus =", Mnucleus), print("Mprotons =", Mprotons), print("Mass Defect =", Mnucleus - Mprotons)
if System1 == 2:
    System2 = int(input("Solve for Energy (1), Wavelength (2), or Frequency (3): "))
    if System2 == 1:
        print("Energy = ", float(6.63E-34) * float(input("Enter Frequency (Example: 4.97E-33): ")))
    if System2 == 2:
        print("Wavelength = ", float(3E8) / float(input("Enter Frequency (Example: 4.97E-33): ")),"m")
    if System2 == 3:
        print("Frequency = ", float(3E8) / float(input("Enter Wavelength (Example: 4.0E-7): ")),"Hz")
    if System2 > 3:
        print("Error, No Operation Selected")
    if System2 < 1:
        print("Error, No Operation Selected")
input("Press Enter to Exit")
