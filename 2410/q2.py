def read_data():
    result = {}
    with open("atoms.txt") as f:
        for l in f:
            fields = l.split()
            result[fields[0]] = float(fields[1])
    return result
def m_mass(molecule):
    atom_mass = read_data()
    mass = 0
    while molecule:
        n = 1
        skip = 1
        a=molecule[0]
        if len(molecule) > 1 and molecule[1].isdigit():
            n = int(molecule[1])
            skip = 2
        molecule = molecule[skip:]
        mass = mass + n*atom_mass[a]
    return mass

print(m_mass("H2O"))
print(m_mass("H2SO3"))
print(m_mass("CH4"))
