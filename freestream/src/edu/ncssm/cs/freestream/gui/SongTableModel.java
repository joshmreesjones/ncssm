package edu.ncssm.cs.freestream.gui;

import java.util.ArrayList;

import javax.swing.table.DefaultTableModel;

import edu.ncssm.cs.freestream.Song;

public class SongTableModel extends DefaultTableModel {
	// data to be displayed in the song table
	private Object[][] data;

	/**
	 * Constructs a SongTableModel with the specified list of songs.
	 * 
	 * @param songsList the list of songs to be displayed
	 */
	public SongTableModel(Object[][] data, String[] columnNames) {
		/*
		// the column names to be used
		String[] columns = {
			"Track",
			"Artist",
			"Length",
			"Album"
		};

		// data[row][column]
		data = new Object[songsList.size()][columns.length];

		// populate data with information
		for (int i = 0; i < data.length; i++) {
			// the current song
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
		*/
		super(data, columnNames);
	}

	/**
	 * Returns true if the cell at rowIndex and columnIndex is editable.
	 * AbstractTableModel by default returns false, but this overrides
	 * that just in case.
	 * 
	 * @param rowIndex the row index of the cell to be queried
	 * @param columnIndex the column index of hte cell to be queried
	 * @return true if the cell at rowIndex and columnIndex is editable (always returns false)
	 */
	public boolean isCellEditable(int rowIndex, int columnIndex) {
		return false;
	}

	public Class getColumnClass(int column) {
		System.out.println(data);
		//System.out.println(column);
		//System.out.println(data[0]);
		//System.out.println(data[0][column]);
		//System.out.println(data[0][column].getClass());
		return data[0][column].getClass();
	}
}
