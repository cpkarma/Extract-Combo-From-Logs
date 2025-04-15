import re

def test(filename, output_file):
    pat = r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})[|:]([^\s|:]+)'
    cred = []
    
    try:
        with open(filename, 'r', encoding='utf-8') as file, open(output_file, 'a', encoding='utf-8') as out:
            for line in file:
                xmc = re.findall(pat, line)
                if xmc:
                    hell = xmc[-1]
                    combo = f"{hell[0]}:{hell[1]}"
                    cred.append(combo)
                    out.write(combo + "\n")
                    out.flush()
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []
    
    return cred

print("Extract Combo From Logs\n")
filename = input("File Name: ")
output_file = "extracted_combo.txt"

result = test(filename, output_file)

if result:
    print("Extracted:")
    for cred in result:
        print(cred)
else:
    print("No email cred found or extraction failed.")

print(f"cred saved to {output_file}")