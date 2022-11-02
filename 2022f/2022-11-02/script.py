import random
print(random.choice(range(100)))

from pathlib import Path
print(Path("README.md").resolve().read_text()[:50])

print("done")
