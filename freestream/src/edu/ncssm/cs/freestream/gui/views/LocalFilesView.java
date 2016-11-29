package edu.ncssm.cs.freestream.gui.views;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.BorderLayout;
import java.util.ArrayList;

import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import javax.swing.ListSelectionModel;

import edu.ncssm.cs.freestream.daemon.LocalFilesDaemon;
import edu.ncssm.cs.freestream.daemon.PlaybackDaemon;
import edu.ncssm.cs.freestream.daemon.UninitializedException;
import edu.ncssm.cs.freestream.gui.SongTable;
import edu.ncssm.cs.freestream.gui.SongTableModel;
import edu.ncssm.cs.freestream.Song;

/**
 * This is the display of local song files stored on the user's computer.
 * 
 * @author Josh Rees-Jones
 */
@SuppressWarnings("serial")
public class LocalFilesView extends MusicView {
	private LocalFilesDaemon daemon = new LocalFilesDaemon();

	// the list of songs stored on the user's computer
	private ArrayList<Song> songsList;
	
	/**
	 * Constructs a LocalFilesView.
	 */
	public LocalFilesView() {
		initView();
	}

	/**
	 * Initializes the view.
	 */
	private void initView() {
		// BorderLayout is used so that the JTable fills the panel
		this.setLayout(new BorderLayout());

		// get all local songs
		songsList = daemon.getSongs();

		// column headers
		String[] columns = {
			"Track",
			"Artist",
			"Length",
			"Album"
		};

		// data to be displayed in the SongTable
		// data[number of songs][number of columns]
		Object[][] data = new Object[songsList.size()][columns.length];
		// populate data with information
		for (int i = 0; i < data.length; i++) {
			// the current Song
			Song song = songsList.get(i);

			// track name
			data[i][0] = song.getTrackName();

			// artist
			data[i][1] = song.getArtist();

			// length
			data[i][2] = song.getLength();

			// album
			data[i][3] = song.getAlbum();
		}

		// create the table to display all of the songs
		System.out.println(data);
		System.out.println(columns);
		SongTable songTable = new SongTable(new SongTableModel(data, columns));
		songTable.addMouseListener(new SongTableListener());

		// enclose the table in a JScrollPane so users can scroll
		JScrollPane songTableScrollPane = new JScrollPane(songTable);

		// add the scroll pane
		this.add(songTableScrollPane, BorderLayout.CENTER);
	}

	/**
	 * The MouseListener to detect events for SongTable.
	 * 
	 * @author Josh Rees-Jones
	 */
	private class SongTableListener extends MouseAdapter {
		/**
		 * {@inheritDoc}
		 */
		@Override
		public void mouseClicked(MouseEvent event) {
			// detect double clicks to play song
			if (event.getClickCount() == 2) {
				JTable target = (JTable) event.getSource();
				// the row index corresponds to the ArrayList<Song> index
				int songIndex = target.getSelectedRow();

				try {
					// load the appropriate song
					PlaybackDaemon.loadSong(LocalFilesView.this.songsList.get(songIndex));
				} catch (UninitializedException ex) {
					PlaybackDaemon.init();
					JOptionPane.showMessageDialog(null, "PlaybackDaemon was not initialized. " +
														"Please try playing the song again.");
				}

				PlaybackDaemon.play();
			}
		}
	}
}
