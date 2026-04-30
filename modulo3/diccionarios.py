ventas_region = {
    "Norte": {"Q1": 90, "Q2": 120, "Q3": 150, "Q4": 200},
    "Sur": {"Q1": 70, "Q2": 100, "Q3": 140, "Q4": 160},
    "Centro": {"Q1": 60, "Q2": 130, "Q3": 180, "Q4": 190}
}

# ventas_region["Centro"]["Q1"]
for region, ventas in ventas_region.items():
    total = sum(ventas.values())
    print(region, total)

#para la región con mayores ventas
region_top = max(
    ventas_region,
    key=lambda r: sum(ventas_region[r].values())
)
print("Región con más ventas:", region_top)

#Acumular ventas trimestre
totales_trimestre = {"Q1": 0, "Q2": 0, "Q3": 0, "Q4": 0}

for ventas in ventas_region.values():
    for trimestre, valor in ventas.items():
        totales_trimestre[trimestre] += valor

print(totales_trimestre)

#Porcentajes por región
total_general = sum(
    sum(ventas.values()) for ventas in ventas_region.values()
)

porcentajes = {
    region: (sum(ventas.values()) / total_general) * 100
    for region, ventas in ventas_region.items()
}

print(porcentajes)

#Reporte ordenado
reporte = sorted(
    porcentajes.items(),
    key=lambda x: x[1],
    reverse=True
)

for region, porcentaje in reporte:
    print(region, porcentaje)