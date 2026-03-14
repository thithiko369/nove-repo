# Carregar os dados preparados
df = pd.read_csv('clientes-v3-preparado.csv')
print(df.head().to_string())

# --- Histograma Simples ---
plt.hist(df['salario'])
plt.show()

# --- Histograma com Parâmetros ---
plt.figure(figsize=(10, 6))
plt.hist(df['salario'], bins=100, color='green', alpha=0.8)
plt.title('Histograma - Distribuição de Salários')
plt.xlabel('Salário')
plt.xticks(ticks=range(0, int(df['salario'].max())+2000, 2000))
plt.ylabel('Frequência')
plt.grid(True)
plt.show()
