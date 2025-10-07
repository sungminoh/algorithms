namespace fact
{
    internal class Fact
    {
        /// <summary>
        ///     Compute n factorial
        /// </summary>
        /// <param name="n">Offset in the sequence, should be greater than or equal to zero</param>
        /// <returns>Factorial of n</returns>
        public static int Factorial(int n)
        {
            if (n == 0) return 1;
            return n * Factorial(n - 1);
        }
    }
}