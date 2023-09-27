package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.JLabel;
import javax.swing.JButton;

public class MySwing03 {

	private JFrame frame;
	private JTextField tx1;
	private JTextField tx2;
	private JTextField tx3;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing03 window = new MySwing03();
					window.frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the application.
	 */
	public MySwing03() {
		initialize();
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		frame = new JFrame();
		frame.setBounds(100, 100, 450, 300);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.getContentPane().setLayout(null);
		
		tx1 = new JTextField();
		tx1.setBounds(32, 22, 62, 21);
		frame.getContentPane().add(tx1);
		tx1.setColumns(10);
		
		tx2 = new JTextField();
		tx2.setColumns(10);
		tx2.setBounds(124, 22, 62, 21);
		frame.getContentPane().add(tx2);
		
		tx3 = new JTextField();
		tx3.setColumns(10);
		tx3.setBounds(253, 22, 62, 21);
		frame.getContentPane().add(tx3);
		
		JLabel lblNewLabel = new JLabel("+");
		lblNewLabel.setBounds(104, 22, 18, 21);
		frame.getContentPane().add(lblNewLabel);
		
		JButton btn = new JButton("=");
		btn.setBounds(195, 22, 46, 21);
		frame.getContentPane().add(btn);
		
		btn.addActionListener(event -> {
			myClick();
		});
		
		
	}
	
	public void myClick() {
		String a = tx1.getText();
		String b = tx2.getText();
		
		int aa = Integer.parseInt(a);
		int bb = Integer.parseInt(b);
		
		int sum = aa + bb;
		tx3.setText(sum + "");
		
	}
}
