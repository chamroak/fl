
import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
csv_file = '/home/mehdi_ktb/Documents/FederatedLearning/codes/simpleFL/fl/stepwise_loss_client_1.csv'
df = pd.read_csv(csv_file)

# Plot column 2 (index 1) against column 3 (index 2)
x = df.iloc[:, 1]  # Step
y = df.iloc[:, 2]  # Loss

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x, y, marker='o', linestyle='-')
plt.xlabel('Step (Column 3)')
plt.ylabel('Loss (Column 2)')
plt.title('Loss vs. Step')
plt.grid(True)
plt.tight_layout()
plt.show()
