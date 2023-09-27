package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JTextArea;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing05 extends JFrame {

	private JPanel contentPane;
	private JTextField tx;
	private JTextArea ta;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing05 frame = new MySwing05();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public MySwing05() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 315, 480);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl = new JLabel("출력단수:");
		lbl.setBounds(30, 38, 57, 15);
		contentPane.add(lbl);
		
		tx = new JTextField();
		tx.setBounds(99, 35, 77, 18);
		contentPane.add(tx);
		tx.setColumns(10);
		
		JButton btn = new JButton("출력하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				gugudan();
			}
		});
		btn.setBounds(30, 88, 146, 23);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setBounds(30, 142, 146, 231);
		contentPane.add(ta);
	}
	public void gugudan() {
		String dan = tx.getText();
		for(int i = 2; i < 10; i++) {
			for(int j = 1; j < 10; j++) {
				int num = Integer.parseInt(dan);
				ta.setText(i + "*" + j + " = " + i*j);
				
			}
		}
	}
}
