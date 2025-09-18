
import re

def bump_version(name):
    """Adds or increments _vNN version suffix before file extension."""
    # Check if filename already has a version suffix at the end
    # Pattern matches: _v followed by 1-2 digits, optionally followed by extension
    match = re.search(r"_v(\d{1,2})(\.[^.]+)?$", name)
    
    if match:
        # Extract version number and extension from the match
        ver, ext = match.groups()
        ext = ext or ""
        v_count = len(re.findall(r'_v\d+', name))
        
        # Determine new version format based on existing version length and count
        # If multiple versions exist and current is single digit, keep single digit
        # Otherwise, use zero-padded 2-digit format
        new_ver = f"{int(ver)+1}" if v_count > 1 and len(ver) == 1 else f"{int(ver)+1:02d}"
        
        # Replace the version suffix with the new incremented version
        return re.sub(r"_v\d{1,2}(\.[^.]+)?$", f"_v{new_ver}{ext}", name)
    else:
        # No existing version found, add _v01 before the extension
        # Split from right to handle multiple dots (e.g., backup.tar.gz)
        parts = name.rsplit('.', 3)  # Split into max 4 parts
        
        # If filename has dots and doesn't end with a dot, insert version before extension
        # Otherwise, just append _v01 to the filename
        return f"{parts[0]}_v01.{parts[3]}" if '.' in name and not name.endswith('.') else name + "_v01"

if __name__== "__main__":
    print("File Version Bumper\n==================")
    print("Examples: report.csv -> report_v01.csv, report_v1.csv -> report_v02.csv\n")
    while True:
        try:
            filename = input("Enter filename (or 'quit'): ").strip()
            if filename.lower() in ['quit', 'exit', 'q']:
                print("Goodbye!"); break
            if filename:
                new_filename = bump_version(filename)
                print(f"Original: {filename}\nUpdated:  {new_filename}\n")
        except (KeyboardInterrupt, Exception):
            print("Goodbye!"); break