import javax.swing.JButton;
import java.awt.Color;
import java.awt.Dimension;

public class Card extends JButton {
	private Color faceColor;
	private static int width = 200, height= 150;
	
	
	public Card(Color fc) {
		faceColor=fc;
		setPreferredSize(new Dimension(width,height));
	}
	public void faceUp() {
		setBackground(faceColor);
		paintImmediately(0,0,getWidth(),getHeight());
	}
}
