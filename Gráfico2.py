import matplotlib.pyplot as plt

# Dados para o eixo x e y (10.000 c/i)
x = [0, 10, 20, 30, 40, 50]
y = [0.00, 0.23, 0.44, 0.68, 0.86, 1.04]

# Dados para o eixo x e y (10000 s/i)
x_2 = [0, 10, 20, 30, 40, 50]
y_2 = [0.00, 1.88, 3.70, 5.49, 7.31, 9.26]

# Criar o gráfico de linhas
plt.plot(x, y, label='Com idx', marker='o', color="red") 
plt.plot(x_2, y_2, label='Sem idx', marker='o', color="blue") 

# Ajustar os intervalos dos eixos x e y
plt.xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) # Define os ticks no eixo x
plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) # Define os ticks no eixo y

# Adicionar rótulos aos eixos
plt.xlabel('Conflito (%)')
plt.ylabel('Tempo (s)')

# Adicionar título ao gráfico
plt.title('Conflitos em transações (10.000)')

# Adicionar uma legenda
plt.legend()

# Exibir o gráfico
plt.show()
