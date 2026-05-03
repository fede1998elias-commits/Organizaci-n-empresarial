import pandas as pd
import matplotlib.pyplot as plt
import os

# ── Carga de datos ──────────────────────────────────────────────────────────
df = pd.read_csv("datos/ventas.csv", parse_dates=["fecha_venta"])
df["ingreso"] = df["cantidad"] * df["precio"]

# ── Ventas totales ──────────────────────────────────────────────────────────
total = df["ingreso"].sum()
print(f"=== Ventas totales ===")
print(f"  ${total:,.2f}\n")

# ── Producto más vendido (por unidades) ────────────────────────────────────
ventas_por_producto = df.groupby("producto")["cantidad"].sum().sort_values(ascending=False)
print("=== Unidades vendidas por producto ===")
print(ventas_por_producto.to_string())
print(f"\n  Producto más vendido: {ventas_por_producto.idxmax()} "
      f"({ventas_por_producto.max()} unidades)\n")

# ── Ventas por mes ──────────────────────────────────────────────────────────
df["mes"] = df["fecha_venta"].dt.to_period("M")
ventas_mes = df.groupby("mes")["ingreso"].sum()
print("=== Ingresos por mes ===")
for mes, valor in ventas_mes.items():
    print(f"  {mes}: ${valor:,.2f}")

# ── Gráfico de evolución mensual ────────────────────────────────────────────
os.makedirs("resultados", exist_ok=True)

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(
    ventas_mes.index.astype(str),
    ventas_mes.values,
    marker="o",
    linewidth=2,
    color="#2563EB",
    markersize=7,
)
ax.fill_between(
    ventas_mes.index.astype(str),
    ventas_mes.values,
    alpha=0.15,
    color="#2563EB",
)
ax.set_title("Evolución de ventas mensuales", fontsize=14, fontweight="bold", pad=15)
ax.set_xlabel("Mes", fontsize=11)
ax.set_ylabel("Ingresos ($)", fontsize=11)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"${x:,.0f}"))
ax.grid(axis="y", linestyle="--", alpha=0.5)
plt.xticks(rotation=30, ha="right")
plt.tight_layout()

output_path = "resultados/evolucion_mensual.png"
plt.savefig(output_path, dpi=150)
print(f"\nGráfico guardado en: {output_path}")
