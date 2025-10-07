namespace orderbook
{
    /// <summary>
    ///     PriceLevel represents a price level with a total size.
    /// </summary>
    public class PriceLevel
    {
        public PriceLevel(double price, double size)
        {
            Price = price;
            Size = size;
        }

        public double Price { get; }
        public double Size { get; }
    }
}