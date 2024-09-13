# Atur cara mengira luas permukaan kon.
# Betulkan ralat dalam kod Python ini.

import math
pi = 3.142

def dapat_jejari_tinggi():
    a = float(input("Masukkan jejari: "))
    b = float(input("Masukkan tinggi: "))
    return (a, b)

def kira_luas_permukaan_kon(r, h):
    luas_permukaan_kon = (pi * h) * (r + maths.sqrt(r**2 + h**2))
    return round(luas_permukaan_kon, 2)

def main():
    (x, y) = dapat_jejari_tinngi()
    luas_permukaan_kon = kira_luas_permukaann_kon(x, y)
    print(f"luas permukaan kon = {luas_permukaan_kon:.2f}")

# Don't change the code below!
if __name__ == "__main__":
    main()
