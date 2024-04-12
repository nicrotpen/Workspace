import matplotlib.pyplot as plt

#valores= [n for n in range(0,5001)]
valores=list(range(5001))
cub= [n**3 for n in valores]

fig, ax = plt.subplots()

ax.plot(valores, cub)

plt.show()