package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JButton;
import javax.swing.JTextField;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import javax.swing.SwingConstants;

public class MySwing06 extends JFrame {

	private JPanel contentPane;
	private JTextField textField;
	private JButton btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn0, btn_call;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing06 frame = new MySwing06();
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
	public MySwing06() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 292, 462);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		btn1 = new JButton("1");
		btn1.setBounds(12, 89, 65, 23);
		contentPane.add(btn1);
		
		btn2 = new JButton("2");
		btn2.setBounds(89, 89, 65, 23);
		contentPane.add(btn2);
		
		btn3 = new JButton("3");
		btn3.setBounds(166, 89, 65, 23);
		contentPane.add(btn3);
		
		btn4 = new JButton("4");
		btn4.setBounds(12, 122, 65, 23);
		contentPane.add(btn4);
		
		btn5 = new JButton("5");
		btn5.setBounds(89, 122, 65, 23);
		contentPane.add(btn5);
		
		btn6 = new JButton("6");
		btn6.setBounds(166, 122, 65, 23);
		contentPane.add(btn6);
		
		btn7 = new JButton("7");
		btn7.setBounds(12, 155, 65, 23);
		contentPane.add(btn7);
		
		btn8 = new JButton("8");
		btn8.setBounds(89, 155, 65, 23);
		contentPane.add(btn8);
		
		btn9 = new JButton("9");
		btn9.setBounds(166, 155, 65, 23);
		contentPane.add(btn9);
		
		btn0 = new JButton("0");
		btn0.setBounds(12, 188, 65, 23);
		contentPane.add(btn0);
		
		btn_call = new JButton("☎");
		btn_call.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				
//				System.out.println(e.getSource());
			}
		});
		btn_call.setBounds(89, 188, 142, 23);
		contentPane.add(btn_call);
		
		textField = new JTextField();
		textField.setHorizontalAlignment(SwingConstants.RIGHT);
		textField.setBounds(12, 23, 219, 37);
		contentPane.add(textField);
		textField.setColumns(10);
		
		btn1.addMouseListener(new MouseAdapter() {public void mouseClicked(MouseEvent e) {myClick(e);}});
		btn2.addMouseListener(new MouseAdapter() {public void mouseClicked(MouseEvent e) {myClick(e);}});
		btn3.addMouseListener(new MouseAdapter() {public void mouseClicked(MouseEvent e) {myClick(e);}});
		btn4.addMouseListener(new MouseAdapter() {public void mouseClicked(MouseEvent e) {myClick(e);}});
		btn5.addMouseListener(new MouseAdapter() {public void mouseClicked(MouseEvent e) {myClick(e);}});
		btn6.addMouseListener(new MouseAdapter() {public void mouseClicked(MouseEvent e) {myClick(e);}});
		btn7.addMouseListener(new MouseAdapter() {public void mouseClicked(MouseEvent e) {myClick(e);}});
		btn8.addMouseListener(new MouseAdapter() {public void mouseClicked(MouseEvent e) {myClick(e);}});
		btn9.addMouseListener(new MouseAdapter() {public void mouseClicked(MouseEvent e) {myClick(e);}});
		btn0.addMouseListener(new MouseAdapter() {public void mouseClicked(MouseEvent e) {myClick(e);}});
		
		btn_call.addMouseListener(new MouseAdapter() {public void mouseClicked(MouseEvent e) {myCall();}});
	}
	
	public void myCall() {
		String str_tel = textField.getText();
		JOptionPane.showMessageDialog(null, "Calling\n" + str_tel);
	}
	
	public void myClick(MouseEvent e) {
		JButton jbtn = (JButton) e.getSource();
		String str_new = jbtn.getText();
		String str_old = textField.getText();
		textField.setText(str_old + str_new);
	}
}
