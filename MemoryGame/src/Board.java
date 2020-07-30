import java.awt.Color;
import java.awt.Container;
import java.awt.FlowLayout;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JFrame;


public class Board  extends JFrame{
	
	public Board() {
		setTitle("Memory Game");
		setSize(400, 500);

		//ButtonActionHandler bah = new ButtonActionHandler();
		
		//He's the judge, jury, and code executioner.
		Judge dredd = new Judge();

		Container c = getContentPane();
		c.setLayout(new GridLayout(3,4));
		
		for(int i=0; i<12; i++) {
			Card b1 = new Card(Color.RED);
			b1.addActionListener(dredd);
			c.add(b1);
		}

		

		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setVisible(true);
	}
	
	public static void main(String[] args) {
		new Board();
	}
	
	private class Judge implements ActionListener{

		@Override
		public void actionPerformed(ActionEvent arg0) {
			// which card was clicked?
			Object clickedObject = arg0.getSource();
			((Card) clickedObject).faceUp();
		}
		
	}
}
