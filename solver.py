import itertools


class Card:
    
    def __init__(self, color: str, number: str, shape: str, shade: str, counter: int) -> None:
        self.color = color
        self.number = number
        self.shape = shape
        self.shade = shade
        self.cardID = counter


def getAttribute(name):
    
    attributes = {
        "color": {"red", "green", "purple"},
        "number": {"1","2","3"},
        "shape": {"diamond", "squiggle", "oval"},
        "shade": {"empty", "half", "full"},
        }

    attribute = str(input(f"{name}: "))

    if attribute not in attributes[name]:
        print(f"acceptable {name}s: {attributes[name]}")
        attribute = getAttribute(name)
    
    return attribute

def getBoardSize():
    board_size = int(input("Board Size: "))
    if board_size < 3 or board_size > 81:
        print("board size cannot be smaller than 3 or greater than 81")
        board_size = getBoardSize()
    
    return board_size

def main():
    
    # the board is a list of cards
    board = []
    
    board_size = getBoardSize()

    for i in range(board_size):
        print(f"\nCard {i}")
        color = getAttribute("color")
        number = getAttribute("number")
        shape = getAttribute("shape")
        shade = getAttribute("shade")
        
        board.append(Card(color,number,shape,shade,i))

    # calculate all possible combinations of three cards on the board
    coms = itertools.combinations(board, 3)


    """
    a SET occurs when, for each combination of three cards, for each type of attribute,
    there are either three unique values or one shared value.

    a combination constitute a SET if no collection of attributes contains 2 unique values.
    """

    for combination in coms:
        colors = []
        numbers = []
        shapes = []
        shades = []

        for card in combination:
            colors.append(card.color)
            numbers.append(card.number)
            shapes.append(card.shape)
            shades.append(card.shade)
        
        if 2 not in {len(set(colors)), len(set(numbers)), len(set(shapes)), len(set(shades))}:
            print("SET FOUND")
            for card in combination:
                print(card.color, card.number, card.shape, card.shade, card.cardID)
            
    
    
if __name__ == '__main__':
    main()
