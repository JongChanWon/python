package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.Random;

public class MySwing07 extends JFrame {
	// 전역변수 되도록이면 많이 쓰지 말자
	private JPanel contentPane;
	private JTextField tf_mine;
	private JTextField tf_com;
	private JTextField tf_result;
	
	private JLabel lbl_mine;
	private JLabel lbl_com;
	private JLabel lbl_result;
	
	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing07 frame = new MySwing07();
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
	public MySwing07() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 311, 499);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		lbl_mine = new JLabel("나:");
		lbl_mine.setBounds(12, 30, 57, 15);
		contentPane.add(lbl_mine);
		
		lbl_com = new JLabel("컴:");
		lbl_com.setBounds(12, 72, 57, 15);
		contentPane.add(lbl_com);
		
		lbl_result = new JLabel("결과:");
		lbl_result.setBounds(12, 109, 57, 15);
		contentPane.add(lbl_result);
		
		tf_mine = new JTextField();
		tf_mine.setBounds(102, 27, 116, 21);
		contentPane.add(tf_mine);
		tf_mine.setColumns(10);
		
		tf_com = new JTextField();
		tf_com.setColumns(10);
		tf_com.setBounds(102, 69, 116, 21);
		contentPane.add(tf_com);
		
		tf_result = new JTextField();
		tf_result.setColumns(10);
		tf_result.setBounds(102, 106, 116, 21);
		contentPane.add(tf_result);
		
		JButton btn = new JButton("게임하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				game();
//				myClick(); // 쌤 로직
			}
		});
		btn.setBounds(12, 151, 206, 23);
		contentPane.add(btn);
	}
	
	public void game() {
		double rnd = Math.random();
		
		if(rnd > 0.66) {
			tf_com.setText("가위");
		} else if(rnd > 0.33) {
			tf_com.setText("바위");
		} else {
			tf_com.setText("보");
		}
		
		
		if(tf_mine.getText().equals(tf_com.getText())) {
			tf_result.setText("비김");
		} else if((tf_mine.getText().equals("가위") && tf_com.getText().equals("바위") || 
				  (tf_mine.getText().equals("바위") && tf_com.getText().equals("보")) || 
				  (tf_mine.getText().equals("보") && tf_com.getText().equals("가위")))) {
			tf_result.setText("패배");
		} else {
			tf_result.setText("승리");
		}
	}
	
	public void myClick() {
		String mine = tf_mine.getText();
		String com = "";
		String result = "";
		
		double rnd = Math.random();
		if(rnd > 0.66) {
			com = "가위";
		} else if(rnd > 0.33) {
			com = "바위";
		} else {
			com = "보";
		}
		
		if(com.equals("가위") && mine.equals("가위")) result = "비김";
		if(com.equals("가위") && mine.equals("바위")) result = "이김";
		if(com.equals("가위") && mine.equals("보")) result = "짐";
		
		if(com.equals("바위") && mine.equals("바위")) result = "비김";
		if(com.equals("바위") && mine.equals("보")) result = "이김";
		if(com.equals("바위") && mine.equals("가위")) result = "짐";
		
		if(com.equals("보") && mine.equals("보")) result = "비김";
		if(com.equals("보") && mine.equals("가위")) result = "이김";
		if(com.equals("보") && mine.equals("바위")) result = "짐";
		
		tf_com.setText(com);
		tf_result.setText(result);
		
	}

}
