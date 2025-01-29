# MyLibrary: Integrate .NET Libraries with Python

MyLibrary is a lightweight .NET library that provides essential mathematical operations, designed for seamless integration with Python using Python.NET. This repository demonstrates how to build a .NET library, use it in Python, and troubleshoot common issues during integration.

---

## Features

- **Mathematical Operations:**
  - Addition
  - Subtraction
  - Multiplication
  - Division (with zero-checking)
  - Power (using `Math.Pow`)
- Designed for compatibility with .NET 6 and Python.NET.
- Step-by-step instructions to set up and run.

---

## Getting Started

### Prerequisites

1. **.NET SDK 6.0 or higher**
   - [Download .NET SDK](https://dotnet.microsoft.com/en-us/download/dotnet/6.0)

2. **Python 3.x**
   - Ensure Python is installed and in your system PATH.

3. **Install Python.NET**
   - Install via pip:
     ```bash
     pip install pythonnet
     ```

---

### Build the Library

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/MyLibrary.git
   cd MyLibrary
   ```

2. Build the .NET library:
   ```bash
   dotnet build -c Release
   ```

The compiled library (`MyLibrary.dll`) will be located in the `bin/Release/net6.0` directory.

---

### Run with Python

Create a Python script (e.g., `use_mylibrary.py`) and include the following code:

```python
import pythonnet
pythonnet.load(runtime_config="path/to/MyLibrary.runtimeconfig.json")
import clr

def main():
    dll_path = "path/to/MyLibrary.dll"
    clr.AddReference(dll_path)

    from MyLibrary import MathOperations
    math_ops = MathOperations()

    print(f"Add(5, 7) = {math_ops.Add(5, 7)}")
    print(f"Multiply(5, 7) = {math_ops.Multiply(5, 7)}")
    print(f"Subtract(10, 3) = {math_ops.Subtract(10, 3)}")
    print(f"Divide(10, 2) = {math_ops.Divide(10, 2)}")
    print(f"Power(2, 3) = {math_ops.Power(2, 3)}")

if __name__ == "__main__":
    main()
```

Replace `path/to/MyLibrary.dll` and `path/to/MyLibrary.runtimeconfig.json` with the actual paths to your DLL and runtime configuration file.

Run the script:
```bash
python use_mylibrary.py
```

Expected output:
```
Add(5, 7) = 12
Multiply(5, 7) = 35
Subtract(10, 3) = 7
Divide(10, 2) = 5.0
Power(2, 3) = 8.0
```

---

## Troubleshooting

### Common Errors

- **`System.TypeLoadException`:** Ensure your project targets .NET 6 or higher and that `MyLibrary.runtimeconfig.json` is passed to `pythonnet.load()`.
- **Missing Methods in Python:** Verify methods are public in `MathOperations` and check available methods with:
  ```python
  print(dir(math_ops))
  ```

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contributions

Feel free to open issues or submit pull requests to improve the project!

