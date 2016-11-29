package edu.ncssm.cs.freestream.gui;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Dimension;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.border.MatteBorder;

import edu.ncssm.cs.freestream.gui.views.HomeView;
import edu.ncssm.cs.freestream.gui.views.LocalFilesView;
import edu.ncssm.cs.freestream.gui.views.MainView;
import edu.ncssm.cs.freestream.gui.views.NavigationView;
import edu.ncssm.cs.freestream.gui.views.PlaybackControlView;
import edu.ncssm.cs.freestream.gui.views.QueueView;
import edu.ncssm.cs.freestream.gui.views.SongView;

/**
 * An extension of JFrame to display and run FreeStream.
 * 
 * @author Josh Rees-Jones
 */
@SuppressWarnings("serial")
public class FreeStreamFrame extends JFrame {
	// center panel
	private MainView display = new LocalFilesView();
	
	// album art, song name, link
	private SongView songDisplay = new SongView();
	// queued songs
	private QueueView queue = new QueueView();
	
	// play, pause, forward, backward, shuffle, repeat
	private PlaybackControlView controls = new PlaybackControlView();
	
	// navigation to local files and different services
	private NavigationView navigation = new NavigationView();
	
	/**
	 * Constructs a new FreeStreamFrame and initializes the GUI.
	 */
	public FreeStreamFrame() {
		initGUI();
	}
	
	/**
	 * Prepares the GUI for display. Configures and builds GUI components and
	 * adds them to the frame.
	 */
	private void initGUI() {
		// use JScrollPanes for areas that might need to scroll
		JScrollPane navigationScrollPane = new JScrollPane(navigation);
		JScrollPane queueScrollPane = new JScrollPane(queue);
		
		// Set borders to clean it up
		// MatteBorder(top, left, bottom, right, color)
		songDisplay.setBorder(new MatteBorder(0, 1, 0, 0, Color.BLACK));
		controls.setBorder(new MatteBorder(1, 0, 0, 0, Color.BLACK));
		
		display.setBackground(new Color(0, 0, 0, 125));

		// make sidebar (only used as a container for layout)
		JPanel sidebar = new JPanel();
		sidebar.setLayout(new BorderLayout());
		sidebar.add(songDisplay, BorderLayout.NORTH);
		sidebar.add(queueScrollPane, BorderLayout.CENTER);
		
		// add panels
		this.add(display, BorderLayout.CENTER);
		this.add(sidebar, BorderLayout.EAST);
		this.add(controls, BorderLayout.SOUTH);
		this.add(navigationScrollPane, BorderLayout.WEST);
		
		// Basic JFrame tasks
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.setMinimumSize(new Dimension(600, 460));
		this.setExtendedState(JFrame.MAXIMIZED_BOTH);
		this.setTitle("FreeStream");
		this.setLocationRelativeTo(null);
	}
}
