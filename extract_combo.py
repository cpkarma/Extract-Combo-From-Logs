import re

def test(filename):
    pat = r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})\|([^\s|]+)'
    cred = []
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                xmc = re.findall(pat, line)
                if xmc:
                    hell = xmc[-1]
                    cred.append(f"{hell[0]}:{hell[1]}")
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []
    
    return cred
print("Extract Combo From Logs\n")
filename = input("File Name: ")

result = test(filename)

if result:
    print("Extracted:")
    for cred in result:
        print(cred)
else:
    print("No email cred found or extraction failed.")

yeh = "extracted_combo.txt"
with open(yeh, "w", encoding="utf-8") as f:
    for cred in result:
        f.write(cred + "\n")
print(f"cred saved to {yeh}")