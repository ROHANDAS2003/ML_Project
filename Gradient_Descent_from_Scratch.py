import numpy as np

# Step 1: Generate synthetic data
np.random.seed(0)
X = 2 * np.random.rand(100, 1)             # 100 data points, one feature (time)
y = 4 + 3 * X + np.random.randn(100, 1)    # True relation: y = 4 + 3x + noise

# Step 2: Add a bias (intercept) term to input
X_b = np.c_[np.ones((X.shape[0], 1)), X]   # Shape: (100, 2)

# Step 3: Initialize weights randomly
theta = np.random.randn(2, 1)              # Two weights: [intercept, slope]

# Step 4: Set hyperparameters
learning_rate = 0.1
n_epochs = 50
batch_size = 20
m = X_b.shape[0]                           # Total number of samples

# Step 5: Define the loss function (Mean Squared Error)
def compute_loss(X, y, theta):
    predictions = X.dot(theta)
    errors = predictions - y
    return np.mean(errors ** 2)

# Step 6: Train using mini-batch gradient descent
for epoch in range(n_epochs):
    # Shuffle data at the start of each epoch
    indices = np.random.permutation(m)
    X_b_shuffled = X_b[indices]
    y_shuffled = y[indices]
    
    for i in range(0, m, batch_size):
        # Create mini-batch
        X_batch = X_b_shuffled[i:i+batch_size]
        y_batch = y_shuffled[i:i+batch_size]
        
        # Predict and compute gradients
        predictions = X_batch.dot(theta)
        errors = predictions - y_batch
        gradients = (2 / batch_size) * X_batch.T.dot(errors)
        
        # Update weights
        theta = theta - learning_rate * gradients

    # Print loss after each epoch
    loss = compute_loss(X_b, y, theta)
    print(f"Epoch {epoch+1}, Loss: {loss:.4f}")

# Final weights after training
print("\nFinal learned weights (theta):")
print(theta)