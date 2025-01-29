import os
import sys

# Import Python.NET for .NET 6/7
import pythonnet
pythonnet.load()
import clr

def find_mylibrary_dll():
    """
    Attempts to find 'MyLibrary.dll' in typical project paths.
    Returns the absolute path if found, otherwise None.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Traverse up to 3 levels to find the project root
    search_roots = []
    current_dir = script_dir
    for _ in range(3):
        search_roots.append(current_dir)
        current_dir = os.path.dirname(current_dir)

    dll_name = "MyLibrary.dll"

    # Add common paths where the DLL might be located
    candidate_paths = []
    for root in search_roots:
        candidate_paths.append(os.path.join(root, "bin", "Release", "net6.0", dll_name))
        candidate_paths.append(os.path.join(root, "bin", "Debug", "net6.0", dll_name))
        # Add other paths if necessary
        # candidate_paths.append(os.path.join(root, "bin", "Release", "net7.0", dll_name))
        # candidate_paths.append(os.path.join(root, "bin", "Debug", "net7.0", dll_name))

    for path in candidate_paths:
        if os.path.exists(path):
            return os.path.abspath(path)

    return None

def main():
    # Find and load the MyLibrary.dll file
    dll_path = find_mylibrary_dll()
    if not dll_path:
        raise FileNotFoundError("Could not find 'MyLibrary.dll' in any of the standard paths.")

    print(f"Found DLL at: {dll_path}")

    pythonnet.load(runtime="net6") 
    clr.AddReference(dll_path)

    # Import the MathOperations class
    from MyLibrary import MathOperations

    # Create an instance of MathOperations
    math_ops = MathOperations()

    print(f"Add(5, 7) = {math_ops.Add(5, 7)}")
    print(f"Multiply(5, 7) = {math_ops.Multiply(5, 7)}")
    print(f"Subtract(10, 3) = {math_ops.Subtract(10, 3)}")
    print(f"Divide(10, 2) = {math_ops.Divide(10, 2)}")
    print(f"Power(2, 3) = {math_ops.Power(2, 3)}")

if __name__ == "__main__":
    main()

