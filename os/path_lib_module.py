from pathlib import Path
# p = Path('/')
# for subdir in p.iterdir():
#     if subdir.is_dir():
#         print(subdir)

p = Path.cwd()
files = p.rglob('*.txt')
for f in files:
    print(f)
    #f.open("+a")
    #f.write_text("My Name is Vrishabh")

# Reading from a file
with (p / 'sample.txt').open('r') as file:
    content = file.read()
    print(content)

# Writing to a file
with (p / 'output.txt').open('w') as file:
    file.write("Hello, Vrishabh!")