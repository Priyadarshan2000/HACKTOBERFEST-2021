from modulz import lib
if __name__ == "__main__":
    try:
        mylib = lib("list_of_books.txt", "MY LIBRARY")
        press_key_list = {"D": "Display Books", "L": "Lend Books", "A": "Add Books", "R": "Return Books", "Q": "Quit"}    
        
        key_press = False
        while(key_press != "q"):
            print(f"\n----------Welcome To {mylib.library_name}'s  Management System---------\n")
            for key, value in press_key_list.items():
                print("Press", key, "To", value)
            key_press = input("Press Key : ").lower()
            if key_press == "l":
                print("\nCurrent Selection : LEND BOOK\n")
                mylib.lend_books()
                
            elif key_press == "a":
                print("\nCurrent Selection : ADD BOOK\n")
                mylib.add_books()

            elif key_press == "d":
                print("\nCurrent Selection : DISPLAY BOOKS\n")
                mylib.display_books()
            
            elif key_press == "r":
                print("\nCurrent Selection : RETURN BOOK\n")
                mylib.return_books()
            elif key_press == "q":
                break
            else:
                continue
    except Exception as e:
        print("Something went wrong. Please check. !!!")