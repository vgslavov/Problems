#include <map>
#include <unordered_map>
#include <unordered_set>
#include <string>
#include <memory>
#include <optional>

using OrderID = uint64_t;
using Price = double;
using Quantity = int;
using Symbol = std::string;

enum class Side {
    BUY,
    SELL
};

// Stores metadata about an individual order
struct OrderMetadata {
    Price price;
    Side side;
    Quantity quantity;
    
    OrderMetadata(Price p, Side s, Quantity q) 
        : price(p), side(s), quantity(q) {}
};

// Represents aggregate liquidity at a single price point
class PriceLevel {
private:
    Price price;
    Quantity totalQuantity;
    std::unordered_set<OrderID> orderIds;
    
public:
    explicit PriceLevel(Price p) : price(p), totalQuantity(0) {}
    
    void addQuantity(OrderID orderId, Quantity qty) {
        orderIds.insert(orderId);
        totalQuantity += qty;
    }
    
    void removeQuantity(OrderID orderId, Quantity qty) {
        orderIds.erase(orderId);
        totalQuantity -= qty;
    }
    
    Quantity getTotalQuantity() const {
        return totalQuantity;
    }
    
    bool isEmpty() const {
        return totalQuantity == 0;
    }
    
    Price getPrice() const {
        return price;
    }
};

// Per-symbol order book with bid/ask price levels
class OrderBook {
private:
    Symbol symbol;
    
    // Order metadata for O(1) lookup during removes/executions
    std::unordered_map<OrderID, OrderMetadata> orderIdToMetadata;
    
    // Bids: highest price first (descending)
    std::map<Price, PriceLevel, std::greater<Price>> bidLevels;
    
    // Asks: lowest price first (ascending)
    std::map<Price, PriceLevel, std::less<Price>> askLevels;
    
public:
    explicit OrderBook(const Symbol& sym) : symbol(sym) {}
    
    // Process AddOrder message
    void addOrder(OrderID orderId, Side side, Price price, Quantity quantity) {
        // Store order metadata
        orderIdToMetadata.emplace(orderId, OrderMetadata(price, side, quantity));
        
        // Add to appropriate price level
        if (side == Side::BUY) {
            auto it = bidLevels.find(price);
            if (it == bidLevels.end()) {
                bidLevels.emplace(price, PriceLevel(price));
                it = bidLevels.find(price);
            }
            it->second.addQuantity(orderId, quantity);
        } else {
            auto it = askLevels.find(price);
            if (it == askLevels.end()) {
                askLevels.emplace(price, PriceLevel(price));
                it = askLevels.find(price);
            }
            it->second.addQuantity(orderId, quantity);
        }
    }
    
    // Process RemoveOrder message
    void removeOrder(OrderID orderId) {
        auto metaIt = orderIdToMetadata.find(orderId);
        if (metaIt == orderIdToMetadata.end()) return;
        
        const OrderMetadata& metadata = metaIt->second;
        
        // Remove from appropriate price level
        if (metadata.side == Side::BUY) {
            auto levelIt = bidLevels.find(metadata.price);
            if (levelIt != bidLevels.end()) {
                levelIt->second.removeQuantity(orderId, metadata.quantity);
                if (levelIt->second.isEmpty()) {
                    bidLevels.erase(levelIt);
                }
            }
        } else {
            auto levelIt = askLevels.find(metadata.price);
            if (levelIt != askLevels.end()) {
                levelIt->second.removeQuantity(orderId, metadata.quantity);
                if (levelIt->second.isEmpty()) {
                    askLevels.erase(levelIt);
                }
            }
        }
        
        orderIdToMetadata.erase(metaIt);
    }
    
    // Process OrderExecuted message
    void executeOrder(OrderID orderId, Quantity executedQty) {
        auto metaIt = orderIdToMetadata.find(orderId);
        if (metaIt == orderIdToMetadata.end()) return;
        
        OrderMetadata& metadata = metaIt->second;
        
        // Remove executed quantity from price level
        if (metadata.side == Side::BUY) {
            auto levelIt = bidLevels.find(metadata.price);
            if (levelIt != bidLevels.end()) {
                levelIt->second.removeQuantity(orderId, executedQty);
                if (levelIt->second.isEmpty()) {
                    bidLevels.erase(levelIt);
                }
            }
        } else {
            auto levelIt = askLevels.find(metadata.price);
            if (levelIt != askLevels.end()) {
                levelIt->second.removeQuantity(orderId, executedQty);
                if (levelIt->second.isEmpty()) {
                    askLevels.erase(levelIt);
                }
            }
        }
        
        // Update or remove order metadata
        metadata.quantity -= executedQty;
        if (metadata.quantity == 0) {
            orderIdToMetadata.erase(metaIt);
        }
    }
    
