import pandas as pd
from cleantam import core 

data = {
    'Producto': ['Café ', 'Té de Limón', 'Alfajor Jorgito'],
    'Precio Venta': ['1.500,50', '2.300,00', '$ 800,25'],
    'Fecha': ['20/01/2026', '21/01/2026', '22/01/2026']
}

df = pd.DataFrame(data)

print("--- Antes ---")
print(df)
print(df.dtypes)

df.latam.limpiar_headers()
df.latam.a_float('precio_venta')
df.latam.normalizar_texto('producto')

print("\n--- Después ---")
print(df)
print(df.dtypes)