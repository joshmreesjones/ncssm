package edu.ncssm.cs.freestream.daemon;

import java.io.File;
import java.io.IOException;
import java.net.URL;

import javax.swing.JOptionPane;

import javazoom.jlgui.basicplayer.BasicPlayer;
import javazoom.jlgui.basicplayer.BasicPlayerException;

import edu.ncssm.cs.freestream.daemon.UninitializedException;
import edu.ncssm.cs.freestream.Song;

/*
 * PlaybackDaemon manages the loading and rendering of audio in FreeStream.
 * 
 * It uses the BasicPlayer API from jlGUI. It depends on
 * 
 * Note that TinySound may not be synchronized for optimal real-time performance.
 * Sound may sometimes lag under slow circumstances.
 * 
 * @author Josh Rees-Jones
 */
public class PlaybackDaemon {
	private static BasicPlayer player;
	private static boolean initialized = false;

	public static void init() {
		player = new BasicPlayer();
		initialized = true;
	}

	public static void loadSong(Song song) throws UninitializedException {
		if (!initialized) {
			throw new UninitializedException("PlaybackDaemon has not been initialized." +
											 "Run init() first.");
		}

		try {
			player.open(song.getFile());
		} catch (BasicPlayerException ex) {
			JOptionPane.showMessageDialog(null, "An error occurred while initializing the sound player.");
		}
	}

	public static void play() {
		try {
			player.play();
		} catch (BasicPlayerException ex) {
			JOptionPane.showMessageDialog(null, "An error occurred while playing the current song.");
		}
	}

	public static void pause() {
		try {
			player.pause();
		} catch (BasicPlayerException ex) {
			JOptionPane.showMessageDialog(null, "An error occurred while pausing the current song.");
		}
	}

	public static void seek(int offset) {
	}
}
