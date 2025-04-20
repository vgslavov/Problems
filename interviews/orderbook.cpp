#include <orderbook.h>

int main()
{
    OrderBookCollection orderBookCollection;
    orderBookCollection.addOrderBook("AAPL");
    orderBookCollection.addOrder("AAPL", 1, OrderBook::OrderType::BUY, 150.0, 100);
    orderBookCollection.addOrder("AAPL", 2, OrderBook::OrderType::SELL, 155.0, 50);
    orderBookCollection.orderExecuted("AAPL", 1, 50);
    orderBookCollection.removeOrder("AAPL", 2);

    return 0;
}