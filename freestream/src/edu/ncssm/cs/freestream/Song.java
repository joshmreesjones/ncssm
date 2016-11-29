package edu.ncssm.cs.freestream;

import com.mpatric.mp3agic.InvalidDataException;
import com.mpatric.mp3agic.Mp3File;
import com.mpatric.mp3agic.UnsupportedTagException;

import java.io.File;
import java.io.IOException;

import javax.swing.JOptionPane;

public class Song {
	private File soundFile;
	// this Mp3File is used to extract ID3 (or other)
	// tag information.
	private Mp3File mp3File;

	private String trackName;
	private String fileName;
	private String artist;
	private String album;
	private int length;

	public Song(File soundFile) {
		this.soundFile = soundFile;
	}

	public File getFile() {
		return soundFile;
	}

	public String getTrackName() {
		return soundFile.getName();
	}

	public String getArtist() {
		return "artist";
	}

	/**
	 * Returns the length of the song in seconds.
	 */
	public int getLength() {
		return 42;
	}

	public String getAlbum() {
		return "album";
	}
}
