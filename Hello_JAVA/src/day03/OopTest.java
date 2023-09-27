package day03;

public class OopTest {
	public static void main(String[] args) {
		Animal ani = new Animal();
		System.out.println(ani.age);
		ani.go1year();
		System.out.println(ani.age);
		
		Human hum = new Human();
		System.out.println(hum.nation);
		hum.immigration("미국");
		System.out.println(hum.nation);
		
		System.out.println(hum.age);
		hum.go1year();
		System.out.println(hum.age);
	}
}
