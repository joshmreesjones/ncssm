package edu.ncssm.cs.freestream;

import javax.swing.JOptionPane;
import javax.swing.SwingUtilities;
import javax.swing.UIManager;

import edu.ncssm.cs.freestream.daemon.PlaybackDaemon;
import edu.ncssm.cs.freestream.gui.FreeStreamFrame;
import edu.ncssm.cs.freestream.PlayQueue;

/**
 * The main class of FreeStream. Contains the main method.
 * 
 * @author Josh Rees-Jones
 */
public class Main {
	/**
	 * The main method of FreeStream. Sets the look and feel to
	 * JTattoo's HiFi theme and creates and shows the frame.
	 * 
	 * @param args unused
	 */
	public static void main(String[] args) {
		SwingUtilities.invokeLater(new Runnable() {
			public void run() {
				try {
					// set the look and feel to JTattoo's Hi-Fi theme
					UIManager.setLookAndFeel("com.jtattoo.plaf.hifi.HiFiLookAndFeel");
				} catch (Exception exception) {
					JOptionPane.showMessageDialog(null, "GUI skin could not be loaded. Proceeding with default skin.");
				}

				// initialize the PlaybackDaemon
				PlaybackDaemon.init();
			
				// make the frame
				FreeStreamFrame frame = new FreeStreamFrame();
				frame.setVisible(true);
			}
		});
	}
}
