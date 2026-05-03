# Organización Empresarial — UTN

Trabajo Práctico de análisis de datos empresariales para la materia **Organización Empresarial** de la Universidad Tecnológica Nacional.

## Descripción

Este proyecto analiza datos de ventas de una empresa utilizando Python y pandas para obtener indicadores clave de desempeño (KPIs) y visualizaciones que apoyen la toma de decisiones gerenciales.

## Estructura del proyecto

```
organizacion-empresarial/
├── datos/
│   └── ventas.csv          # Dataset de ventas simuladas
├── scripts/
│   └── analisis_ventas.py  # Script principal de análisis
├── resultados/
│   └── evolucion_mensual.png  # Gráfico generado por el script
├── .gitignore
└── README.md
```

## Análisis realizados

- **Ventas totales**: ingresos acumulados del período analizado
- **Producto más vendido**: ranking por cantidad de unidades vendidas
- **Ventas por mes**: desglose mensual de ingresos
- **Evolución mensual**: gráfico de línea con tendencia de ventas

## Requisitos

```
Python >= 3.9
pandas
matplotlib
```

Instalar dependencias:

```bash
pip install pandas matplotlib
```

## Ejecución

```bash
python scripts/analisis_ventas.py
```

El gráfico de evolución mensual se guarda automáticamente en `resultados/evolucion_mensual.png`.

## Datos

El archivo `datos/ventas.csv` contiene 15 registros de ventas con las siguientes columnas:

| Columna      | Descripción                         |
|--------------|-------------------------------------|
| `producto`   | Nombre del producto vendido         |
| `cantidad`   | Unidades vendidas en la transacción |
| `precio`     | Precio unitario en pesos            |
| `fecha_venta`| Fecha de la venta (YYYY-MM-DD)      |

## Autores

Trabajo Práctico — UTN  
Materia: Organización Empresarial
