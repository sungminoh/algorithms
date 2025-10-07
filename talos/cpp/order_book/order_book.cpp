#include "order_book.h"

#include <vector>

namespace order_book {


void OrderBook::OnMessage(const OrderUpdate& order_update) {
}

std::vector<PriceLevel> OrderBook::Bids() {
    return std::vector<PriceLevel>();
}

std::vector<PriceLevel> OrderBook::Offers() {
    return std::vector<PriceLevel>();
}


}  // namespace order_book
