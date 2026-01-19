// Facade Pattern
// source: https://www.hellointerview.com/learn/low-level-design/in-a-hurry/patterns
// type: structural
// use: when you want to hide internal complexity behind a simple entry point

#include <string>
 
enum class GameState { IN_PROGRESS, WON, DRAW };

class Board {
public:
  bool placeMark(int row, int col, const std::string& mark) {
    // Place mark logic
    return true;
  }

  bool checkWin(int row, int col) {
    // Check win logic
    return false;
  }

  bool isFull() {
    // Check if board is full
    return false;
  }
};

class Player {
public:
  explicit Player(std::string mark) : mark(std::move(mark)) {}
  const std::string& getMark() const { return mark; }

private:
  std::string mark;
};

class Game {
public:
  Game() : board(), playerX("X"), playerO("O"), currentPlayer(&playerX), state(GameState::IN_PROGRESS) {}

  bool makeMove(int row, int col) {
    if (state != GameState::IN_PROGRESS) return false;
    if (!board.placeMark(row, col, currentPlayer->getMark())) return false;

    if (board.checkWin(row, col)) {
      state = GameState::WON;
    } else if (board.isFull()) {
      state = GameState::DRAW;
    } else {
      currentPlayer = currentPlayer == &playerX ? &playerO : &playerX;
    }
    return true;
  }

private:
  Board board;
  Player playerX;
  Player playerO;
  Player* currentPlayer;
  GameState state;
};

// Usage
// Game game;
// game.makeMove(0, 0);
// game.makeMove(1, 1);