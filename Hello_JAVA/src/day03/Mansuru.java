package day03;

public class Mansuru {
	int money = 2400;
	int cnt_building = 10;
	
	void buyBuilding(int money) {
		cnt_building += money; // 1조당 빌딩 한채
		money -= money;
	}
}
