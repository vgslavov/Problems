#include <iostream>
#include <memory>

// abstract product
class Shape {
public:
    virtual void draw() = 0;
    virtual ~Shape() = default;

};

// concrete products
class Circle : public Shape {
public:
    void draw() override
    {
        std::cout << "drawing a circle" << std::endl;
    }
};

class Square : public Shape {
public:
    void draw() override
    {
        std::cout << "drawing a square" << std::endl;
    }

};

// abstract creator
class ShapeFactory {
public:
    virtual std::unique_ptr<Shape> create() = 0;
    virtual ~ShapeFactory() = default;
};

// concrete creators
class CircleFactory : public ShapeFactory {
public:
    std::unique_ptr<Shape> create() override
    {
        return std::make_unique<Circle>();
    }
};

class SquareFactory : public ShapeFactory {
public:
    std::unique_ptr<Shape> create() override
    {
        return std::unique_ptr<Square>();
    }
};

int main()
{

    std::unique_ptr<ShapeFactory> circleFactory =
        std::make_unique<CircleFactory>();
    std::unique_ptr<ShapeFactory> squareFactory =
        std::make_unique<SquareFactory>();

    std::unique_ptr<Shape> circle = circleFactory->create();
    std::unique_ptr<Shape> square = squareFactory->create();

    circle->draw();
    square->draw();

    return 0;
}
