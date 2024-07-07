# Archivo: vlan_rango.py
vlan = int(input("1005,4096,1006: "))
if 1 <= vlan <= 1005:
    print("La VLAN corresponde al rango normal.")
elif 1006 <= vlan <= 4094:
    print("La VLAN corresponde al rango extendido.")
else:
    print("Número de VLAN fuera de rango.")
