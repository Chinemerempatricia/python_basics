filename = input("Enter a filename (e.g. document.pdf, image.png, script.py):")

parts = filename.split('.')

if len(parts) > 1:
    print("File Extension:",
parts[-1])
else:
    print("No file extension found.")

