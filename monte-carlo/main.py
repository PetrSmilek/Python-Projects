import numpy as np
import matplotlib.pyplot as plt

# Define the function to integrate
def func(x):
    return np.sin(x**2)

# Set the interval [a,b] and the number of samples
a,b = 0,np.sqrt(2*np.pi)
N = 10**6

# Generate the samples and evaluate function at each
x = np.random.uniform(a, b, N)

# Compute the mean and estimate the integral
mean = np.mean(func(x))
my_integral = (b-a) * mean
print("The Monte Carlo estimate for the integral is", my_integral)


# Plot the function and sample points if N is small
plt.figure(figsize=(6,5))
x_plot = np.linspace(a, b, 101)
y_plot = func(x_plot)
plt.plot(x_plot ,y_plot, 'y')

plt.title("Monte Carlo Method 1",fontdict={'fontweight':'bold', 'fontsize': 15})
plt.grid(True)
plt.plot([a,b,b,a,a],[0,0,mean, mean,0], color=(0,0.75,0))
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("Monte_Carlo_Method_1.png")
plt.show()

# Generate N uniform random points in [x_min, x_max]x[y_min, y_max]
N = 1500
x_min, x_max = 0, np.sqrt(2 * np.pi)
y_min, y_max = -1, 1

x = np.random.uniform(x_min, x_max, N)
y = np.random.uniform(y_min, y_max, N)

# Obtain the area
total = 0
for i in range(N):
    if y[i] > 0 and y[i] < func(x[i]):
        total += 1
    elif y[i] < 0 and y[i] > func(x[i]):
        total -= 1
    else:
        pass

rectangle_area = (x_max - x_min) * (y_max - y_min)
region_area = rectangle_area * total / N

print("The Monte Carlo estimate for the integral using method 2 is", region_area)

# If N < 2000 we plot graph of the function with points sorted into three area categories (null , positive, negative area contribution) for better visualization y=0 axis is plotted
if N < 2000:
    plt.figure(figsize=(6, 5))
    for i in range(N):
        x_plot = np.linspace(x_min, x_max, 101)
        y_plot = func(x_plot)
        plt.plot(x_plot, y_plot, 'y')
        plt.plot(np.linspace(x_min, x_max, 101), np.zeros(101), "k")  # y=0 line

        if y[i] > 0 and y[i] < func(x[i]):  # this is where different color coding is engaged.
            plt.plot(x[i], y[i], '.g')
        elif y[i] < 0 and y[i] > func(x[i]):
            plt.plot(x[i], y[i], '.r')
        else:
            plt.plot(x[i], y[i], '.b')

    plt.title("Monte Carlo Method 2", fontdict={'fontweight': 'bold', 'fontsize': 15})
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.savefig("Monte_Carlo_Method_2.png")
    plt.show()