# imports
import os
from datetime import datetime

# limpa tela
os.system('cls || clear') or None

# output
print(datetime.today().strftime('%A, %B %d, %Y, %H:%M:%S'))