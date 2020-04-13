# port.py

total = 0.0

#with open('Data/portfolio.csv', 'r') as f:
with open('Data/portfolio2.csv', 'r') as f:
    headers = next(f) # Skip a single line of input
    for line in f:
        line = line.strip() # Strip whitespaces
        parts = line.split(',')
        parts[0] = parts[0].strip('"')
        parts[1] = parts[1].strip('"')
        parts[2] = int(parts[2])
        parts[3] = float(parts[3])
        total += parts[2]*parts[3]
        #print(parts)
        #print(line)
print("Total cost: ", total)