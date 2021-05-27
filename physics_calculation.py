
def mechanical_word_value(f, s):
    w = f * s
    return w
print(mechanical_word_value(2.5,5))


def potential_energy(m, g, h):
    p_energy = m * g * h
    return p_energy

print(potential_energy(1,2,3))

def kinnetic_energy(v, m):
    k_energy = 0.5 * m * v ** 2
    return k_energy

print(kinnetic_energy(1, 10))

def pressure(f ,s):
    p_value = f / s
    return p_value

print(pressure(3,5))

def electrodynamic_force(b, i, l):
    ed_force_value = b * i * l
    return ed_force_value

print(electrodynamic_force(2,3,5))

def electromagnetic_vave_lenght(c , f):
    e_v_m = c / f
    return e_v_m

print(electromagnetic_vave_lenght(299792458, 1000))
