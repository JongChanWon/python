package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.Iterator;
import java.util.Random;

public class MySwing04 extends JFrame {

	private JPanel contentPane;
	private JLabel lbl01;
	private JLabel lbl02;
	private JLabel lbl03;
	private JLabel lbl04;
	private JLabel lbl05;
	private JLabel lbl06;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing04 frame = new MySwing04();
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
	public MySwing04() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);

		lbl01 = new JLabel("__");
		lbl01.setBounds(40, 26, 31, 15);
		contentPane.add(lbl01);

		lbl02 = new JLabel("__");
		lbl02.setBounds(94, 26, 31, 15);
		contentPane.add(lbl02);

		lbl03 = new JLabel("__");
		lbl03.setBounds(162, 26, 31, 15);
		contentPane.add(lbl03);

		lbl04 = new JLabel("__");
		lbl04.setBounds(229, 26, 31, 15);
		contentPane.add(lbl04);

		lbl05 = new JLabel("__");
		lbl05.setBounds(296, 26, 31, 15);
		contentPane.add(lbl05);

		lbl06 = new JLabel("__");
		lbl06.setBounds(351, 26, 31, 15);
		contentPane.add(lbl06);

		JButton btn = new JButton("로또생성하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				lotto();
			}
		});
		btn.setBounds(94, 69, 233, 23);
		contentPane.add(btn);
	}

	public void lotto() {

		int[] lotto = new int[6];

		for (int i = 0; i < lotto.length; i++) {
			lotto[i] = (int) (Math.random() * 45) + 1;

			for (int j = 0; j < i; j++) {
				if (lotto[i] == lotto[j]) {
					i--;
					break;
				}
			}
		}

		for (int i = 0; i < lotto.length; i++) {
			lbl01.setText(lotto[0] + "");
			lbl02.setText(lotto[1] + "");
			lbl03.setText(lotto[2] + "");
			lbl04.setText(lotto[3] + "");
			lbl05.setText(lotto[4] + "");
			lbl06.setText(lotto[5] + "");
		}

	}
}
