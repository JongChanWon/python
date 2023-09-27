package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JLabel;
import java.awt.BorderLayout;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class MySwing02 {

	private JFrame frame;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing02 window = new MySwing02();
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
	public MySwing02() {
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
		
		JLabel lblNewLabel = new JLabel("100");
		lblNewLabel.setBounds(86, 40, 63, 23);
		frame.getContentPane().add(lblNewLabel);
		
		JButton btn = new JButton("increase");
		btn.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				int count = Integer.parseInt(lblNewLabel.getText());
				count++;
				lblNewLabel.setText(String.valueOf(count));
				myClick();
			}
		});
		btn.setBounds(182, 40, 97, 23);
		frame.getContentPane().add(btn);
		
		JButton btn2 = new JButton("reset");
		btn2.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				lblNewLabel.setText("0");
			}
		});
		btn2.setBounds(182, 76, 97, 23);
		frame.getContentPane().add(btn2);
	}
	public void myClick() {
	}
	
	
}
