using System;

namespace MyLibrary
{
    public class MathOperations
    {
        public int Add(int a, int b)
        {
            return a + b;
        }

        public int Multiply(int a, int b)
        {
            return a * b;
        }

        public int Subtract(int a, int b)
        {
            return a - b;
        }

        public double Divide(int a, int b)
        {
            if (b == 0)
            {
                throw new ArgumentException("Division by zero is not allowed.");
            }
            return (double)a / b;
        }

        public double Power(double a, double b)
        {
            double result = 1;
            for (int i = 0; i < (int)b; i++)
            {
                result *= a;
            }
            return result;
        }
    }
}
