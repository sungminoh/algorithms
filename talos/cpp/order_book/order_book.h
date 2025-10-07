#ifndef TALOS__CODING_INTERVIEW__CPP__ORDER_BOOK__ORDER_BOOK_H
#define TALOS__CODING_INTERVIEW__CPP__ORDER_BOOK__ORDER_BOOK_H

#include <string>
#include <vector>

namespace order_book {


enum class Side {kBid, kOffer};

enum class Action {kNew, kChange, kDelete};

struct OrderUpdate  {
    std::string order_id;
    Side side;
    double price;
    double size;
    Action action;
};

struct PriceLevel {
    double price;
    double size;
};

class OrderBook {
public:
    virtual void OnMessage(const OrderUpdate& order_update);

    virtual std::vector<PriceLevel> Bids();

    virtual std::vector<PriceLevel> Offers();

private:
};


}  // namespace order_book

#endif // TALOS__CODING_INTERVIEW__CPP__ORDER_BOOK__ORDER_BOOK_H
