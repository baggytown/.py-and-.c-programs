import pandas as pd

# Create a sample Series with custom string labels
data = [10, 20, 30, 40]
labels = ['alpha', 'beta', 'gamma', 'delta']
s = pd.Series(data, index=labels)

# 1. Access by explicit label using .loc
val_label = s.loc['beta']  # Returns 20

# 2. Access by integer position using .iloc
val_pos = s.iloc[1]        # Returns 20 (the second element)

# 3. Standard brackets (shortcut, but use with caution)
val_bracket = s['beta']    # Returns 20
/