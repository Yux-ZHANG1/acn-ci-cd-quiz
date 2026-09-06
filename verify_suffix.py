import os

suffix = os.environ.get("SUFFIX", "")

print("==============================")
print(f"Suffix: {suffix}")
print("==============================")

if not suffix:
    print("ERROR: suffix is empty!")
    exit(1)

print(f"Suffix validated successfully: {suffix}")
