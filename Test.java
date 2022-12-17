 import javax.swing.ImageIcon;

    import javax.swing.JFrame;

    import javax.swing.JLabel;

    import javax.swing.JPanel;

        

    public class Test {

   

      public static void main(String[] args) {

        

        //Without JPanel images would be added to JFrame on top of each other.

        //That way only last image would be visible.

        JPanel  panel                 = new JPanel ();

                panel.add (new JLabel (new ImageIcon ("C:/Temp/warrior.png")));

                panel.add (new JLabel (new ImageIcon ("C:/Temp/dragon.png" )));

   

        JFrame  frame                 = new JFrame ("Display multiple images from files.");

                frame.getContentPane           ().add (panel);

                frame.pack                     ();

                frame.setVisible               (true);

                frame.setDefaultCloseOperation (JFrame.EXIT_ON_CLOSE);   

 

      }

      

    }