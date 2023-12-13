import matplotlib.pyplot as plt

# Dados para o eixo x_2 e y_2 (100000 s/i)
x = [0, 10, 20, 30, 40, 50]
y = [0.00, 2.06, 4.10, 6.16 , 7.86, 9.85]

# Dados para o eixo x_2 e y_2 (100000 c/i)
x_2 = [0, 10, 20, 30, 40, 50]
y_2 = [0.00, 1.97, 3.89, 5.80, 7.63, 9.62]

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
plt.title('Conflitos em transações (100.000)')

# Adicionar uma legenda
plt.legend()

# Exibir o gráfico
plt.show()
