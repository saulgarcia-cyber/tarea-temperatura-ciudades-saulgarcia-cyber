import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

# Ver tipos de datos de las columnas
print(df.dtypes)

# Convertir la columna 'Datetime' a tipo datetime
df['Datetime'] = pd.to_datetime(df['Datetime'])

# Establecer la columna 'Date' como índice del DataFrame
df.set_index('Datetime', inplace=True)

# Crear funcion para convertir de grados Kelvin a Celsius
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

# Copiar el DataFrame original y nombralo df_celsius
df_celsius = df.copy()

# Convertir las temperaturas de cada ciudad de Kelvin a Celsius usando la funcion creada
df_celsius[['San Diego', 'Phoenix', 'Toronto']] = df_celsius[['San Diego', 'Phoenix', 'Toronto']].applymap(kelvin_to_celsius)

# Analisis
phoenix_data = df_celsius['Phoenix']

# Temperatura mínima
min_temp = phoenix_data.min()
min_temp_date = phoenix_data.idxmin()

# Temperatura máxima
max_temp = phoenix_data.max()
max_temp_date = phoenix_data.idxmax()

# Temperatura promedio
avg_temp = phoenix_data.mean()

print(f"El día con la temperatura mínima en Phoenix fue: {min_temp_date}")
print(f"La temperatura mínima registrada en Phoenix fue de: {min_temp:.2f} °C")
print(f"El día con la temperatura máxima en Phoenix fue: {max_temp_date}")
print(f"La temperatura máxima registrada en Phoenix fue de: {max_temp:.2f} °C")
print(f"La temperatura promedio durante 2016 en Phoenix fue de: {avg_temp:.2f} °C")

# Graficar la temperatura de Phoenix durante el año 2016
plt.figure(figsize=(20, 10))
plt.scatter(df_celsius.index, df_celsius['Phoenix'], label='Phoenix')
plt.title('Temperatura en Phoenix durante 2016')
plt.xlabel('Fecha')
plt.ylabel('Temperatura (°C)')
plt.legend()
plt.grid()
plt.savefig("temperatura_phoenix_2016.png")
plt.show()

# Exportar el DataFrame modificado a un nuevo archivo CSV
df_celsius.to_csv("temperatura_celsius.csv")
