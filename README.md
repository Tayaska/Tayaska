#include <iostream>
#include <vector>
#include <algorithm>

class Order {
public:
    Order(int orderId, const std::string& customerName, const std::string& product, double price)
        : orderId(orderId), customerName(customerName), product(product), price(price) {}

    void displayOrder() const {
        std::cout << "Order ID: " << orderId << "\n";
        std::cout << "Customer: " << customerName << "\n";
        std::cout << "Product: " << product << "\n";
        std::cout << "Price: $" << price << "\n\n";
    }

    double getPrice() const {
        return price;
    }

    int getOrderId() const {
        return orderId;
    }

private:
    int orderId;
    std::string customerName;
    std::string product;
    double price;
};

class OrderManagementSystem {
public:
    void addOrder(const Order& order) {
        orders.push_back(order);
        std::cout << "Order added successfully.\n\n";
        updateSystemInfo();  // Оновлено інформацію про систему
    }

    bool removeOrder(int orderId) {
        auto it = std::remove_if(orders.begin(), orders.end(),
            [orderId](const Order& order) { return order.getOrderId() == orderId; });

        bool orderRemoved = (it != orders.end());
        orders.erase(it, orders.end());
        if (orderRemoved) {
            std::cout << "Order with ID " << orderId << " removed successfully.\n";
            updateSystemInfo();  // Оновлено інформацію про систему
        }
        else {
            std::cout << "Failed to remove order with ID " << orderId << ". Order not found.\n";
        }
        return orderRemoved;
    }

    const Order* findOrderById(int orderId) const {
        auto it = std::find_if(orders.begin(), orders.end(),
            [orderId](const Order& order) { return order.getOrderId() == orderId; });

        if (it != orders.end()) {
            return &(*it);
        }
        else {
            return nullptr;
        }
    }

    void displayOrders() const {
        if (orders.empty()) {
            std::cout << "No orders available.\n\n";
            return;
        }

        std::cout << "List of Orders:\n";
        for (const auto& order : orders) {
            order.displayOrder();
            std::cout << "--------------------------------\n"; // Роздільник між замовленнями
        }

        std::cout << "Total Price for all Orders: $" << calculateTotalPrice() << "\n\n";
    }

    void displaySystemInfo() const {
        std::cout << "Order Management System Information:\n";
        std::cout << "Number of Orders: " << orders.size() << "\n";
        std::cout << "--------------------------------\n";
    }

    // Новий метод для підрахунку середньої ціни всіх замовлень
    double calculateAveragePrice() const {
        if (orders.empty()) {
            return 0.0;
        }

        double total = calculateTotalPrice();
        return total / orders.size();
    }

private:
    double calculateTotalPrice() const {
        double total = 0.0;
        for (const auto& order : orders) {
            total += order.getPrice();
        }
        return total;
    }

    void updateSystemInfo() const {
        std::cout << "System information updated.\n\n";
    }

    std::vector<Order> orders;
};

int main() {
    OrderManagementSystem orderSystem;

    // Додавання замовлень для демонстрації
    Order order1(1466373, "Lina Kostenko", "Notes of a Ukrainian hermit", 350);
    Order order2(2432240, "Taras Shecvhenko", "Kobzar", 600);
    Order order3(8690433, "Andrzej Sapkowski", "The Witcher", 470);
    Order order4(1924754, "Agatha Christie", "Death on the Nile", 235);

    orderSystem.addOrder(order1);
    orderSystem.addOrder(order2);
    orderSystem.addOrder(order3);
    orderSystem.addOrder(order4);

    // Виведення списку замовлень
    orderSystem.displayOrders();
    std::cout << "--------------------------------\n"; // Роздільник між замовленнями

    // Тест на видалення замовлення
    if (orderSystem.removeOrder(1466373)) {
        std::cout << "Order with ID 1466373 removed successfully.\n\n";
        std::cout << "--------------------------------\n"; // Роздільник між замовленнями
    }
    else {
        std::cout << "Failed to remove order with ID 1466373. Order not found.\n\n";
    }

    // Тест на пошук замовлення за ідентифікатором
    const Order* foundOrder = orderSystem.findOrderById(2432240);
    if (foundOrder != nullptr) {
        std::cout << "Order with ID 2432240 found:\n";
        foundOrder->displayOrder();
        std::cout << "--------------------------------\n"; // Роздільник між замовленнями
    }
    else {
        std::cout << "Order with ID 2432240 not found.\n";
    }

    // Виведення середньої ціни всіх замовлень
    std::cout << "Average Price for all Orders: $" << orderSystem.calculateAveragePrice() << "\n";

    return 0;
}
