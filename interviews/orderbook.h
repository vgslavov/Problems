#include <map>
#include <string>
#include <vector>

class OrderBookCollection {
public:
    OrderBookCollection() = default;

    void addOrderBook(const std::string& ticker) {
        if (d_ticker2index.find(ticker) != d_ticker2index.end()) {
            throw std::runtime_error(
                "Order book already exists for ticker: " + ticker);
        }

        // Creates a new OrderBook and init it with the ticker
        d_orderBooks.emplace_back(ticker);
        d_ticker2index[ticker] = d_orderBooks.size() - 1;
    }

    OrderBook& getOrderBook(const std::string& ticker) {
        auto it = d_ticker2index.find(ticker);
        if (it == d_ticker2index.end()) {
            throw std::runtime_error(
                "Order book not found for ticker: " + ticker);
        }

        return d_orderBooks[it->second];
    }

    bool addOrder(
            const std::string& ticker,
            size_t orderId,
            OrderBook::OrderType side,
            double price,
            int quantity)
    {
        OrderBook& orderBook = getOrderBook(ticker);

        return orderBook.addOrder(orderId, side, price, quantity);
    }

    bool removeOrder(
            const std::string& ticker,
            size_t orderId)
    {
        OrderBook& orderBook = getOrderBook(ticker);

        return orderBook.removeOrder(orderId);
    }

    bool orderExecuted(
            const std::string& ticker,
            size_t orderId,
            int quantity)
    {
        OrderBook& orderBook = getOrderBook(ticker);

        return orderBook.orderExecuted(orderId, quantity);
    }
private:
    std::vector<OrderBook> d_orderBooks;
    std::map<std::string, size_t> d_ticker2index;
};

class OrderBook {
public:
    enum class OrderType {
        BUY,
        SELL
    };

    OrderBook(const std::string& ticker)
    : d_ticker(ticker)
    {}

    bool addOrder(
            size_t orderId,
            OrderType side,
            double price,
            int quantity)
    {
        if (side != OrderType::BUY && side != OrderType::SELL) {
            throw std::runtime_error("Invalid order type");
        }

        d_orders.emplace_back(orderId, side, price, quantity);
        return true;
    }

    bool removeOrder(size_t orderId) {
        auto it = d_orderToIndex.find(orderId);
        if (it == d_orderToIndex.end()) {
            return false; // Order not found
        }

        // TODO: inefficient?
        d_orders.erase(d_orders.begin() + it->second);
        d_orderToIndex.erase(it); // Remove from map 
        for (size_t i = it->second; i < d_orders.size(); ++i) {
            d_orderToIndex[d_orders[i].orderId()] = i; // Update indices
        }

        return true;
    }

    bool orderExecuted(size_t orderId, int quantity) {
        auto it = d_orderToIndex.find(orderId);
        if (it == d_orderToIndex.end()) {
            return false; // Order not found
        }

        Order& order = d_orders[it->second];
        if (order.quantity() < quantity) {
            return false; // Not enough quantity to execute
        }

        order.setQuantity(order.quantity() - quantity);

        if (order.quantity() == 0) {
            removeOrder(orderId); // Remove order if quantity is zero
        }

        return true;
    }

private:
    std::string d_ticker;
    std::vector<Order> d_orders;
    std::map<size_t, size_t> d_orderToIndex;
    // sort?
    std::vector<PriceLevel> d_priceLevels; 
};

class Order {
public:
    Order(size_t orderId, OrderBook::OrderType side, double price, int quantity)
    : d_orderId(orderId)
    , d_side(side)
    , d_price(price)
    , d_quantity(quantity)
    {}

    size_t orderId() const { return d_orderId; }
    OrderBook::OrderType side() const { return d_side; }
    double price() const { return d_price; }
    int quantity() const { return d_quantity; }
    void setQuantity(int quantity) { d_quantity = quantity; }

private:
    size_t d_orderId;
    OrderBook::OrderType d_side;
    double d_price;
    int d_quantity;

};

class PriceLevel {
public:
    PriceLevel(double price)
    : d_price(price)
    {}

    double price() const { return d_price; }
    void addOrder(size_t orderId) { d_orders.push_back(orderId); }
    void removeOrder(size_t orderId) {
        auto it = std::find(d_orders.begin(), d_orders.end(), orderId);
        if (it != d_orders.end()) {
            d_orders.erase(it);
        }
    }
    const std::vector<size_t>& orders() const { return d_orders; }
private:
    double d_price;
    std::vector<size_t> d_orders; // Order IDs
};