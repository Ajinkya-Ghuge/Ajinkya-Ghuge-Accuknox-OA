from rectangle_demo.rectangle import Rectangle


def main():
    print("Rectangle Class - Example Usage")
    print("=" * 50)
    
    # Create a rectangle
    rect = Rectangle(length=10, width=5)
    print(f"\nCreated Rectangle: length={rect.length}, width={rect.width}")
    
    # Iterate and print each value
    print("\nIterating over Rectangle:")
    for item in rect:
        print(f"  {item}")
    
    # Using list comprehension
    print("\nUsing list comprehension:")
    items = [item for item in rect]
    print(f"  {items}")
    
    # Using next() with iterator
    print("\nUsing next() with iterator:")
    rect_iter = iter(rect)
    first_item = next(rect_iter)
    second_item = next(rect_iter)
    print(f"  First: {first_item}")
    print(f"  Second: {second_item}")
    
    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()
