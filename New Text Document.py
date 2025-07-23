import os

print(os.getcwd())

v = 'yes' if os.path.exists('data.csv') else 'no'

print(v)
