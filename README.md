
Overview
CardGames is a Python project that simulates popular card games like Poker and Truco. It provides the core functionalities to create card objects, manage hands, and evaluate them according to the rules of the respective games.

##
Features
- **Card Class**: Basic representation of a card with values and suits.
- **Hand Evaluation**: Methods to evaluate poker hands.
- **Poker Ranking**: Comparison between different poker hands.
- **Truco Card**: Specific rules and ranking for Truco cards.
- **Unit Tests**: Comprehensive unit tests to ensure the correctness of hand evaluations and other functionalities.

##
Installation Instructions
To set up and run this project, follow these steps:

1. Clone the repository:
   ```sh
   git clone https://github.com/ehernandez/CardGames.git
   ```

2. Navigate to the project directory:
   ```sh
   cd CardGames
   ```

3. It's recommended to create a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

##
Usage Examples
### PokerHand Evaluation
To evaluate poker hands, you can create instances of `Card` and `PokerHand`:

```python
from src.CardGame import Card
from src.PokerHand import PokerHand

high_card_hand_1 = [Card('4','D'), Card('K','H'), Card('3','D'), Card('10','D'), Card('J','D')]
poker_hand = PokerHand()
evaluated = poker_hand.evaluate(high_card_hand_1)
print(f'Hand Evaluation: {evaluated}')
```

### TrucoHand Evaluation
For Truco, you can use the `Truco_Card` class:

```python
from src.TrucoHand import Truco_Card, Truco_Hand_Evaluator

espadao = Truco_Card('A','S')
bastiao = Truco_Card('A','C')
manilha_espada = Truco_Card('7','S')

truco_hand_evaluator = Truco_Hand_Evaluator()
winner = truco_hand_evaluator.winner([espadao, bastiao, manilha_espada])
print(f'Winner: {winner}')
```

##
Code Summary
- **`CardGame.py`**: Defines the `Card` class and the abstract `Hand` class, providing basic methods to get card values and determine if all cards have the same suit.
- **`PokerHand.py`**: Extends `Hand` class to implement Poker-specific hand evaluations and ranking comparisons.
- **`TrucoHand.py`**: Extends the `Card` class to define Truco-specific card rankings and provides the `Truco_Hand_Evaluator` for hand evaluations.
- **Unit Tests**:
  - **`BasicHandTests.py`**: Contains basic tests for the abstract `Hand` class.
  - **`PokerHandTests.py`**: Contains tests for poker hands, checking various hand types.
  - **`TrucoHandTests.py`**: Contains tests for Truco hand evaluations.

##
Contributing Guidelines
We welcome contributions! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix:
   ```sh
   git checkout -b feature-name
   ```
3. Commit your changes and push them to your fork:
   ```sh
   git commit -m 'Add a descriptive commit message'
   git push origin feature-name
   ```
4. Create a pull request describing your changes.

Please ensure that all new code includes appropriate unit tests.

##
License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.