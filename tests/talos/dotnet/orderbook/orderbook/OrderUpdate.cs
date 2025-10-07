namespace orderbook
{
    /// <summary>
    ///     OrderUpdate represents a change to an individual order.
    /// </summary>
    public class OrderUpdate
    {
        public OrderUpdate(string orderId, Side side, double price, double size, Action action)
        {
            OrderId = orderId;
            Side = side;
            Price = price;
            Size = size;
            Action = action;
        }

        public string OrderId { get; }
        public Side Side { get; }
        public double Price { get; }
        public double Size { get; }
        public Action Action { get; }
    }
}