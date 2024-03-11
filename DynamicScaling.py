class DynamicScaler:
    def __init__(self):
        self.min = None
        self.max = None

    def update_range(self, new_data):
        if self.min is None or self.max is None:
            self.min = self.max = new_data
        else:
            self.min = min(self.min, new_data)
            self.max = max(self.max, new_data)

    def scale(self, data):
        if self.min == self.max:  # Avoid division by zero
            return 0  # or 127, or another appropriate value for this edge case
        return round(((data - self.min) * 127) / (self.max - self.min))
    

# Example usage with negative values
scaler = DynamicScaler()
data_points = [30, -10, 0, 1, 10, 30, 300,100,-100]
for data in data_points:
    scaler.update_range(data)
    print(f"{data}: {scaler.scale(data)}")