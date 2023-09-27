package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JLabel;
import javax.swing.JButton;
import javax.swing.JTextArea;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.Iterator;

public class MySwing08 extends JFrame {

	private JPanel contentPane;
	private JTextField tf_first;
	private JTextField tf_last;
	private JTextArea ta;
	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing08 frame = new MySwing08();
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
	public MySwing08() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 352, 559);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl01 = new JLabel("첫째별수:");
		lbl01.setBounds(63, 13, 57, 15);
		contentPane.add(lbl01);
		
		JLabel lbl02 = new JLabel("끝별수:");
		lbl02.setBounds(63, 58, 57, 15);
		contentPane.add(lbl02);
		
		tf_first = new JTextField();
		tf_first.setBounds(140, 10, 116, 21);
		contentPane.add(tf_first);
		tf_first.setColumns(10);
		
		tf_last = new JTextField();
		tf_last.setColumns(10);
		tf_last.setBounds(140, 55, 116, 21);
		contentPane.add(tf_last);
		
		JButton btn = new JButton("별그리기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				drawStar();
			}
		});
		btn.setBounds(63, 103, 193, 23);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setBounds(63, 159, 193, 257);
		contentPane.add(ta);
	}
	
	public String getStar(int cnt) {
		String ret = "";
		for(int i = 0; i < cnt; i++) {
			ret += "*";
		}
		ret += "\n";
		return ret;
	}
	
	public void drawStar() {
		String fStar = tf_first.getText();
		String lStar = tf_last.getText();
		
		int star1 = Integer.parseInt(fStar);
		int star2 = Integer.parseInt(lStar);
		
		String txt = "";
		for(int i = star1; i <= star2; i++) {
			txt += getStar(i);
		}
		ta.setText(txt);
		
//		System.out.println(star1);
//		for(int i = 0; i < star2; i++) {
//			for(int j = 0; j < star1; j++) {
//				ta.append("*");
//			}
//			ta.append("\n");
//		}
		
	}
}