    // Query: Get best bid (highest buy price)
    std::optional<std::pair<Quantity, Price>> getBestBid() const {
        if (bidLevels.empty()) return std::nullopt;
        
        const auto& [price, level] = *bidLevels.begin();
        return std::make_pair(level.getTotalQuantity(), price);
    }
    
    // Query: Get best ask (lowest sell price)
    std::optional<std::pair<Quantity, Price>> getBestAsk() const {
        if (askLevels.empty()) return std::nullopt;
        
        const auto& [price, level] = *askLevels.begin();
        return std::make_pair(level.getTotalQuantity(), price);
    }
    
    // Query: Get inside market (best bid x best ask)
    std::pair<std::optional<std::pair<Quantity, Price>>,
              std::optional<std::pair<Quantity, Price>>> getInsideMarket() const {
        return {getBestBid(), getBestAsk()};
    }
    
    // Query: Get total liquidity for first N price levels
    Quantity getTotalLiquidity(Side side, int numLevels) const {
        Quantity total = 0;
        int count = 0;
        
        if (side == Side::BUY) {
            for (const auto& [price, level] : bidLevels) {
                if (count >= numLevels) break;
                total += level.getTotalQuantity();
                count++;
            }
        } else {
            for (const auto& [price, level] : askLevels) {
                if (count >= numLevels) break;
                total += level.getTotalQuantity();
                count++;
            }
        }
        
        return total;
    }
};

// Top-level collection managing all symbol order books
class OrderBookCollection {
private:
    std::unordered_map<Symbol, std::unique_ptr<OrderBook>> symbolToBook;
    
public:
    OrderBook* getOrCreateOrderBook(const Symbol& symbol) {
        auto it = symbolToBook.find(symbol);
        if (it == symbolToBook.end()) {
            auto book = std::make_unique<OrderBook>(symbol);
            auto ptr = book.get();
            symbolToBook[symbol] = std::move(book);
            return ptr;
        }
        return it->second.get();
    }
    
    OrderBook* getOrderBook(const Symbol& symbol) {
        auto it = symbolToBook.find(symbol);
        return (it != symbolToBook.end()) ? it->second.get() : nullptr;
    }
    
    // Message processing interface
    void processAddOrder(OrderID orderId, const Symbol& symbol, 
                        Side side, Price price, Quantity quantity) {
        auto* book = getOrCreateOrderBook(symbol);
        book->addOrder(orderId, side, price, quantity);
    }
    
    void processRemoveOrder(OrderID orderId, const Symbol& symbol) {
        auto* book = getOrderBook(symbol);
        if (book) {
            book->removeOrder(orderId);
        }
    }
    
    void processOrderExecuted(OrderID orderId, const Symbol& symbol, 
                             Quantity executedQty) {
        auto* book = getOrderBook(symbol);
        if (book) {
            book->executeOrder(orderId, executedQty);
        }
    }
};

/*
 * COMPLEXITY ANALYSIS:
 * 
 * Time Complexities:
 * - addOrder:          O(log p) where p = number of price levels
 * - removeOrder:       O(log p)
 * - executeOrder:      O(log p)
 * - getBestBid/Ask:    O(1)
 * - getInsideMarket:   O(1)
 * - getTotalLiquidity: O(n) where n = numLevels requested
 * 
 * Space Complexity:
 * - O(orders + price_levels)
 * 
 * KEY DESIGN CHOICES:
 * 
 * 1. std::map with custom comparators:
 *    - Bids use std::greater<Price> for descending order
 *    - Asks use std::less<Price> for ascending order
 *    - Provides O(log p) insert/delete and O(1) best price access
 * 
 * 2. std::unordered_map for order metadata:
 *    - O(1) lookup during removes/executions
 *    - Stores price, side, quantity per order
 * 
 * 3. std::unordered_set in PriceLevel:
 *    - Tracks which orders exist at each price
 *    - O(1) insertion/deletion
 * 
 * 4. Automatic price level cleanup:
 *    - Empty levels removed immediately
 *    - Minimizes memory and maintains clean book state
 */