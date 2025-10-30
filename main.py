import subprocess

with open("blocklists.txt", 'r') as infile:
    lines = infile.readlines()
 
print(lines)
  
for index, line in enumerate(lines):
    command = f"curl {line}"
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)

    with open('processed.txt', 'a') as file:
        file.write(result.stdout)

    print(f"Processed {index} / {len(lines)}.")
    