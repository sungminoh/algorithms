using NUnit.Framework;

namespace fact
{
    public class FactorialTest
    {
        [Test]
        public void TestFactorial()
        {
            Assert.AreEqual(1, Fact.Factorial(0));
            Assert.AreEqual(1, Fact.Factorial(1));
            Assert.AreEqual(2, Fact.Factorial(2));
            Assert.AreEqual(6, Fact.Factorial(3));
        }
    }
}