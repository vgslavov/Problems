class Deck {
	public:
		Deck();
		Card deal();
		Card card_at(int pos);
		void shuffle();
		int cards_left();
	private:
		vector<Card> deck (52);
};

class Hand {
	public:
		Hand();
		void clear();
		void add_card(Card c);
		void remove_card(Card c);
		void remove_card(int pos);
		Card get_card(int pos);
		int get_card_count();
		void sort_suit();
		void sort_value();
};

class Card {
	public:
		Card(int val, int s);
		enum Suits { CLUBS, SPADES, HEARTS, DIAMONDS };
		enum Values { ACE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, JACK, QUEEN, KING };	
		int get_suit();
		int get_value();
		string get_value2str()
		string get_suit2str();
		void print_card();
	private:
		int value;
		int suit;
};

class Pot {

    private:
        vector<int> amounts;
        vector<id> players;
};

class Game {

    private:
        Deck d;
        Pot p;
        vector<Player> players;
};

class Player: public User {
    public:
        bool bet(int amount);
        bool fold();
        bool request(Card c);

    private:
        Hand h;
        double money;
        int id;
};

class User {

    private:
        string name;
        string picture;
        string location;
};

Card::Card(int val, int s)
{
	// ATTN: check for valid input!;
	value = val;
	suit = s;
}

string
Card::get_suit2str()
{
	switch(suit) {
	case CLUBS: return "Clubs";
	case SPADES: return "Spades";
	case HEARTS: return "Hearts";
	case DIAMONDS: return "Diamonds";
	default:	return "Joker";
	}
}

string
Card::get_value2str()
{
	string str;

	if (value > 2 && value < 11) {
		str.to_string(value);
		return str;
	} else {
		switch(value) {
		case 1: return "Ace";
		case 11: return "Jack";
		case 12: return "Queen";
		case 13: return "King";
		default: return NULL;
		}
	}
}

int
Card::get_value()
{
	return value;
}

int
Card::get_suit()
{
	return suit;
}

void
Deck::shuffle()
{
	random_shuffle(deck.begin(), deck.end());
}
