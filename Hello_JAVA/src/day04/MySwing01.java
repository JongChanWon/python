package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JToolBar;
import javax.swing.JButton;
import javax.swing.JLabel;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing01 extends JFrame {

	private JPanel contentPane;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing01 frame = new MySwing01();
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
	public MySwing01() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JButton btn = new JButton("click");
		
		btn.setBounds(156, 11, 117, 36);
		contentPane.add(btn);
		
		JLabel lbl = new JLabel("Good Morning");
		lbl.setBounds(61, 11, 83, 36);
		contentPane.add(lbl);
		
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				
				lbl.setText("Good Evening");
			}
			@Override
			public void mousePressed(MouseEvent e) {
				lbl.setText("Good Morning");
			}
			@Override
			public void mouseEntered(MouseEvent e) {
				lbl.setText("Good Evening");
			}
		});
		
//		if(lbl.equals(new JLabel("Good Morning"))) {
//			btn.addActionListener(event -> {
//				lbl.setText("Good Evening");
//			});
//		} else {
//			btn.addActionListener(event -> {
//			lbl.setText("Good Evening");
//			});
//		}
		
	}
}
