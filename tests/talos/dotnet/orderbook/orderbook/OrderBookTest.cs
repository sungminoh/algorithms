using NUnit.Framework;

namespace orderbook
{
    public class OrderBookTest
    {
        private OrderBook _orderBook;

        [SetUp]
        public void Setup()
        {
            _orderBook = new OrderBook();
        }

        [TearDown]
        public void TearDown()
        {
            _orderBook = null;
        }

        [Test]
        public void TestOneBid()
        {
            var orderUpdate1 = new OrderUpdate("1", Side.Bid, 100.00, 10.0,
                Action.New);
            _orderBook.OnMessage(orderUpdate1);
            Assert.AreEqual(1, _orderBook.Bids().Count, "one bid");
            Assert.AreEqual(100.0, _orderBook.Bids()[0].Price, "bid size");
            Assert.AreEqual(10.0, _orderBook.Bids()[0].Size, "bid size");
        }

        [Test]
        public void TestBidUpdate()
        {
            var orderUpdate1 = new OrderUpdate("1", Side.Bid, 100.00, 10.0,
                Action.New);
            _orderBook.OnMessage(orderUpdate1);
            var orderUpdate2 = new OrderUpdate("1", Side.Bid, 100.00, 7.0,
                Action.Change);
            _orderBook.OnMessage(orderUpdate2);
            Assert.AreEqual(1, _orderBook.Bids().Count, "one bid");
            Assert.AreEqual(100.0, _orderBook.Bids()[0].Price, "bid[0] size");
            Assert.AreEqual(7.0, _orderBook.Bids()[0].Size, "bid[0] size");
            var orderUpdate3 = new OrderUpdate("1", Side.Bid, 100.00, 0.0,
                Action.Delete);
            _orderBook.OnMessage(orderUpdate3);
            Assert.AreEqual(0, _orderBook.Bids().Count, "no bids");
        }

        [Test]
        public void TestMultipleBids()
        {
            var orderUpdate1 = new OrderUpdate("1", Side.Bid, 100.00, 10.0,
                Action.New);
            _orderBook.OnMessage(orderUpdate1);
            var orderUpdate2 = new OrderUpdate("2", Side.Bid, 101.00, 7.0,
                Action.New);
            _orderBook.OnMessage(orderUpdate2);
            var orderUpdate3 = new OrderUpdate("3", Side.Bid, 100.00, 5.0,
                Action.New);
            _orderBook.OnMessage(orderUpdate3);
            Assert.AreEqual(2, _orderBook.Bids().Count, "two levels");
            Assert.AreEqual(101.0, _orderBook.Bids()[0].Price, "bid[0] price");
            Assert.AreEqual(7.0, _orderBook.Bids()[0].Size, "bid[0] size");
            Assert.AreEqual(100.0, _orderBook.Bids()[1].Price, "bid[1] price");
            Assert.AreEqual(15.0, _orderBook.Bids()[1].Size, "bid[1] size");
        }

        [Test]
        public void TestMultipleOffers()
        {
            var orderUpdate1 = new OrderUpdate("1", Side.Offer, 100.00, 10.0,
                Action.New);
            _orderBook.OnMessage(orderUpdate1);
            var orderUpdate2 = new OrderUpdate("2", Side.Offer, 101.00, 7.0,
                Action.New);
            _orderBook.OnMessage(orderUpdate2);
            var orderUpdate3 = new OrderUpdate("3", Side.Offer, 100.00, 5.0,
                Action.New);
            _orderBook.OnMessage(orderUpdate3);
            Assert.AreEqual(2, _orderBook.Offers().Count, "two levels");
            Assert.AreEqual(100.0, _orderBook.Offers()[0].Price, "offer[0] price");
            Assert.AreEqual(15.0, _orderBook.Offers()[0].Size, "offer[0] size");
            Assert.AreEqual(101.0, _orderBook.Offers()[1].Price, "offer[1] price");
            Assert.AreEqual(7.0, _orderBook.Offers()[1].Size, "offer[1] size");
        }

        [Test]
        public void TestOrderChangeDelete()
        {
            var orderUpdate1 = new OrderUpdate("1", Side.Offer, 100.00, 10.0,
                Action.New);
            _orderBook.OnMessage(orderUpdate1);
            var orderUpdate2 = new OrderUpdate("1", Side.Offer, 101.00, 7.0,
                Action.Change);
            _orderBook.OnMessage(orderUpdate2);
            Assert.AreEqual(1, _orderBook.Offers().Count, "one offers");
            Assert.AreEqual(101.0, _orderBook.Offers()[0].Price, "offer[0] price");
            Assert.AreEqual(7.0, _orderBook.Offers()[0].Size, "offer[0] size");

            var orderUpdate3 = new OrderUpdate("1", Side.Offer, 0.0, 0.0,
                Action.Delete);
            _orderBook.OnMessage(orderUpdate3);
            Assert.AreEqual(0, _orderBook.Offers().Count, "no offers");
        }
    }
}